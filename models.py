from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)

    def __str__(self):
        return self.username