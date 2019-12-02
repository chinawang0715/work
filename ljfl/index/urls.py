from django.conf.urls import url

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/index/
    url(r'^$', views.index),
    # http://127.0.0.1:8000/index/news
    url(r'^news$', views.news)

]
