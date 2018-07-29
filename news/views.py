from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from .models import Website

def show(request):
# With QuerySet API to get all objects，return tuple
    queryset = Website.objects.all()
    # 传入三个渲染参数
    return render(request, 'news/nws.html', {'QuerySet': queryset})
    #return HttpResponse("Hello, world. You're at the polls index.")