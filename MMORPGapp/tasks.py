import datetime


from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import  User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Post

@shared_task
def send_notifications(title, body, slug, subscribers):
    html_content = render_to_string(
        'New_post.html',
        {

            'text': body,
            'link': f'{settings.SITE_URL}/post/{slug}',
        }
    )

    message = EmailMultiAlternatives(
        subject=title,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )
    message.attach_alternative(html_content, 'text/html')
    message.send()

@shared_task
def send_newsletter():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    subscribers = User.objects.filter(groups__name='subscribed_users').values_list('email', flat=True)
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(post_save, sender=Post)
def send_newsletter_signal(sender, instance, created, **kwargs):
    if created:
        subscribers = User.objects.filter(groups__name='subscribed_users').values_list('email', flat=True)
    else:
        # Handle other cases if necessary
        return

    send_notifications.delay(instance.title, instance.body, instance.slug, subscribers)



