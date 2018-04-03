from django.db import models

class CartInfo(models.Model):
    user = models.ForeignKey('m_user.UserInfo')
    goods = models.ForeignKey('m_goods.GoodsInfo')
    number = models.IntegerField(default=0)
