from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Comment, Post


@receiver(post_save, sender=Comment)
def notify_user_post(sender, instance, created, **kwargs):

    commentator = None
    first_name = None
    title_post = instance.post.title
    text_comment = instance.body
    link_post = f'{settings.SITE_URL}/post/{instance.post.slug}'

    subject = None
    email = None

    if created:
        print('Hello, I am a created comment!!!')

        commentator = instance.commentator
        user = instance.post.author
        first_name = user.first_name if user.first_name else user.username

        subject = f'{settings.SITE_URL}/post/{instance.post.slug}! New commentary on your post'
        email = user.email

    html_content = render_to_string(
        'post_created_email.html',
        {
            'commentator': commentator,
            'name': first_name,
            'text_comment': text_comment,
            'title_post': title_post,
            'link': link_post,
        }
    )

    message = EmailMultiAlternatives(
        subject=subject,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email]
    )
    print(email)
    message.attach_alternative(html_content, 'text/html')
    message.send()