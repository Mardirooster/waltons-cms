# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='cms.CMSPlugin', auto_created=True, serialize=False)),
                ('poll', models.ForeignKey(to='polls.Poll')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
