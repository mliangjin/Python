from django.contrib import admin
from .models import *

class TypeInfoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'name', 'isDelete']    

class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['id', 'name' , 'pic', 'price', 'unit', 'click','typeinfo', 'intor', 'kuchun','isDelete']

admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)

