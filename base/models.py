from audioop import add
from email.policy import default
from typing import Text
from django.db import models
from django.contrib.auth.models import User
from django.forms import BooleanField, CharField, DateTimeField

class Task(models.Model):
    user = User.username
    title = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title

