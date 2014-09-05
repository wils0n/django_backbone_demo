__author__ = 'wilson'

from django.conf.urls import patterns, include, url
from .views import BaseTest

urlpatterns = patterns('',
    
    url(r'^$', BaseTest.as_view(), name='base'),
    #url(r'^auth/logout/$', 'apps.perfil.views.logout_view', name='auth_logout'),
)