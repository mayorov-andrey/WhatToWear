# Generated by Django 2.2.7 on 2020-01-09 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200109_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 1, 9, 19, 17, 27, 360476), verbose_name='Опубликована'),
        ),
    ]
