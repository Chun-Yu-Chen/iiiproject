# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

count=0  #行數不變
a = open("author_2.txt", 'r')
lines = a.readlines()
l_line = lines[0:]  ##行數減一  ####可設定從第幾行開始讀  [2:]-->從第三行開始
for au in l_line:
    count += 1
    print count
    #print au  #要式utf8編碼存檔
    page_format = au.strip()
    author = au.strip()
    #print author  #作者
    #print page_format
    try:
        style_format_1 = "http://blog.yam.com/BlogIndex.php?BLOG_ID="
        style_format_2 = "&search=%E5%8F%B0%E5%8D%97"
        link_page = style_format_1+page_format+style_format_2  #只找該作者有關台南的網誌
        #print link_page
        if link_page is not None:
            res_page = requests.get(link_page)
            response_page = res_page.text.encode('utf8')
            soup_page = BeautifulSoup(response_page)
            #print soup_page    
            blog_link = soup_page.findAll('div', {'class':'post_titlediv'})  #要找連結
            for li in blog_link:
                link = [tag['href'] for tag in li.findAll('a', {'href':True})][0]  #連結
                #print link
                res_link = requests.get(link)
                response_link = res_link.text.encode('utf8')
                soup_link = BeautifulSoup(response_link)
                blog_title = soup_link.findAll('div', {'class':'post_titlediv'})  #要找標題
                blog_date = soup_link.findAll('div', {'class':'post_body'})  #要找日期
                blog_content = soup_link.findAll('div', {'class':'post_body'})  #要找內容
                for ti in blog_title:
                    title = ti.find('a').text.encode('utf8')  #標題
                    #print title
                for da in blog_date:
                    date_1 = da.find('div', {'class':'post_date'}).text.encode('utf8')
                    #print date_1
                    date_y = date_1.split(',')[1].strip()
                    #print date_y #年
                    if date_1.split(',')[0].split(' ')[1] == "":
                        date_d_1 = date_1.split(',')[0].split('  ')[1]
                        if int(date_d_1) < 10:
                            date_d = "0"+date_d_1
                        else:
                            date_d = date_d_1
                    else:
                        date_d = date_1.split(',')[0].split(' ')[1]
                        if int(date_d_1) < 10:
                            date_d = "0"+date_d_1
                        else:
                            date_d = date_d_1
                    #print date_d  #日
                    date_m_1 = date_1.split(' ')[0]
                    dic = {"January":"01", 
                           "February":"02", 
                           "March":"03", 
                           "April":"04", 
                           "May":"05", 
                           "June":"06", 
                           "July":"07", 
                           "August":"08", 
                           "September":"09", 
                           "October":"10", 
                           "November":"11", 
                           "December":"12"}
                    date_m = dic[date_m_1]
                    #print date_m  #月
                    date_2 = da.find('div', {'class':'post_time'}).text.encode('utf8').split('|')[0].strip().split("表於")[1]
                    #print date_2
                    date_h = date_2.split(':')[0]
                    #print date_h  #時
                    date_M = date_2.split(':')[1]
                    #print date_M  #分
                    date = date_y+"/"+date_m+"/"+date_d+" "+date_h+":"+date_M
                    #print date  #日期時間
                    id_date = date_y+date_m+date_d+date_h+date_M
                    #print id_date
                    id_name = "yam_"+author+"_"+id_date+".txt"
                    print id_name
                    f = open(id_name, 'w')
                    f.write(title+"\n")
                    f.write(date+"\n")
                    f.write(link+"\n")
                for co in blog_content:
                    content = co.find('div', {'class':'post_content'}).text.encode('utf8')
                    #print content
                    f.write(content+"\n")
    except:
        print "skip"
    
        
f.close()        
print "done"