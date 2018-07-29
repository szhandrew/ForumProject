from django.conf.urls import url
from . import views

app_name = 'news'
urlpatterns = [
    url('', views.show, name='show'),
    #url(r'^show/', views.show, name='show'),
]