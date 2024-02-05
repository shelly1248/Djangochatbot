# Generated by Django 3.2.13 on 2024-01-26 20:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0026_chatbotuser_sentiment_counts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='chatbotuser',
            name='sentiment_counts',
        ),
        migrations.RemoveField(
            model_name='userscore',
            name='sentiment_counts',
        ),
        migrations.RemoveField(
            model_name='userscore',
            name='sentiment_scores',
        ),
        migrations.AlterField(
            model_name='chatbotuser',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userscore',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.chatbotuser'),
        ),
        migrations.AlterField(
            model_name='userscore',
            name='updatedAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
