from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.utils import timezone

urlpatterns = patterns('',
    url(r'^$','apolish.views.index',name='index'),
)