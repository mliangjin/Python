from django.contrib import admin
from .models import *

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'pwd', 'email', 'shouName', 'phone', 'youbian']

admin.site.register(UserInfo, UserInfoAdmin)
