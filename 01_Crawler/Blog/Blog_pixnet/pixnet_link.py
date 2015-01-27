# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

f = open("link.txt", 'a')
count = 517
style_format = "https://www.pixnet.net/searcharticle?q=%E5%8F%B0%E5%8D%97&type=related&period=all&"
page_format = "page=%d"
for page in range(518, 1000):
    count += 1
    print count
    res_page = requests.get(style_format+page_format%(page))
    res_page.encoding='utf-8'
    if res_page is not None:  #當有這個page時
        response_page = res_page.text#.encode('utf-8')
        soup_page = BeautifulSoup(response_page)
        blog_link = soup_page.findAll('li', {'class':'search-list'})  #要找每篇網誌的網址連結
        for li in blog_link:
            link = [tag['href'] for tag in li.findAll('a', {'href':True})][0]  #每篇網誌的網址連結
            #print link
            f.write(link+"\n")
            
print "done"
f.close()