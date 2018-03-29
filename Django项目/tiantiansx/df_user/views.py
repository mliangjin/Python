from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from .models import *

def register(request):
    return render(request, 'df_user/register.html')

def register_dispose(request):
    name = request.POST.get('user_name')
    pwd = request.POST.get('pwd')
    pwd2 = request.POST.get('cpwd')
    email = request.POST.get('email')
    # 再判断一次密码
    if pwd != pwd2:
        return redirect('/user/register/')    
    
    # 密码加密
    pwd3 = make_password(pwd)
    print(pwd3)

    # 保存到数据库
    user = UserInfo()
    user.name = name
    user.pwd = pwd3
    user.email = email
    user.save()
    # 重定向到登陆页面
    return redirect('/user/login/')

def login(request):
    return render(request, 'df_user/login.html')

def register_exist(request):
    name = request.GET.get('name')
    count = UserInfo.object.filter(name=name).count()
    return JsonResponse({"count":count})

