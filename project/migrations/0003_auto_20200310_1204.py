# Generated by Django 3.0.3 on 2020-03-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20200305_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='audio',
            field=models.FileField(blank='True', default='', null='True', upload_to=''),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='image',
            field=models.ImageField(default='', upload_to='', verbose_name='Изображение'),
        ),
    ]