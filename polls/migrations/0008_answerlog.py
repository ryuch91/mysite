# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20150121_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField()),
                ('question', models.ForeignKey(to='polls.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
