from django.db import models

# Create your models here

class Manager(models.model):
    user_name = models.CharField(max_length=100,default='manager')
    password = models.CharField(max_length=100)
    email = models.EmailField(default='manager_email@email.com')