# Generated by Django 4.2.2 on 2023-07-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_alter_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='mjgallery', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
