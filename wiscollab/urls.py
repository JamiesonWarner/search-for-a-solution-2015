from django.conf.urls import patterns, include, url
from django.contrib import admin
from core import views

urlpatterns = patterns('',
    url(r'^$', 'core.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(\d+)$', 'core.views.project_details'),
    url(r'^api/project', views.ProjectView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
