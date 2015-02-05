# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150125_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='files',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
