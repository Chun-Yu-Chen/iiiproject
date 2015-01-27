# -*- coding: utf-8 -*- 
import requests
import urlparse
from bs4 import BeautifulSoup
dic={ '1':'spring','2':'summer','3':'fall','4':'winter'}
file = open("tainan_activity_name.txt","w")
file.write("活動名稱"+"\n")
for season in sorted(dic.iterkeys()):
    tainan_activity_format='http://tour.tainan.gov.tw/action.aspx?season=%s'
    tainan_activity_link=tainan_activity_format%(dic[season])
    span_class="02_"+season+"title"
    tainan_activity=requests.get(tainan_activity_link)
    tainan_activity.encoding='utf-8'
    tainan_activity_text = tainan_activity.text.encode('utf-8')
    tainan_activity_soup=BeautifulSoup(tainan_activity_text)
    tainan_activity_table=tainan_activity_soup.find('table',{'id':"Action1_ActivityList1_dtlList"})
    tainan_activity_spans=tainan_activity_table.findAll('span',{'class':span_class})
    for tainan_activity_span in tainan_activity_spans:
        tainan_activity_alink=tainan_activity_span.find('a')['href']
        tainan_activity_page_link=urlparse.urljoin(tainan_activity_link,tainan_activity_alink)
        
        tainan_activity_page=requests.get(tainan_activity_page_link)
        tainan_activity_page.encoding='utf-8'
        tainan_activity_page_text = tainan_activity_page.text.encode('utf-8')
        tainan_activity_page_soup=BeautifulSoup(tainan_activity_page_text)
        tainan_activity_name_span=tainan_activity_page_soup.find('span',{'id':'Action1_ActivityDetail1_lblActivityName'})
        tainan_activity_name = tainan_activity_name_span.text.encode('utf-8').strip()
   
        file.write(tainan_activity_name+"\n")
        
file.close()