# Generated by Django 2.2.7 on 2020-01-20 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20200116_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodimage',
            options={'verbose_name': 'изображение к товару', 'verbose_name_plural': 'изображения к товару'},
        ),
        migrations.AlterField(
            model_name='goodimage',
            name='image',
            field=models.ImageField(upload_to='goods/detail', verbose_name='Дополнительное изображение'),
        ),
    ]