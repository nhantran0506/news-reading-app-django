# Generated by Django 4.1.13 on 2024-05-29 10:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_user_is_active_user_is_staff"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_staff",
        ),
        migrations.AddField(
            model_name="user",
            name="avt_image",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="reset_code",
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="reset_code_expiry",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]