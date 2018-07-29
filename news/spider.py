#!/usr/bin/python
# -*- coding: utf-8 -*-
# import data into mysql(sqlite3), must have these four lines defination:
import os
# 我所创建的project名称为learn_spider;里面的app名称为website
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learn_spider.settings")
import django
django.setup()


# urllib2 package: open resource by URL; re package: use regular expression to filter the objects
import urllib.request, re
import urllib.parse
# BeautifulSoup: abstract data clearly from html/xml files
from bs4 import BeautifulSoup
# import tables from models.py
from news.models import Website

# urlopen()方法需要加read()才可视源代码，其中decode("utf-8")表示以utf-8编码解析原网页，这个编码格式是根据网页源代码中<head>标签下的<meta charset="utf-8">来决定的。
html_python = urllib.request.urlopen('https://baike.baidu.com/item/Python').read().decode("utf-8")
soup_python = BeautifulSoup(html_python, "html.parser")
# print soup
#这里用到了正则表达式进行筛选
item_list = soup_python.find_all('a', href=re.compile("item"))

for each in item_list:
    print (each.string)
    # use quote to replace special characters in string(escape encode method)
    urls = "https://baike.baidu.com/item/" + urllib.parse.quote(each.string.encode("utf-8"))
    print (urls)
    html = urllib.request.urlopen(urls).read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    if soup.find('div', 'lemma-summary') == None:
        text = "None"
    else:
        text = soup.find('div', 'lemma-summary').get_text()
    print (text)
    Website.objects.get_or_create(name=each.string, url=urls, text=text)


text_python = soup_python.find('div', 'lemma-summary').text

Website.objects.get_or_create(name="Python", url="https://baike.baidu.com/item/Python", text=text_python)