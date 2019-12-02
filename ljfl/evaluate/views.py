from django.shortcuts import render

# Create your views here.
import json

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Evaluation, Order


# 发表评论
def pay_text(request):
    # 点击发表评论按钮,获取订单id数值

    if request.method == 'GET':
        # 获取订单数据, 在前端中显示订单信息(标题, 发布者, 接取者, 订单发布时间, 评价时间, 悬赏金额)

        order_info = Order.objects.values\
            ('order_title','order_name','order_appointment','order_money').filter(id=3)

        return render(request, 'evaluate/evaluate.html', locals())

    elif request.method == 'POST':

        # 获取前端输入的评价分数,评价内容
        eval_content = request.POST.get('txt_info')
        eval_score = request.POST.get('num')
        order_id = request.POST.get('order_id')


        # 限定输入的字数
        str = '最多输入1024个评价哦'
        if len(eval_content) > 36:
            print(eval_content)
            return render(request, 'evaluate/evaluate.html')

        ## 如果评分为1or2,扣除50%悬赏金
        # if eval_score == 1 or eval_score == 2:
        #     pass
        #
        # # 如果评分为3,扣除20%悬赏金,不扣除信誉分
        # elif eval_score == 3:
        #     pass
        #
        # ## 如果评分为4or5,不扣除赏金,增加50点信誉分
        # elif eval_score == 4 or eval_score == 5:
        #     pass

        # 增加接单者计算后的个人余额,扣除悬赏金额数值的个人余额

        # 将获取到的评价内容,分数,以及订单号,存入数据库中
        try:
            Evaluation.objects.create(order_id=order_id, eval_score=eval_score,
                                      eval_content=eval_content, )
        except Exception as e:
            print('--Sorry--')
            print(e)
            return HttpResponse('server error')
        return HttpResponse('发送成功')
