from django.db import models


# Create your models here.
class News(models.Model):
    news_title = models.CharField('标题', max_length=128)
    news_content = models.TextField('内容')
    news_date = models.DateTimeField('发布时间', auto_now_add=True)
    news_source = models.CharField('新闻来源', max_length=32)

    class Meta:
        db_table = 'news'

    def __str__(self):
        return '%s %s %s %s %s' % (self.id, self.news_title, self.news_content, self.news_date, self.news_source)
