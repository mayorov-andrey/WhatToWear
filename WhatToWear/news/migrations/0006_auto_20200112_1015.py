# Generated by Django 2.2.7 on 2020-01-12 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200111_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 1, 12, 10, 15, 17, 687811), verbose_name='Опубликована'),
        ),
    ]
