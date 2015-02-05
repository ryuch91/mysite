# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150117_0028'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='Survey',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='request',
            new_name='survey',
        ),
    ]
