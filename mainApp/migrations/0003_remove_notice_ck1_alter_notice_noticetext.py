# Generated by Django 4.1 on 2022-08-31 10:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_rename_responseuser_response_responseauthor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='ck1',
        ),
        migrations.AlterField(
            model_name='notice',
            name='noticeText',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
