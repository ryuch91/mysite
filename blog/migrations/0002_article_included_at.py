# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='included_at',
            field=models.ForeignKey(to='blog.Category', null=True),
            preserve_default=True,
        ),
    ]
