from django.conf.urls import include, url
from django.contrib import admin
from portscanner import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'predictiveApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),

    url(r'^scan/(?P<id>\w+)', views.scan),
    url(r'^scans/', views.scans),
    url(r'^new/', views.new_scan),
    url(r'^rescan/(?P<id>\w+)', views.rescan),
]
