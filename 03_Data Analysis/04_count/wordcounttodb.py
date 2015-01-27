# -*- coding: utf-8 -*-
import mysql.connector
cnx = mysql.connector.connect(user='yb101', password='iii',
                              host='10.120.28.19',
                              database='db01',
                              charset='utf8',
                              use_unicode=True)
cursor = cnx.cursor(buffered=True)
cursor1 = cnx.cursor(buffered=True)
cursor2 = cnx.cursor(buffered=True)
cursor3 = cnx.cursor(buffered=True)
f1 = open('C:\\Users\\BigData\\100_project\\wordcount\\count_2.txt','r')
f2 = open('C:\\Users\\BigData\\100_project\\wordcount\\nodata.txt','w')
f3 = open('C:\\Users\\BigData\\100_project\\wordcount\\dupdata.txt','w')
frank=0
vrank=0

for line1 in f1.readlines():
    compare=1
    name=line1.split(' : ')[0].strip()
    num=line1.split(' : ')[1].strip()
    if num >=10:
        try:
            cursor.execute("SELECT foodid, foodname FROM foodinfo WHERE foodname=%s",(name,))
            for foodid, foodname in cursor:
                frank +=1
                compare -=1
                cursor1.execute ("""UPDATE foodinfo SET countnum=%s, rank=%s WHERE foodid=%s""", (num,frank,foodid))
                cnx.commit()
            if compare ==1:
                cursor2.execute("SELECT viewid, viewname FROM viewinfo WHERE viewname=%s",(name,))
                for viewid,viewname in cursor2:
                    vrank +=1
                    compare -=1
                    cursor3.execute("""UPDATE viewinfo SET countnum=%s, rank=%s WHERE viewid=%s""", (num,vrank,viewid))
                    cnx.commit()
            if compare ==1:
                f2.write(line1)
        except:
            f3.write(line1)
            pass
        
cursor1.close()
cursor2.close()
cursor3.close()
cursor.close()
cnx.close()
f3.close()
f2.close()
f1.close()