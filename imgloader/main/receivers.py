from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import MediaImg


@receiver([post_save], sender=MediaImg)
def send_email_notification(sender, instance, **kwargs):
    send_mail('Загружено новое изображение',
              f'{instance.author}, {instance.created_at}, {settings.PROJECT_URL}/media/{instance.img}',
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[instance.author.email],
              fail_silently=True
              )
