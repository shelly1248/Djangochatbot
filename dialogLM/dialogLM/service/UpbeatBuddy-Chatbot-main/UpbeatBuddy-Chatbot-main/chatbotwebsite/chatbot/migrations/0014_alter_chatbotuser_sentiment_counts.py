# Generated by Django 3.2.13 on 2024-01-25 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0013_alter_chatbotuser_sentiment_counts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbotuser',
            name='sentiment_counts',
            field=models.JSONField(default={'걱정스러운(불안한)': 0, '기쁨(행복한)': 0, '사랑하는': 0, '생각이 많은': 0, '설레는(기대하는)': 0, '슬픔(우울한)': 0, '일상적인': 0, '즐거운(신나는)': 0, '짜증남': 0, '힘듦(지침)': 0}),
        ),
    ]
