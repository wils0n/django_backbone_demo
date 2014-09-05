from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    #url(r'^test/$', BaseTest.as_view(), name='base'),
    url(r'', include('app.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

from tastypie.api import Api
from app.api import EntryResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())

urlpatterns += patterns('',
    # The normal jazz here...
    url(r'^api/', include(v1_api.urls)),
)