# Generated by Django 3.1.6 on 2021-03-06 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boTtelegramm', '0002_auto_20210307_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Фото'),
        ),
    ]
