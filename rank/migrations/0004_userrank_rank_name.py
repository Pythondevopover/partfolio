# Generated by Django 5.1 on 2024-12-28 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0003_userrank_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrank',
            name='rank_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
