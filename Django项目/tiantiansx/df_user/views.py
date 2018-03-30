from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse, HttpResponseRedirect
from .models import *

# 注册
def register(request):
    return render(request, 'df_user/register.html')
# 注册数据到数据库
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
    
# 注册用户名验证
def register_exist(request):
    name = request.GET.get('name')
    count = UserInfo.objects.filter(name=name).count()
    return JsonResponse({"count":count})

# 登陆
def login(request):
    name = request.COOKIES.get('name','')
    print(name)
    print('name')
    context = {"name":name}
    return render(request, 'df_user/login.html', context)
# 登陆验证
def login_dispose(request):
    name = request.POST.get('username')
    pwd = request.POST.get('pwd')
    checkbox = request.POST.get('checkbox',0)
    # 数据里取出数据
    MysqlDate = UserInfo.objects.filter(name=name)
    # 数据库里有无数据防止拿数据的时候索引错误
    if len(MysqlDate) == 1:
        MysqlPwd = MysqlDate[0].pwd
        MysqlName = MysqlDate[0].name
        # django内置加密判断用户输入与数据里的密码是否一样
        pwdValue =  check_password(pwd,MysqlPwd)
        # 如果密码正确的逻辑判断
        if pwdValue == True and name == MysqlName:
            hrr = HttpResponseRedirect('/user/info/')
            # 设置cookie
            if checkbox != 0:
                print('cookie 测试')
                hrr.set_cookie('name',name)
            else:
                hrr.set_cookie('name','',max_age=-1)
            # 设置session
            request.session['name_id'] = MysqlDate[0].id
            request.session['name'] = name
            return hrr
        else:
            context = {'title': '用户登陆', 'error': '1', 'name':name}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登陆', 'error': '1', 'name':name}
        return render(request, 'df_user/login.html', context)
 
# 用户中心
def info(request):
    # 获取数据库数据
    MysqlDate = UserInfo.objects.filter(id=request.session.get('name_id'))
    # 判断是否数据库存在数据
    if len(MysqlDate) != 0:
        # 检查数据库中的收货地址与电话是否存在
        if MysqlDate[0].shou == None and MysqlDate[0].phone == None:
            context = {
                'name': MysqlDate[0].name,
                'site': '请在收货地址填写地址',
                'phone': '请在收获地址填写电话',
            }
            # 返回给模版的数据
            return render(request, 'df_user/user_center_info.html', context)
        else:
            context = {
                'name': MysqlDate[0].name,
                'site': MysqlDate[0].show,
                'phone': MysqlDate[0].phone,
            }
            # 返回给模版的数据
            return render(request, 'df_user/user_center_info.html', context)
    return render(request, 'df_user/user_center_info.html')

# 订单
def order(request):

    return render(request, 'df_user/user_center_order.html')

# 地址
def site(request):

    return render(request, 'df_user/user_center_site.html')

def site_dispose(request):
    # 获取到session对应的数据库数据
    MysqlDate = UserInfo.objects.filter(id=request.session.get('name_id'))
    print(MysqlDate[0].id)
    # 接收到POST请求的数据
    shou = request.POST.get('shou')
    detaddr = request.POST.get('detaddr')
    youbian = request.POST.get('youbian')
    phone = request.POST.get('phone')
    # 给对应的数据库字段更新数据
    MysqlDate.update(shou=shou)
    MysqlDate.update(detaddr=detaddr)
    MysqlDate.update(youbian=youbian)
    MysqlDate.update(phone=phone)
    # 返回context数据，便于显示给用户数据内容
    context = {
        'shou': shou,
        'detaddr': detaddr,
        'youbian': youbian,
        'phone': phone,
    }
    return render(request, 'df_user/user_center_site.html', context)


