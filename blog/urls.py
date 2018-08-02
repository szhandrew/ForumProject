from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^home', views.index, name='index'),
    url(r'^my-posts', views.my_posts, name='my_posts'),
    url(r'^add-post', views.add_post, name='add_post'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    url(r'^about', views.aboutUs, name='about'),
    url(r'^contact', views.contact, name='contact'),
    # url(r'^search/$', views.search, name='search'),
]
