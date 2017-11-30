#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.index, {'template_name': 'catalog/index.html'},
    #     'catalog_home'),
    url(r'^$', views.product_list,name = 'product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]