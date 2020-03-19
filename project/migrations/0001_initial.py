# Generated by Django 3.0.4 on 2020-03-18 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(default='', max_length=250)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('text', models.TextField()),
                ('video', embed_video.fields.EmbedVideoField(blank='True', null='True', verbose_name='video')),
                ('name_audio', models.CharField(blank='True', max_length=50, null='True')),
                ('audio', models.FileField(blank='True', default='', null='True', upload_to='files/')),
                ('image', models.ImageField(default='', upload_to='image/', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='NewsGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('image2', models.ImageField(upload_to='', verbose_name='Изображение1')),
                ('image3', models.ImageField(upload_to='', verbose_name='Изображение2')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date='publish')),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('private', 'Draft'), ('public', 'Published')], default='private', max_length=20)),
                ('video', embed_video.fields.EmbedVideoField(blank='True', null='True', verbose_name='video')),
                ('name_audio', models.CharField(blank='True', max_length=50, null='True')),
                ('audio', models.FileField(blank='True', default='', null='True', upload_to='files/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_materials', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'post',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth', models.DateTimeField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='user/')),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_like', models.ManyToManyField(related_name='user_likes', to='project.NewsGame')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('author_comment', models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='project.NewsGame')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
