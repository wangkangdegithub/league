# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Premier',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('home', models.CharField(max_length=10)),
                ('away', models.CharField(max_length=10)),
            ],
        ),
    ]
