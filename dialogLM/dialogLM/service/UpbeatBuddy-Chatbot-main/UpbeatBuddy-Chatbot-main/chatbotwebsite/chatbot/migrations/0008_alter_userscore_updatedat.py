# Generated by Django 3.2.13 on 2024-01-15 21:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0007_auto_20220328_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userscore',
            name='updatedAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
