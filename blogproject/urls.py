"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse
from users import views
from blog.feeds import AllPostsRssFeed
from blog import views as blog_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chat/', include('chat.urls')),
    url(r'^profile/', blog_view.dajibaofans, name='dajibao'),
    url(r'', include('blog.urls', namespace='blog')),
    url(r'', include('comments.urls')),
    url(r'^robots\.txt$', lambda r: HttpResponse('User-agent: *\nDisallow: /', content_type='text/plain')),
    url(r'^search/', include('haystack.urls')),
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),


    url(r'^users/', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    # url(r'^$', views.index, name='index'),

    url(r'^$', views.index, name='index'),
    url(r'^logout/', blog_view.logout_view, name='logout'),

    url(r'^news/', include('news.urls')),
]
