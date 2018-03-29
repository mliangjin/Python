from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse, HttpResponseRedirect
from .models import *

# 注册
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

# 注册验证
def register_exist(request):
    name = request.GET.get('name')
    count = UserInfo.objects.filter(name=name).count()
    return JsonResponse({"count":count})

# 登陆
def login(request):
    return render(request, 'df_user/login.html')
def login_dispose(request):
    name = request.POST.get('username')
    pwd = request.POST.get('pwd')
    checkbox = request.POST.get('checkbox',0)
    
    # 数据里取出数据
    MysqlDate = UserInfo.objects.filter(name=name)
    MysqlPwd = MysqlDate[0].pwd
    MysqlName = MysqlDate[0].name
    # django内置加密判断用户输入与数据里的密码是否一样
    pwdValue =  check_password(pwd,MysqlPwd)
    # 如果密码正确的逻辑判断
    if pwdValue == True and name == MysqlName:
        hrr = HttpResponseRedirect('/user/info/')
        # 设置cookie
        if checkbox == 1:
            hrr.set_cookie('name',name)
        else:
            hrr.set_cookie('name','',max_age=-1)
        request.session['name_id'] = MysqlDate[0].id
        request.session['name'] = name
        return hrr

    return 

# 登陆验证
def login_existCookie(request):
    nameCookie = request.COOKIE.get('name','')
    return JsonResponse({"nameCookie":nameCookie})

