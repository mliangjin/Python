from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    name = models.CharField(max_length=20)                      # 种类名字
    isDelete = models.BooleanField(default=False)               # 逻辑删除
    def __str__(self):
        return self.name

class GoodsInfo(models.Model):
    name = models.CharField(max_length=20)                      # 商品名字
    pic = models.ImageField(upload_to='m_goodsPic')             # 图片路径
    price = models.DecimalField(max_digits=5, decimal_places=2) # 价格
    unit = models.CharField(max_length=20)                      # 单位
    click = models.IntegerField()                               # 点击量
    typeinfo = models.ForeignKey(TypeInfo)                      # 外键
    isDelete = models.BooleanField(default=False)               # 逻辑删除
    intor = models.CharField(max_length=200)                    # 简介
    kuchun = models.IntegerField()                              # 库存
    details = HTMLField()                                       # 详情
    def __str__(self):
        return self.name