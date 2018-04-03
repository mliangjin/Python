from django.shortcuts import render,redirect
from m_user.models import *
from m_goods.models import *
from .models import *


def index(request):
    # 通过session得到当前用户是谁
    user = UserInfo.objects.filter(name=request.session.get('user_name'))
    # 在购物车中找到当前用户所有的购物车数据
    cartinfo = CartInfo.objects.filter(user_id=user[0].id)
    print(cartinfo)
    context = {
        'cart': cartinfo
    }
    return render(request, 'm_cart/cart.html', context)

def add(request, goods, number):
    # 拿到用户和商品对应的表
    user = UserInfo.objects.filter(name=request.session.get('user_name'))
    # 拿到对应表中数据查找是否有对于的购物车
    cartinfo = CartInfo.objects.filter(goods_id=goods,user_id=user[0].id)
    # 1.判断购物车是否存在
    # 1.1 存在购物车,则继续判断购物车是否已经有商品数量
    # 1.2 不存在商品就直接添加新的商品数量
    # 1.3 否则商品数量等于现在的加原来的数量
    # 2.不存在购物车,则添加新的购物车数据
    if len(cartinfo) != 0:
        if cartinfo[0].number == 0:
            cartinfo.update(number=int(number))
        else:
            cartinfo.update(number=cartinfo[0].number + int(number))
    else:
        cart = CartInfo()
        cart.user_id = user[0].id
        cart.goods_id = goods
        cart.number = number
        cart.save()
    return redirect('/cart/')