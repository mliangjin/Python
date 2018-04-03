from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=20)                  # 用户名
    pwd = models.CharField(max_length=128)                  # 密码
    email = models.CharField(max_length=30)                 # 邮箱
    phone = models.CharField(max_length=11, null=True)      # 手机
    shouName = models.CharField(max_length=20 ,null=True)   # 收货人
    detadd = models.CharField(max_length=100 ,null=True)    # 收货地址
    youbian = models.CharField(max_length=6 ,null=True)     # 收货邮编

