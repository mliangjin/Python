from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

class GoodsInfo(models.Model):
    typeInfo = models.ForeignKey(TypeInfo)                      # 外键
    name = models.CharField(max_length=20)                      # 名字
    pic = models.ImageField(upload_to='df_goods')               # 图片
    price = models.DecimalField(max_digits=5,decimal_places=2)  # 价格
    unit = models.CharField(max_length=20)                      # 单位
    repertroy = models.IntegerField()                           # 库存
    click = models.IntegerField()                               # 点击量
    intro = models.CharField(max_length=200)                    # 简介
    context = HTMLField()                                       # 详情/富文本编辑器 
    isDelete = models.BooleanField(default=False)               # 逻辑删除
    # adv = models.BooleanField(default=False)                    # 广告
