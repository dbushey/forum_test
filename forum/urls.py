from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.thread_list, name='thread_list'),
    url(r'^thread/(?P<pk>\d+)/$', views.thread_detail, name='thread_detail'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]

