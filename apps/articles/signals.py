from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.articles.models import Article
from apps.notify.models import Notification
from apps.users.models import User

@receiver(post_save, sender=Article)
def create_notifications(sender, instance, created, **kwargs):
    if created:
        followers = User.objects.filter(followers__user=instance.user)
        for follower in followers:
            Notification.objects.create(
                recipient=follower,
                message=f"New article '{instance.title}' published by {instance.user.username}",
                article=instance
            )