# Generated by Django 5.1 on 2024-12-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prizes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='photo',
            field=models.ImageField(default=1, upload_to='static/image/'),
            preserve_default=False,
        ),
    ]