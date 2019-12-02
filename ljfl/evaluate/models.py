from django.db import models
from django.utils import timezone

# Create your models here.


class Evaluation(models.Model):
    order_id=models.IntegerField('订单id',unique=True,null=False)
    eval_score=models.IntegerField('评价分数',null=False)
    eval_content=models.TextField('评价内容')
    eval_date=models.DateTimeField('时间',auto_now_add=True)

    class Meta:
        db_table='evaluate'

class Order(models.Model):
    order_title = models.CharField('标题', max_length=20)
    order_name = models.CharField('发布人', max_length=50)
    order_tel = models.CharField('电话号码', max_length=11)
    order_address = models.CharField('地址', max_length=1000)
    type01 = ((1, '大'), (2, '中'), (3, '小'))
    rubbish_size = models.IntegerField('垃圾大小', choices=type01,null=True)
    order_appointment = models.DateTimeField('预约时间', default=timezone.now)

    order_money = models.DecimalField('悬赏金额', max_digits=6, decimal_places=2, default=0.0)
    order_creat_time = models.DateTimeField('创建时间', auto_now=True)
    type02 = ((1, '待接单'), (2, '已接单'), (3, '已完成'), (4, '已过期'))
    order_state = models.IntegerField('订单状态', choices=type02)

    class Meta:
        db_table = 'order_table'
