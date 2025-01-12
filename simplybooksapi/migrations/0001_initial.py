# Generated by Django 4.1.3 on 2025-01-11 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=80)),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('image', models.CharField(max_length=100)),
                ('favorite', models.BooleanField(default=True)),
                ('uid', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('image', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
                ('sale', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=200)),
                ('uid', models.CharField(max_length=200)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simplybooksapi.author')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simplybooksapi.book')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simplybooksapi.genre')),
            ],
        ),
    ]