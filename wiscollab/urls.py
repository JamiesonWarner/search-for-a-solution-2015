from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'core.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(\d+)$', 'core.views.project_details'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
