from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^users/(?P<pk>[0-9]+)/$', views.user, name='user'),
#url(r'^user/new/(?P<pk>\d+)/$', views.user_new, name='user_new'),
]