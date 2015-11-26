"""edgemark_dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
    url(r'^admin/', include(admin.site.urls)),
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from dashing.utils import router
from django.contrib.auth.decorators import login_required

from edgemark_dashboard.widget import *
from edgemark_dashboard.views import *

router.register(WorkToClientWidget, 'total_work_completed')

urlpatterns = patterns('',
    url(r'^$', main_page),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    #    url(r'^widgets/total_work_completed/?', login_required(WorkToClientWidget.as_view()), "widget_total_work_completed"),

    url(r'^dashboard/', include(router.urls)),

        # Serve static content.
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'})
)
