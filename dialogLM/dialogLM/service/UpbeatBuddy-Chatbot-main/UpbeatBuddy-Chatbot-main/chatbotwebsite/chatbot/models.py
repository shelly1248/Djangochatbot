import imp
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class ChatbotUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True, null=True,)
    def __str__(self) -> str:
        return self.user.username+"__"+str(self.email)


class UserScore(models.Model):
    owner = models.ForeignKey(ChatbotUser, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    posCount = models.IntegerField(default=0)
    negCount = models.IntegerField(default=0)
    updatedAt = models.DateTimeField(auto_now=True, editable=True)
    sentiment_scores = models.JSONField(default=dict)
    date = models.DateField(auto_now=True)
    daily_sentiment_scores = models.JSONField(default=dict)
    
    def __str__(self) -> str:
        return self.owner.user.username+'__'+str(self.updatedAt)

class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)