from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.template.loader import render_to_string
import random
from django.shortcuts import redirect

from .models import OneTimeCode, Response


@receiver(post_save, sender=Response)
def response_created_message(sender, instance, created, **kwargs):
    if created:
        html_content = render_to_string(
            'response_created_email.html',
            {
                'username': instance.responseAuthor.username,
                'notice': instance.responseNotice.noticeTitle,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'Новый отклик',
            body='Hi!',
            from_email='EvgStud@yandex.ru',
            to=[instance.responseNotice.noticeAuthor.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    else:
        pass



@receiver(post_save, sender=User)
def reg_continue(sender, instance, created, **kwargs):
    if created:

        instance.is_active = False
        instance.save()
        reg_code = OneTimeCode.objects.create(code=random.randint(10000, 99999), user=instance)
        reg_code.save()

        html_content = render_to_string(
            'login/activation_email.html',
            {
                'reg_code': reg_code.code,
                'username': instance.username,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'Подтверждение регистрации',
            body='Hi!',
            from_email='EvgStud@yandex.ru',
            to=[instance.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        redirect('/login/signup_end.html')

    else:
        pass
