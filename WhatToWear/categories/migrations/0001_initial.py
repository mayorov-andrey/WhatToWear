# Generated by Django 2.2.7 on 2020-01-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, unique=True, verbose_name='Название')),
                ('order', models.PositiveSmallIntegerField(db_index=True, default=0, verbose_name='Порядковый номер')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['order', 'name'],
            },
        ),
    ]