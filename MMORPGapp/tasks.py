# from celery import shared_task
# import time
#
# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.template.loader import render_to_string
#
# from .models import Comment
#
#
# @shared_task
# def send_notifications(slug, body, author):
#     html_content = render_to_string(
#         'post_created_email.html',
#         {
#             'text': body,
#             'link': f'{settings.SITE_URL}/post/{slug}'
#         }
#     )
#     msg = EmailMultiAlternatives(
#         subject=body,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=author
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
#
#
# @receiver(post_save, sender=Comment)
# def notify_abt_new_post(sender, instance, **kwargs):
#     if kwargs['action'] == 'add_comment':
#         print('Hello, Im signal')
#         comments = instance.Comment.all()
#         commentator: list[str] = []
#         for comment in comments:
#             commentator += comment.commentator.all()
#
#         commentator = [s.email for s in commentator]
#         print(commentator)
#
#         send_notifications.delay(instance.slug, instance.body, commentator)
#
