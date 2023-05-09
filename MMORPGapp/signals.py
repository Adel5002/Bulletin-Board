from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import Comment, Post


@receiver(post_save, sender=Comment)
def notify_user_post(sender, instance, created, **kwargs):

    template = None
    title_post = instance.post.title
    text_comment = instance.body
    link_post = f'{settings.SITE_URL}/post/{instance.post.slug}'

    if created:
        print('Hello, I am a created comment!!!')

        user = instance.post.author
        first_name = user.first_name or user.username
        template = 'post_created_email.html'

        commentator = instance.commentator or ""
        subject = f'{settings.SITE_URL}/post/{instance.post.slug}! New commentary on your post'
        email = user.email or ""

    elif instance.accept_comment:
        print('Hello, I am an accepted comment!!!')

        user = instance.commentator
        first_name = user.first_name or user.username
        template = 'email_notify_about_accepted_comment.html'

        commentator = instance.commentator or ""
        subject = f'{settings.SITE_URL}/post/{instance.post.slug}! Your commentary on the post was accepted'
        email = user.email or ""

    else:
        # Handle other cases if necessary
        return

    html_content = render_to_string(
        f'{template}',
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