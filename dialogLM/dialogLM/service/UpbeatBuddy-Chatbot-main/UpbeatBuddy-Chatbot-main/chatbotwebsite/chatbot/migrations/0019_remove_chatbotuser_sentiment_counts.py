# Generated by Django 3.2.13 on 2024-01-26 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0018_chatbotuser_sentiment_counts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatbotuser',
            name='sentiment_counts',
        ),
    ]
