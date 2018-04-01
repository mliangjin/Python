from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from django.http import JsonResponse, HttpResponseRedirect


# 注册
def register(request):
    return render(request, 'm_user/register.html')
def register_dispose(request):
    # 接收ajax GET请求
    if request.method == 'GET':
        # 如果直接dispose页面,那么user_name就是空对象,直接返回到注册页面
        if request.GET.get('name') == None:
            return redirect('/user/register/')
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

# 登陆
def login(request):    
    # 接收表单 post请求
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('pwd')
        remember = request.POST.get('remember')
        # 取出数据库对应name的数据
        user = UserInfo.objects.filter(name=name)
        # 判断是否存在数据
        if len(user) != 0:
            # 验证密码
            if check_password(pwd,user[0].pwd) == True:
                # 构造HTTPRESPONSE对象
                hrr = HttpResponseRedirect('/user/info/')
                # 记住用户名
                if remember == 1:
                    hrr.set_cookie('name', name)
                else:
                    hrr.set_cookie('name','',max_age=-1)
                # 保存session
                request.session['user_id'] = user[0].id
                request.session['user_name'] = name
                return hrr
            # 用户名存在 密码错误
            context = {'name':name}
            return render(request, 'm_user/login.html', context)
        else:
            # 用户名不存在
            context = {'name':name}
            return render(request, 'm_user/login.html', context)
    return render(request, 'm_user/login.html')

# 信息
def info(request):
    # 获取session对应的数据库字段
    user = UserInfo.objects.filter(id=request.session.get('user_id',''))
    # 判断是否存在数据
    if len(user) != 0:
        # 返回不同的上下文内容
        if user[0].phone == None:
            name = user[0].name
            context = {
                'name': name,
                'phone': '请在收获地址中添加',
            }
            return render(request, 'm_user/user_center_info.html', context)
        else:
            name = user[0].name
            phone = user[0].phone
            context = {
                'name': name,
                'phone': phone,
            }
            return render(request, 'm_user/user_center_info.html', context)
    # 直接请求网址没有session的情况下返回的地址
    return render(request, 'm_user/user_center_info.html')

# 订单
def order(request):
    return render(request, 'm_user/user_center_order.html')

# 地址
def site(request):
    # 获取更新字段 
    user = user = UserInfo.objects.filter(id=request.session.get('user_id',''))
    # 判断是否存在数据
    if len(user) != 0:
        # 接收表单 post请求
        if request.method == 'POST':
            shouName = request.POST.get('shouName')
            detadd = request.POST.get('detadd')
            youbian = request.POST.get('youbian')
            phone = request.POST.get('phone')
            user.update(shouName=shouName)
            user.update(detadd=detadd)
            user.update(youbian=youbian)
            user.update(phone=phone)
            # 构造返回给模版显示的数据
            context = {
                'shouName': shouName,
                'detadd': detadd,
                'youbian': youbian,
                'phone': phone,
            }
            return render(request, 'm_user/user_center_site.html', context)
        # 直接请求页面 get请求
        if request.method == 'GET':
            shouName = user[0].shouName
            detadd = user[0].detadd
            youbian = user[0].youbian
            phone = user[0].phone
            context = {
                'shouName': shouName,
                'detadd': detadd,
                'youbian': youbian,
                'phone': phone,
            }
            return render(request, 'm_user/user_center_site.html', context)
    # 意外的其他请求
    return render(request, 'm_user/user_center_site.html')
