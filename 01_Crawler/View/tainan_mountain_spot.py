# -*- coding: utf-8 -*- 
import requests
import urlparse
from bs4 import BeautifulSoup,Comment
def remove_space(element):
	return  "".join(element.strip().split(" "))
file = open("tainan_mountain_spot.txt","w")
file.write("景點名稱|旅遊區域|旅遊主題|相關網址|地址|電話|美食資訊|住宿資訊|附近景點|建議停留|景點介紹"+"\n")
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
    comments = mountain_page_soup.findAll(text=lambda text:isinstance(text, Comment))
    [comment.extract() for comment in comments]
    mountain_name = remove_space(mountain_page_soup.find('span',{"id":"View1_SpotDetail1_lblName"}).text.encode('utf-8'))
    mountain_region = remove_space(mountain_page_soup.find('span',{"id":"View1_SpotDetail1_lblTownName"}).text.encode('utf-8'))

    mountain_type = remove_space(mountain_page_soup.find('span',{"id":"View1_SpotDetail1_lblSubjectName"}).text.encode('utf-8'))

    mountain_content = remove_space(mountain_page_soup.find('span',{"id":"View1_SpotDetail1_lblContent"}).text.encode('utf-8'))

    mountain_url_a = mountain_page_soup.find('a',{"id":"View1_SpotDetail1_aUrl"})
    if mountain_url_a is not None:
        mountain_url =remove_space( mountain_url_a['href'].encode('utf-8'))
    else:
        mountain_url="暫無提供"
        
    mountain_address_span=mountain_page_soup.find('span',{"id":"View1_SpotDetail1_lblAddress"})
    if mountain_address_span is not None:
        mountain_address = remove_space(mountain_address_span.text.encode('utf-8'))
    else:
        mountain_address = "暫無提供"
        
    mountain_phone_span=mountain_page_soup.find('span',{"id":"View1_SpotDetail1_lblTel"})
    if mountain_phone_span is not None:
        mountain_phone = remove_space(mountain_phone_span.text.encode('utf-8'))
    else:
        mountain_phone = "暫無提供"
      
    mountain_food_span=mountain_page_soup.find('span',{"id":"View1_SpotDetail1_dtlSpotToFineFood"})
    if mountain_food_span is not None:
        mountain_food=""
        mountain_food_spans = mountain_food_span.findAll('span',{'id':True})
        count=len(mountain_food_spans)
        for food_span in mountain_food_spans:
            count-=1
            mountain_food +=remove_space(food_span.text.encode('utf-8'))
            if count!=0:
                mountain_food +="/"
    else:
        mountain_food = "暫無提供"
        
        
    mountain_house_span=mountain_page_soup.find('span',{"id":"View1_SpotDetail1_dtlSpotToHospice"})
    if mountain_house_span is not None:
        mountain_house=""
        mountain_house_spans = mountain_house_span.findAll('span',{'id':True})
        count=len(mountain_house_spans)
        for house_span in mountain_house_spans:
            count-=1
            mountain_house +=remove_space(house_span.text.encode('utf-8'))
            if count!=0:
                mountain_house +="/"
    else:
        mountain_house = "暫無提供"

        
    mountain_spot_span=mountain_page_soup.find('span',{"id":"View1_SpotDetail1_dtlSpotToSpot"})
    if mountain_spot_span is not None:
        mountain_spot=""
        mountain_spot_as = mountain_spot_span.findAll('a',{'id':True})
        count=len(mountain_spot_as)
        for spot_a in mountain_spot_as:
            count-=1
            mountain_spot +=remove_space(spot_a.text.encode('utf-8'))
            if count!=0:
                mountain_spot +="/"
    else:
        mountain_spot = "暫無提供"
    mountain_proposal_span=mountain_page_soup.find('span',{"id":"View1_SpotDetail1_lblProposal"})
    if mountain_proposal_span is not None:
        mountain_proposal = remove_space(mountain_proposal_span.text.encode('utf-8'))
    else:
        mountain_proposal="暫無提供"
    
    file.write(mountain_name+"|"+mountain_region+"|"+mountain_type+"|"+mountain_url+"|")
    file.write(mountain_address+"|"+mountain_phone+"|"+mountain_food+"|"+mountain_house+"|"+mountain_spot+"|"+mountain_proposal+"|"+mountain_content+"\n")
file.close()