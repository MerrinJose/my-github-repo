# Generated by Django 4.2.3 on 2023-07-04 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-01-22'),
            preserve_default=False,
        ),
    ]
