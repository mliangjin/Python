from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.http import JsonResponse


# 注册
def register(request):
    return render(request, 'm_user/register.html')
def register_dispose(request):
    # 接收ajax GET请求
    if request.method == 'GET':
        # 返回在数据库中获取的数据个数,交给ajax回掉函数做继续判断
        count = UserInfo.objects.filter(name=request.GET.get('name')).count()
        return JsonResponse({'count': count})
    # 接收表单 POST请求
    if request.method == 'POST':
        name = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        # 密码加密
        pwd2 = make_password(pwd)
        # 存入数据库
        user = UserInfo()
        user.name = name
        user.pwd = pwd2
        user.email = email
        user.save()
        return render(request, 'm_user/login.html')
    return redirect('/user/register/')

# 登陆
def login(request):    
    return render(request, 'm_user/login.html')
