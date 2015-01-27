# -*- coding: utf-8 -*- 
import requests
import urlparse
from bs4 import BeautifulSoup

##設定remove space函式
def remove_space(element):
	return  "".join(element.strip().split(" "))


file = open("tainan_folkfestival.txt","w")
file.write("活動名稱|活動區域|活動類型|地址|電話|美食資訊|住宿資訊|附近景點|活動介紹"+"\n")
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
    tainan_folkfestival_name=remove_space(tainan_folkfestival_name_span.text.encode('utf-8'))
    tainan_folkfestival_region_span=tainan_folkfestival_page_soup.find('span',{"id":"Action1_SpotDetail1_lblTownName"})
    tainan_folkfestival_region = remove_space(tainan_folkfestival_region_span.text.encode('utf-8'))
    
    tainan_folkfestival_type_span=tainan_folkfestival_page_soup.find('span',{"id":"Action1_SpotDetail1_lblSubjectName"})
    tainan_folkfestival_type = remove_space(tainan_folkfestival_type_span.text.encode('utf-8'))
    
	
    tainan_folkfestival_content_span=tainan_folkfestival_page_soup.find('span',{"id":"Action1_SpotDetail1_lblContent"})
    tainan_folkfestival_content = remove_space(tainan_folkfestival_content_span.text.encode('utf-8'))
    
    tainan_folkfestival_address_span=tainan_folkfestival_page_soup.find('span',{"id":"Action1_SpotDetail1_lblAddress"})
    if tainan_folkfestival_address_span is not None:
        tainan_folkfestival_address = remove_space(tainan_folkfestival_address_span.text.encode('utf-8'))
    else:
        tainan_folkfestival_address="暫無提供"
    
    tainan_folkfestival_phone_span=tainan_folkfestival_page_soup.find('span',{"id":"Action1_SpotDetail1_lblTel"})
    if tainan_folkfestival_phone_span is not None:
        tainan_folkfestival_phone = remove_space(tainan_folkfestival_phone_span.text.encode('utf-8'))
    else:
        tainan_folkfestival_phone="暫無提供"
    
    tainan_folkfestival_food_span=tainan_folkfestival_page_soup.find('span',{"id":"Action1_SpotDetail1_dtlSpotToFineFood"})
    if tainan_folkfestival_food_span is not None:
        tainan_folkfestival_food_spans=tainan_folkfestival_food_span.findAll('span',{"id":True})
        count = len(tainan_folkfestival_food_spans)
        tainan_folkfestival_food=""
        for food_span in tainan_folkfestival_food_spans:
            count -=1
            tainan_folkfestival_food += remove_space(food_span.text.encode('utf-8'))
            if count!=0 :
                tainan_folkfestival_food+="/" 
    else:
        tainan_folkfestival_food="暫無提供"
    
    tainan_folkfestival_house_span=tainan_folkfestival_page_soup.find('span',{"id":"Action1_SpotDetail1_dtlSpotToHospice"})
    if tainan_folkfestival_house_span is not None:
        tainan_folkfestival_house_spans=tainan_folkfestival_house_span.findAll('span',{"id":True})
        count = len(tainan_folkfestival_house_spans)
        tainan_folkfestival_house=""
        for house_span in tainan_folkfestival_house_spans:
            count -=1
            tainan_folkfestival_house += remove_space(house_span.text.encode('utf-8'))
            if count!=0 :
                tainan_folkfestival_house+="/" 
    else:
        tainan_folkfestival_house="暫無提供"
    
    tainan_folkfestival_spot_span=tainan_folkfestival_page_soup.find('span',{"id":"Action1_SpotDetail1_dtlSpotToSpot"})
    if tainan_folkfestival_spot_span is not None:
        tainan_folkfestival_spot_a=tainan_folkfestival_spot_span.findAll('a',{"id":True})
        count = len(tainan_folkfestival_spot_a)
        tainan_folkfestival_spot=""
        for spot_a in tainan_folkfestival_spot_a:
            count -=1
            tainan_folkfestival_spot += remove_space(spot_a.text.encode('utf-8'))
            if count!=0 :
                tainan_folkfestival_spot+="/" 
    else:
        tainan_folkfestival_spot="暫無提供"
    
    file.write(tainan_folkfestival_name+"|"+tainan_folkfestival_region+"|"+tainan_folkfestival_type+"|")
    file.write(tainan_folkfestival_address+"|"+tainan_folkfestival_phone+"|")
    file.write(tainan_folkfestival_food+"|"+tainan_folkfestival_house+"|"+tainan_folkfestival_spot+"|"+tainan_folkfestival_content+"\n")
file.close()