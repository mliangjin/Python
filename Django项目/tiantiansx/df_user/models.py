from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=128)
    email = models.CharField(max_length=20)
    shou = models.CharField(max_length=20, null=True)
    detaddr = models.CharField(max_length=100, null=True)
    youbian = models.CharField(max_length=6, null=True)
    phone = models.CharField(max_length=11, null=True)

