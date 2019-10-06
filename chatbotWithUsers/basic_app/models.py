from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ChatBotAdmin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #additional
    
    
    def __str__(self):
        return self.user.username

class QandAModel(models.Model):
    Questions=models.CharField(blank=False,max_length=1000)
    Answers=models.CharField(blank=True,max_length=5000)
    
    
    
    
