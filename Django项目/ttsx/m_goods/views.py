from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


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
# 接收 类型id 排序页面1.2.3 分页
def lists(request, tid, orders, pagIndex):
    # 根据排序的值判断 默认 价格 人气 要取的数据
    # 默认 数据排序
    if orders == '1': 
        goods = GoodsInfo.objects.filter(typeinfo_id=tid).order_by('id')
    # 价格 数据排序
    elif orders == '2':
        goods = GoodsInfo.objects.filter(typeinfo_id=tid).order_by('-price')
    # 人气 数据排序
    elif orders == '3':
        goods = GoodsInfo.objects.filter(typeinfo_id=tid).order_by('-click')
    # 推荐的两条商品
    goodsDouble = GoodsInfo.objects.filter(typeinfo_id=tid).order_by('id')[:2]
    # 构造分页需要用的数据,遍历数据库,每页10条
    paginator = Paginator(goods, 10)
    # 构造每一页的数据
    goodsList = paginator.page(int(pagIndex))
    # 构造的迭代对象,是一个分页的个数数据
    pagIndexList = paginator.page_range
    # session用户的收藏的商品个数

    # 构造返回上下文
    context = {
        # 两条推荐商品
        'goodsDouble': goodsDouble,
        # 当前页面的类型
        'tid': tid,
        # 排序页面 1,2,3
        'order': orders,
        # 传入的分页第几页
        'pagIndex': int(pagIndex),
        # 构造的迭代对象,是一个分页的个数数据
        'pagIndexList': pagIndexList,
        # 每页分页数据
        'goodsList': goodsList,
    }
    return render(request, 'm_goods/list.html', context)
    

# 详情
def detail(request, id):
    id = GoodsInfo.objects.filter(id=id)
    goodsDouble = GoodsInfo.objects.all().order_by('-id')[:2]
    context = {
        "id":id[0],
        "goodsDouble": goodsDouble
    }
    return render(request, 'm_goods/detail.html', context)
