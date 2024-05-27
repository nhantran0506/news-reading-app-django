from rest_framework import serializers
from apps.users.models import User
import base64
from django.core.files.base import ContentFile

class Base64ImageField(serializers.ImageField):
    def to_representation(self, value):
        if not value:
            return None
        try:
            with open(value.path, 'rb') as f:
                return base64.b64encode(f.read()).decode()
        except Exception as e:
            return str(e)

    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)

class UserSerializer(serializers.ModelSerializer):
    avt_image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'role', 'avt_image']
        extra_kwargs = {
            'username': {'required': False},
            'password': {'write_only': True, 'required': False},
        }

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        avt_image = validated_data.pop('avt_image', None)
        
        instance = super().update(instance, validated_data)
        
        if password:
            instance.set_password(password)
        
        if avt_image:
            instance.avt_image = avt_image
        
        instance.save()
        return instance

    


from rest_framework import serializers
from apps.users.models import User
from django.utils.crypto import get_random_string
from django.utils import timezone
import datetime

from django.core.mail import send_mail

def send_reset_email(to_email, reset_code):
    subject = 'Your Password Reset Code'
    message = f'Your password reset code is {reset_code}. It will expire in 10 minutes.'
    send_mail(subject, message, 'quykuro1234567890@gmail.com', [to_email])

class ForgotPasswordSerializer(serializers.Serializer):
    username = serializers.EmailField()

    def validate_username(self, value):
        try:
            user = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        return value

    def save(self):
        username = self.validated_data['username']
        user = User.objects.get(username=username)
        reset_code = get_random_string(length=6, allowed_chars='0123456789')
        user.reset_code = reset_code
        user.reset_code_expiry = timezone.now() + datetime.timedelta(minutes=10)
        user.save()
        send_reset_email(user.username, reset_code)
        return reset_code

class ResetPasswordSerializer(serializers.Serializer):
    username = serializers.EmailField()
    reset_code = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'], reset_code=data['reset_code'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid reset code or email.")
        
        if user.reset_code_expiry < timezone.now():
            raise serializers.ValidationError("Reset code has expired.")
        return data

    def update(self, instance, validated_data):
        new_password = validated_data.pop('new_password', None)
        if new_password:
            instance.set_password(new_password)
            instance.reset_code = None  
            instance.reset_code_expiry = None
            instance.save()
        return instance

    def save(self):
        validated_data = self.validated_data
        try:
            user = User.objects.get(username=validated_data['username'])
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this username does not exist.")
        return self.update(user, validated_data)


