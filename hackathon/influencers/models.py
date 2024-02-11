from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
# Create your models here





class User(AbstractUser, PermissionsMixin):
    """
    model user used for Managers and Influecers
    manager =  User.role = MANAGER
    influencer =  User.role = INFLUENDER

    """
    class RolesUser(models.TextChoices):
        # KEY_ACESSS / VALUE / Representation Value 
        MANAGER = "MANAGER",'Manager'
        INFLUENCER = "INFLUENCER",'Influencer'


    name = models.CharField("name", max_length=255)

    role = models.CharField('Permissão',max_length=255, choices=RolesUser.choices, default=RolesUser.INFLUENCER)
    created_at = models.DateTimeField("created_at", auto_now_add=True, blank=True)
    url = models.URLField("url")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self) -> str:
        return self.user_name
        


class Link(models.Model):
    link_name = models.CharField(max_length=255)
    influencer = models.ForeignKey(User, related_name="link_influencer", on_delete=models.CASCADE)
    created_at = models.DateTimeField("created_at", auto_now_add=True, blank=True)


class GroupInfo(models.Model):
    name = models.CharField(max_length=255)

class Groups(models.Model):
    group_info = models.ForeignKey(GroupInfo, on_delete=models.CASCADE)
    influencer = models.ForeignKey(User, related_name="influencer_groups", on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)



class Visitor(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    influencer = models.ForeignKey(User, on_delete=models.CASCADE)
    referer = models.CharField("referrer", max_length=255)
    location = models.CharField("referrer", max_length=255)
    headers = models.JSONField("headers")
    created_at = models.DateTimeField("created_at", auto_now_add=True, blank=True)

    

class ConsolidatedVisitors(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    influencer = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.IntegerField("day")
    month = models.IntegerField("month")
    year = models.IntegerField("year")
    data_json = models.JSONField("headers")







# # class Manager(models.Model):
# #     user_name = models.CharField(max_length=100,default='manager')
# #     password = models.CharField(max_length=100)
# #     email = models.EmailField(default='manager_email@email.com')
# #     def __str__(self) -> str:
# #         return self.user_name

