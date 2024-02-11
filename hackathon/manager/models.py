from django.db import models

# Create your models here

class Manager(models.Model):
    user_name = models.CharField(max_length=100,default='manager')
    password = models.CharField(max_length=100)
    email = models.EmailField(default='manager_email@email.com')
    def __str__(self) -> str:
        return self.user_name   