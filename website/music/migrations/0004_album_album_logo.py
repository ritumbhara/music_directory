# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-05-25 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_remove_album_album_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_logo',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
