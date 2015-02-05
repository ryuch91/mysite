# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20150120_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(default=b'radio', max_length=30, choices=[(b'char', b'character'), (b'text', b'text'), (b'radio', b'radio button'), (b'check', b'check box'), (b'combo', b'combo box'), (b'email', b'e-mail'), (b'select', b'select')]),
            preserve_default=True,
        ),
    ]
