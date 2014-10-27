from django.conf.urls import patterns, include, url
from blog.views import blog_detail, blog_list

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', blog_list),
    url(r'^blog/(?P<pk>[0-9]+)/$', blog_detail),
)

