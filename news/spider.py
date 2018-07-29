import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogproject.settings")
import django
django.setup()

import urllib.request, re
from urllib.request import Request, urlopen
import urllib.parse
from bs4 import BeautifulSoup


from news.models import Website


html_news = urllib.request.urlopen('http://news.mit.edu/topic/computers').read().decode("utf-8")
soup_news = BeautifulSoup(html_news, "html.parser")

title_List = soup_news.find('ul', 'view-news-items').find_all(class_=re.compile("title"))
link_List = soup_news.find('ul', 'view-news-items').find_all('a')
Date_List = soup_news.find('ul', 'view-news-items').find_all(class_="date")
Summ_List = soup_news.find('ul', 'view-news-items').find_all(class_="dek")

## add date at the end of title
title_with_Time = []

## fix the full URL
Full_Link = []
for i in range(0, len(link_List)):
    if(i%2 == 0):
        Full_Link.append("http://news.mit.edu" + link_List[i].get('href'))

for i in range(0, len(title_List)):
    title_with_Time.append(title_List[i].string + "----" + Date_List[i].string)


## save to DB
for i in range(0, len(title_with_Time)):
    Website.objects.get_or_create(name=title_with_Time[i], url=Full_Link[i], text=Summ_List[i].string)


# print (title_List[0].string)
# print (Full_Link[0])
# print (Date_List[0].string)
# print (Summ_List[0].string)
# print (title_with_Time[0])


# print (len(title_List))
# print (len(Full_Link))
# print (len(Date_List))
# print (len(Summ_List))