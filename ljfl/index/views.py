# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import *


def index(request):
    ljfl = ''
    if request.method == 'POST':
        lj = request.POST.get('lj')
        # objs = Rubbish_classification.objects.filter(rubbish_name__contains=lj)
        # for i in objs:
        #     ljfl+='%s %s\n'%(objs.rubbish_name,objs.rubbish_type)
        ljfl = '某某某是那种哪里,还需要查寻'
        print(ljfl)
        return render(request, 'index/index.html', locals())
    return render(request, 'index/index.html')


def news(request):
    # 数据库里面调数据,包括标题,图片路径,内容,点击量
    all = News.objects.order_by('news_date')[0:5]
    return render(request, 'index/news.html', locals())
