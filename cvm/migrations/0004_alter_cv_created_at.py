# Generated by Django 4.1.1 on 2022-09-23 19:33

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cvm', '0003_cv_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
