# -*- coding: utf-8 -*- 
import requests
import urlparse
from bs4 import BeautifulSoup

file = open("tainan_hotspring_name.txt","w")
file.write("景點名稱"+"\n")
tainan_hotspring_link = 'http://tour.tainan.gov.tw/view.aspx?subject=hotspring'
tainan_hotspring = requests.get(tainan_hotspring_link)
tainan_hotspring_text = tainan_hotspring.text.encode('utf-8')


tainan_hotspring_soup=BeautifulSoup(tainan_hotspring_text)
tainan_hotspring_table=tainan_hotspring_soup.find('table',{"id":"View1_SpotList1_dtlList"})
tainan_hotspring_spans = tainan_hotspring_table.findAll('span',{"id":"main-wrapper"})

for tainan_hotspring_span in tainan_hotspring_spans:
    hotspring_alink = tainan_hotspring_span.find('a',{"href":True})['href']
    hotspring_link=urlparse.urljoin(tainan_hotspring_link,hotspring_alink)
    hotspring_page=requests.get(hotspring_link)
    hotspring_page_text = hotspring_page.text.encode('utf-8')
    hotspring_page_soup=BeautifulSoup(hotspring_page_text)
    hotspring_name = hotspring_page_soup.find('span',{"id":"View1_SpotDetail1_lblName"}).text.encode('utf-8')
    file.write(hotspring_name.strip()+"\n")
file.close()