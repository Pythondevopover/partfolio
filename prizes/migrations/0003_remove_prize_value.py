# Generated by Django 5.1 on 2024-12-28 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prizes', '0002_prize_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prize',
            name='value',
        ),
    ]