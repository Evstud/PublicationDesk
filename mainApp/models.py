from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField, CKEditorWidget, RichTextField

class Notice(models.Model):
    tanks = 'TA'
    heals = 'HE'
    DDs = 'DD'
    merchants = 'ME'
    guildmasters = 'GM'
    questgivers = 'QG'
    hammermans = 'HM'
    leathercrafters = 'LC'
    poisoncookers = 'PC'
    mantramasters = 'MM'

    CATEGORIES = [
        (tanks, 'Танки'),
        (heals, 'Хилы'),
        (DDs, 'ДД'),
        (merchants, 'Торговцы'),
        (guildmasters, 'Гилдмастеры'),
        (questgivers, 'Квестгиверы'),
        (hammermans, 'Кузнецы'),
        (leathercrafters, 'Кожевники'),
        (poisoncookers, 'Зельевары'),
        (mantramasters, 'Мастера заклинаний'),
    ]
    noticeTitle = models.CharField(max_length=255)
    noticeText = RichTextField(
        blank=True,
        null=True,
        config_name='default',
        external_plugin_resources=[(
            'youtube',
            'plugins/youtube/',
            'plugin.js',
        )],
    )
    noticeCategory = models.CharField(max_length=2, choices=CATEGORIES, default=tanks)
    noticeAuthor = models.OneToOneField(User, on_delete=models.CASCADE)
    # ck1 = RichTextField(blank=True, null=True)
    # ck2 = RichTextFormField()
    # ck3 = CKEditorWidget()


class Response(models.Model):
    responseText = models.TextField()
    responseAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    responseNotice = models.ForeignKey(Notice, on_delete=models.CASCADE)
