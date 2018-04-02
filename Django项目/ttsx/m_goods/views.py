from django.shortcuts import render
from .models import *

# 首页
def index(request):
    # 获取 正序的四个id数据 与 降序的四个order数据
    # goodsinfo表下面 id为typeinfo的数据
    shuiguo = GoodsInfo.objects.filter(typeinfo_id=1).order_by('id')[:4]
    shuiguo2 = GoodsInfo.objects.filter(typeinfo_id=1).order_by('-click')[:4]
    shuichan = GoodsInfo.objects.filter(typeinfo_id=2).order_by('id')[:4]
    shuichan2 = GoodsInfo.objects.filter(typeinfo_id=2).order_by('-click')[:4]
    tegong = GoodsInfo.objects.filter(typeinfo_id=3).order_by('id')[:4]
    tegong2 = GoodsInfo.objects.filter(typeinfo_id=3).order_by('-click')[:4]
    danpin = GoodsInfo.objects.filter(typeinfo_id=4).order_by('id')[:4]
    danpin2 = GoodsInfo.objects.filter(typeinfo_id=4).order_by('-click')[:4]
    sucai = GoodsInfo.objects.filter(typeinfo_id=5).order_by('id')[:4]
    sucai2 = GoodsInfo.objects.filter(typeinfo_id=5).order_by('-click')[:4]
    shipin = GoodsInfo.objects.filter(typeinfo_id=6).order_by('id')[:4]
    shipin2 = GoodsInfo.objects.filter(typeinfo_id=6).order_by('-click')[:4]
    context = {
        'shuiguo': shuiguo, 'shuiguo2': shuiguo2,
        'shuichan': shuichan, 'shuichan2': shuichan2,
        'tegong': tegong, 'tegong2': tegong2,
        'danpin': danpin, 'danpin2': danpin2,
        'sucai': sucai, 'sucai2': sucai2,
        'shipin': shipin, 'shipin2': shipin2,
    }
    return render(request, 'm_goods/index.html', context)

# 商品列表
def lists(request):
    return render(request, 'm_goods/list.html')

# 详情
def detail(request):
    return render(request, 'm_goods/detail.html')
