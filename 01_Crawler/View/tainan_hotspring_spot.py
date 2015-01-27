# -*- coding: utf-8 -*- 
import requests
import urlparse
from bs4 import BeautifulSoup,Comment
def remove_space(element):
	return  "".join(element.strip().split(" "))
file = open("tainan_hotspring_spot.txt","w")
file.write("景點名稱|旅遊區域|旅遊主題|相關網址|地址|電話|美食資訊|住宿資訊|附近景點|建議停留|景點介紹"+"\n")
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
    comments = hotspring_page_soup.findAll(text=lambda text:isinstance(text, Comment))
    [comment.extract() for comment in comments]
    hotspring_name = remove_space(hotspring_page_soup.find('span',{"id":"View1_SpotDetail1_lblName"}).text.encode('utf-8'))
    hotspring_region = remove_space(hotspring_page_soup.find('span',{"id":"View1_SpotDetail1_lblTownName"}).text.encode('utf-8'))

    hotspring_type = remove_space(hotspring_page_soup.find('span',{"id":"View1_SpotDetail1_lblSubjectName"}).text.encode('utf-8'))

    hotspring_content = remove_space(hotspring_page_soup.find('span',{"id":"View1_SpotDetail1_lblContent"}).text.encode('utf-8'))

    hotspring_url_a = hotspring_page_soup.find('a',{"id":"View1_SpotDetail1_aUrl"})
    if hotspring_url_a is not None:
        hotspring_url = remove_space(hotspring_url_a['href'].encode('utf-8'))
    else:
        hotspring_url="暫無提供"
        
    hotspring_address_span=hotspring_page_soup.find('span',{"id":"View1_SpotDetail1_lblAddress"})
    if hotspring_address_span is not None:
        hotspring_address = remove_space(hotspring_address_span.text.encode('utf-8'))
    else:
        hotspring_address = "暫無提供"
        
    hotspring_phone_span=hotspring_page_soup.find('span',{"id":"View1_SpotDetail1_lblTel"})
    if hotspring_phone_span is not None:
        hotspring_phone = remove_space(hotspring_phone_span.text.encode('utf-8'))
    else:
        hotspring_phone = "暫無提供"
      
    hotspring_food_span=hotspring_page_soup.find('span',{"id":"View1_SpotDetail1_dtlSpotToFineFood"})
    if hotspring_food_span is not None:
        hotspring_food=""
        hotspring_food_spans = hotspring_food_span.findAll('span',{'id':True})
        count=len(hotspring_food_spans)
        for food_span in hotspring_food_spans:
            count-=1
            hotspring_food +=remove_space(food_span.text.encode('utf-8'))
            if count!=0:
                hotspring_food +="/"
    else:
        hotspring_food = "暫無提供"
        
        
    hotspring_house_span=hotspring_page_soup.find('span',{"id":"View1_SpotDetail1_dtlSpotToHospice"})
    if hotspring_house_span is not None:
        hotspring_house=""
        hotspring_house_spans = hotspring_house_span.findAll('span',{'id':True})
        count=len(hotspring_house_spans)
        for house_span in hotspring_house_spans:
            count-=1
            hotspring_house +=remove_space(house_span.text.encode('utf-8'))
            if count!=0:
                hotspring_house +="/"
    else:
        hotspring_house = "暫無提供"

        
    hotspring_spot_span=hotspring_page_soup.find('span',{"id":"View1_SpotDetail1_dtlSpotToSpot"})
    if hotspring_spot_span is not None:
        hotspring_spot=""
        hotspring_spot_as = hotspring_spot_span.findAll('a',{'id':True})
        count=len(hotspring_spot_as)
        for spot_a in hotspring_spot_as:
            count-=1
            hotspring_spot +=remove_space(spot_a.text.encode('utf-8'))
            if count!=0:
                hotspring_spot +="/"
    else:
        hotspring_spot = "暫無提供"
    hotspring_proposal_span=hotspring_page_soup.find('span',{"id":"View1_SpotDetail1_lblProposal"})
    if hotspring_proposal_span is not None:
        hotspring_proposal = remove_space(hotspring_proposal_span.text.encode('utf-8'))
    else:
        hotspring_proposal="暫無提供"
    
    file.write(hotspring_name+"|"+hotspring_region+"|"+hotspring_type+"|"+hotspring_url+"|")
    file.write(hotspring_address+"|"+hotspring_phone+"|"+hotspring_food+"|"+hotspring_house+"|"+hotspring_spot+"|"+hotspring_proposal+"|"+hotspring_content+"\n")
file.close()