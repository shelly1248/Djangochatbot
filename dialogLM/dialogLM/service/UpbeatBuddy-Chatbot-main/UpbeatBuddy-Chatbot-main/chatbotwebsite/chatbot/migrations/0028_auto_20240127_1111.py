# Generated by Django 3.2.13 on 2024-01-27 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0027_auto_20240126_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='userscore',
            name='sentiment_scores',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='userscore',
            name='updatedAt',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 27, 11, 11, 26, 44757)),
        ),
    ]