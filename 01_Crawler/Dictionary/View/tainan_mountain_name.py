# -*- coding: utf-8 -*- 
import requests
import urlparse
from bs4 import BeautifulSoup

file = open("tainan_mountain_name.txt","w")
file.write("景點名稱\n")
tainan_mountain_link = 'http://tour.tainan.gov.tw/view.aspx?subject=mountain'
tainan_mountain = requests.get(tainan_mountain_link)
tainan_mountain_text = tainan_mountain.text.encode('utf-8')


tainan_mountain_soup=BeautifulSoup(tainan_mountain_text)
tainan_mountain_table=tainan_mountain_soup.find('table',{"id":"View1_SpotList1_dtlList"})
tainan_mountain_spans = tainan_mountain_table.findAll('span',{"id":"main-wrapper"})

for tainan_mountain_span in tainan_mountain_spans:
    mountain_alink = tainan_mountain_span.find('a',{"href":True})['href']
    mountain_link=urlparse.urljoin(tainan_mountain_link,mountain_alink)
    mountain_page=requests.get(mountain_link)
    mountain_page_text = mountain_page.text.encode('utf-8')
    mountain_page_soup=BeautifulSoup(mountain_page_text)
    mountain_name = mountain_page_soup.find('span',{"id":"View1_SpotDetail1_lblName"}).text.encode('utf-8')
    file.write(mountain_name.strip()+"\n")
file.close()