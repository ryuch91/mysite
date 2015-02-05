from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog import views
from polls import views
from homepage import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^blog/',  include('blog.urls', namespace="blog")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^homepage/', include('homepage.urls', namespace="homepage")),
)
