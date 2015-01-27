# -*- coding: utf-8 -*- 
import requests
import urlparse
from bs4 import BeautifulSoup
file = open("tainan_folkfestival_name.txt","w")
file.write("活動名稱"+"\n")
tainan_folkfestival_link='http://tour.tainan.gov.tw/action.aspx?Sys=FolkFestival'
tainan_folkfestival=requests.get(tainan_folkfestival_link)
tainan_folkfestival.encoding='utf-8'
tainan_folkfestival_text = tainan_folkfestival.text.encode('utf-8')
tainan_folkfestival_soup=BeautifulSoup(tainan_folkfestival_text)
tainan_folkfestival_table=tainan_folkfestival_soup.find('table',{'id':"Action1_FestivalList1_dtlList"})
tainan_folkfestival_spans=tainan_folkfestival_table.findAll('span',{'class':"03_title"})
for tainan_folkfestival_span in tainan_folkfestival_spans:
    tainan_folkfestival_alink=tainan_folkfestival_span.find('a')['href']
    tainan_folkfestival_page_link=urlparse.urljoin(tainan_folkfestival_link,tainan_folkfestival_alink)
    tainan_folkfestival_page=requests.get(tainan_folkfestival_page_link)
    tainan_folkfestival_page.encoding='utf-8'
    tainan_folkfestival_page_text = tainan_folkfestival_page.text.encode('utf-8')
    tainan_folkfestival_page_soup=BeautifulSoup(tainan_folkfestival_page_text)
    tainan_folkfestival_name_span=tainan_folkfestival_page_soup.find('span',{'id':"Action1_SpotDetail1_lblName"})
    tainan_folkfestival_name=tainan_folkfestival_name_span.text.encode('utf-8')
    file.write(tainan_folkfestival_name+"\n")
file.close()