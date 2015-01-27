# -*- coding: utf-8 -*- 
import requests
import urlparse
from bs4 import BeautifulSoup

##設定remove space函式
def remove_space(element):
	return  "".join(element.strip().split(" "))
dic={ '1':'spring','2':'summer','3':'fall','4':'winter'}
file = open("tainan_activity.txt","w")
file.write("活動名稱|活動區域|活動類型|活動月份|活動介紹"+"\n")
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
    activityname = []
    continue_flag= 'n'
    for tainan_activity_span in tainan_activity_spans:
        tainan_activity_alink=tainan_activity_span.find('a')['href']
        tainan_activity_page_link=urlparse.urljoin(tainan_activity_link,tainan_activity_alink)
        
        tainan_activity_page=requests.get(tainan_activity_page_link)
        tainan_activity_page.encoding='utf-8'
        tainan_activity_page_text = tainan_activity_page.text.encode('utf-8')
        tainan_activity_page_soup=BeautifulSoup(tainan_activity_page_text)
        tainan_activity_name_span=tainan_activity_page_soup.find('span',{'id':'Action1_ActivityDetail1_lblActivityName'})
        tainan_activity_name = remove_space(tainan_activity_name_span.text.encode('utf-8'))

        tainan_activity_region_span = tainan_activity_page_soup.find('span',{"id":"Action1_ActivityDetail1_lblTownName"})
        tainan_activity_region = remove_space(tainan_activity_region_span.text.encode("utf-8"))

        tainan_activity_type_span = tainan_activity_page_soup.find('span',{"id":"Action1_ActivityDetail1_lblClassName"})
        tainan_activity_type=remove_space(tainan_activity_type_span.text.encode('utf-8'))
        tainan_activity_month_span=tainan_activity_page_soup.find('span',{"id":"Action1_ActivityDetail1_lblActivityMonth"})
        tainan_activity_month = remove_space(tainan_activity_month_span.text.encode('utf-8'))
        tainan_activity_content_span=tainan_activity_page_soup.find('span',{"id":"Action1_ActivityDetail1_lblActivityContent"})
        tainan_activity_content =remove_space(tainan_activity_content_span.text.encode('utf-8'))
        
        file.write(tainan_activity_name+"|"+tainan_activity_region+"|")
        if tainan_activity_type is not None:
            file.write(tainan_activity_type+"|")
        else: 
            file.write("暫無提供|")
        if tainan_activity_month is not None:
            file.write(tainan_activity_month+"|")
        else:
            file.write("暫無提供|")
        if tainan_activity_content is not None:
            file.write(tainan_activity_content)
        else:
            file.write("暫無提供")
            
        file.write("\n")
file.close()