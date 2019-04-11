# -*- coding: utf-8 -*-

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0010_auto_20180414_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
