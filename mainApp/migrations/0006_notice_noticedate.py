# Generated by Django 4.1 on 2022-09-12 18:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_alter_onetimecode_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='noticeDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
