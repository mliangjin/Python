from django.contrib import admin
from .models import *

class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'goods', 'number']

admin.site.register(CartInfo, CartInfoAdmin)
