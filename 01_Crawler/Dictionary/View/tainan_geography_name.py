# -*- coding: utf-8 -*- 
import requests
import urlparse
from bs4 import BeautifulSoup

##取得頁數
file = open('tainan_geography_name.txt','w')
file.write("景點名稱"+"\n")
tainan_geography_link='http://tour.tainan.gov.tw/view.aspx?subject=geography'
tainan_geography = requests.get(tainan_geography_link) 
tainan_geography_text = tainan_geography.text.encode('utf-8')
tainan_geography_soup=BeautifulSoup(tainan_geography_text)
tainan_geography_page_number = tainan_geography_soup.find('span',{"id":"View1_SpotList1_lblPageCount"}).text.encode('utf-8')

##每頁取資料
for page in range(1,int(tainan_geography_page_number)+1):
    form_data_number='第'+str(page)+'頁'

    payload = { '__EVENTTARGET':'View1:SpotList1:ddlPageList'
      ,'__EVENTARGUMENT':''
      ,'__VIEWSTATE':'dDwtMTUzODMyOTkxNDt0PDtsPGk8MT47PjtsPHQ8O2w8aTwxPjtpPDM+Oz47bDx0PHA8cDxsPFN1YmplY3Q7RGlzcGxheTtTbjtOb2RlSUQ7PjtsPGdlb2dyYXBoeTs7Ozs+Pjs+O2w8aTwwPjtpPDE+O2k8Mj47aTw2PjtpPDc+Oz47bDx0PHA8cDxsPFNOO3NuO1N1Yk1lbnVJRDtwYXRoOz47bDxcZTs7MDtodHRwOz4+Oz47bDxpPDE+O2k8Mj47aTwzPjtpPDQ+O2k8NT47aTw2Pjs+O2w8dDxAMDxwPHA8bDxfIUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTw5PjtsPD47Pj47Pjs7Ozs7Ozs7PjtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PDtsPGk8MT47aTwzPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3ZpZXcuYXNweD9zdWJqZWN0PW1vdW50YWluO+eZu+WxseatpemBkzvnmbvlsbHmraXpgZM7Pj47Oz47dDxwPGw8VGV4dDs+O2w84pSCOz4+Ozs+Oz4+O3Q8O2w8aTwxPjtpPDM+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vdmlldy5hc3B4P3N1YmplY3Q9bmF0dXJlO+eUn+aFi+izh+a6kDvnlJ/mhYvos4fmupA7Pj47Oz47dDxwPGw8VGV4dDs+O2w84pSCOz4+Ozs+Oz4+O3Q8O2w8aTwxPjtpPDM+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vdmlldy5hc3B4P3N1YmplY3Q9Z2VvZ3JhcGh5O+iHqueEtuWcsOaZrzvoh6rnhLblnLDmma87Pj47Oz47dDxwPGw8VGV4dDs+O2w84pSCOz4+Ozs+Oz4+O3Q8O2w8aTwxPjtpPDM+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vdmlldy5hc3B4P3N1YmplY3Q9aG90c3ByaW5nO+a6q+azieW6puWBhzvmuqvms4nluqblgYc7Pj47Oz47dDxwPGw8VGV4dDs+O2w84pSCOz4+Ozs+Oz4+O3Q8O2w8aTwxPjtpPDM+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vdmlldy5hc3B4P3N1YmplY3Q9Y3VsdHVyZTvkurrmlofol53ooZM75Lq65paH6Jed6KGTOz4+Ozs+O3Q8cDxsPFRleHQ7PjtsPOKUgjs+Pjs7Pjs+Pjt0PDtsPGk8MT47aTwzPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3ZpZXcuYXNweD9zdWJqZWN0PXJlc29ydDvkvJHplpLovrLloLQ75LyR6ZaS6L6y5aC0Oz4+Ozs+O3Q8cDxsPFRleHQ7PjtsPOKUgjs+Pjs7Pjs+Pjt0PDtsPGk8MT47aTwzPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTt0YXJnZXQ7aW5uZXJodG1sOz47bDxodHRwOi8vdG91ci50YWluYW4uZ292LnR3L3RlbXBsZTvlrpfmlZnlkI3lu587X2JsYW5rO+Wul+aVmeWQjeW7nzs+Pjs7Pjt0PHA8bDxUZXh0Oz47bDzilII7Pj47Oz47Pj47dDw7bDxpPDE+O2k8Mz47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7dGFyZ2V0O2lubmVyaHRtbDs+O2w8aHR0cDovL3cyLWN1bHR1cmUudGFpbmFuLmdvdi50dy9jb21tdW5pdHkvO+WPsOWNl+aWh+WMlumkqDtfYmxhbms75Y+w5Y2X5paH5YyW6aSoOz4+Ozs+O3Q8cDxsPFRleHQ7PjtsPOKUgjs+Pjs7Pjs+Pjt0PDtsPGk8MT47aTwzPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3ZpZXcuYXNweD9ub2RlaWQ9MTI4MDA76KeA5YWJ5bel5bugO+ingOWFieW3peW7oDs+Pjs7Pjt0PHA8bDxUZXh0Oz47bDzilII7Pj47Oz47Pj47Pj47dDxAMDxwPHA8bDxfIUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxMD47bDw+Oz4+Oz47Ozs7Ozs7Oz47bDxpPDA+O2k8Mj47aTw0PjtpPDY+O2k8OD47aTwxMD47aTwxMj47aTwxND47aTwxNj47aTwxOD47PjtsPHQ8O2w8aTwxPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL2FjdGlvbi5hc3B4P25vZGVpZD0xMjg5MTvlj7DljZfnvo7po5/nr4A75Y+w5Y2X576O6aOf56+AOz4+Ozs+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL2FjdGlvbi5hc3B4P25vZGVpZD0xMjg1MTsyMDE05bm05Y+w5Y2X5paw5pil5rS75YuVOzIwMTTlubTlj7DljZfmlrDmmKXmtLvli5U7Pj47Oz47Pj47dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vYWN0aW9uLmFzcHg/bm9kZWlkPTEyNzUzO+W5tOW6pua0u+WLlee4veihqDvlubTluqbmtLvli5XnuL3ooag7Pj47Oz47Pj47dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vYWN0aW9uLmFzcHg/c2Vhc29uPXNwcmluZzvmmKXmmpboirHplos75pil5pqW6Iqx6ZaLOz4+Ozs+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL2FjdGlvbi5hc3B4P3NlYXNvbj1zdW1tZXI75aSP5pel6aKo5oOFO+Wkj+aXpemiqOaDhTs+Pjs7Pjs+Pjt0PDtsPGk8MT47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7aW5uZXJodG1sOz47bDwuLi9hY3Rpb24uYXNweD9zZWFzb249ZmFsbDvnp4vmpZPpo4TokYk756eL5qWT6aOE6JGJOz4+Ozs+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL2FjdGlvbi5hc3B4P3NlYXNvbj13aW50ZXI75Yas6Zm95pqW5pqWO+WGrOmZveaaluaaljs+Pjs7Pjs+Pjt0PDtsPGk8MT47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7aW5uZXJodG1sOz47bDwuLi9hY3Rpb24uYXNweD9TeXM9Rm9sa0Zlc3RpdmFsO+awkeS/l+evgOaFtjvmsJHkv5fnr4DmhbY7Pj47Oz47Pj47dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vYWN0aW9uLmFzcHg/U3lzPWN1bHR1cmVOZXc755Si5qWt5paH5YyW5rS75YuVO+eUoualreaWh+WMlua0u+WLlTs+Pjs7Pjs+Pjt0PDtsPGk8MT47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7dGFyZ2V0O2lubmVyaHRtbDs+O2w8aHR0cDovL3RvdXIudGFpbmFuLmdvdi50dy90ZW1wbGUvY2hpbmVzZS9kZWZhdWx0LmFzcHg75a6X5pWZ6KeA5YWJ57ay56uZO19ibGFuazvlrpfmlZnop4DlhYnntrLnq5k7Pj47Oz47Pj47Pj47dDxAMDxwPHA8bDxfIUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTw1PjtsPD47Pj47Pjs7Ozs7Ozs7PjtsPGk8MD47aTwyPjtpPDQ+O2k8Nj47aTw4Pjs+O2w8dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vcGxhbi5hc3B4P25vZGVpZD0xMjgyNjvlj7DljZfnsbPlhbbmnpfkuInmmJ/kuYvml4U75Y+w5Y2X57Gz5YW25p6X5LiJ5pif5LmL5peFOz4+Ozs+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3BsYW4uYXNweDvmjqjolqbooYznqIs75o6o6Jam6KGM56iLOz4+Ozs+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3BsYW4uYXNweD9ub2RlaWQ9MTI4MTU754Sh6Zqc56SZ5peF6YGK5bCI5Y2AO+eEoemanOekmeaXhemBiuWwiOWNgDs+Pjs7Pjs+Pjt0PDtsPGk8MT47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7aW5uZXJodG1sOz47bDwuLi9wbGFuLmFzcHg/bm9kZWlkPTEyODE2O+WPsOWNl+W5uee3muWFrOi7iuaXhemBiuihjOeoi+WwiOWNgDvlj7DljZflubnnt5rlhazou4rml4XpgYrooYznqIvlsIjljYA7Pj47Oz47Pj47dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vcGxhbi5hc3B4P25vZGVpZD0xMjgyNDvlj7DngaPljYHlpKflubjnpo/lpb3njqnpgYrnqIs75Y+w54Gj5Y2B5aSn5bm456aP5aW9546p6YGK56iLOz4+Ozs+Oz4+Oz4+O3Q8QDA8cDxwPGw8XyFJdGVtQ291bnQ7RGF0YUtleXM7PjtsPGk8MTE+O2w8Pjs+Pjs+Ozs7Ozs7Ozs+O2w8aTwwPjtpPDI+O2k8ND47aTw2PjtpPDg+O2k8MTA+O2k8MTI+O2k8MTQ+O2k8MTY+O2k8MTg+O2k8MjA+Oz47bDx0PDtsPGk8MT47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7aW5uZXJodG1sOz47bDwuLi90cmF2ZWwuYXNweD9zeXM9aG9zcGljZTvkvY/lrr/os4foqIo75L2P5a6/6LOH6KiKOz4+Ozs+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3RyYXZlbC5hc3B4P3N5cz1maW5lZm9vZDvntpPlhbjnvo7po5/lj4rkvLTmiYvnpq4757aT5YW4576O6aOf5Y+K5Ly05omL56auOz4+Ozs+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3RyYXZlbC5hc3B4P25vZGVpZD0xMjI3MTvkuqTpgJros4foqIo75Lqk6YCa6LOH6KiKOz4+Ozs+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3RyYXZlbC5hc3B4P25vZGVpZD0xMjc3Mjvml4XpgYrmnI3li5nkuK3lv4Pmk5rpu5475peF6YGK5pyN5YuZ5Lit5b+D5pOa6bueOz4+Ozs+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3RyYXZlbC5hc3B4P25vZGVpZD0xMjc0Njvop4DlhYnoqIjnqIvou4rlsIjljYA76KeA5YWJ6KiI56iL6LuK5bCI5Y2AOz4+Ozs+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3RyYXZlbC5hc3B4P3N5cz1saW5rO+aXhemBiuizh+ioiuebuOmXnOmAo+e1kDvml4XpgYros4foqIrnm7jpl5zpgKPntZA7Pj47Oz47Pj47dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO3RhcmdldDtpbm5lcmh0bWw7PjtsPGh0dHA6Ly9jaXR5YnVzLnRhaW5hbi5nb3YudHcvemgvbmV3cy8xLmh0bWw75bm557ea5YWs6LuKO19ibGFuazvlubnnt5rlhazou4o7Pj47Oz47Pj47dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vdHJhdmVsLmFzcHg/bm9kZWlkPTEyODIwO+WQiOazleingOWFiemBiuaogualrTvlkIjms5Xop4DlhYnpgYrmqILmpa07Pj47Oz47Pj47dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vdHJhdmVsLmFzcHg/bm9kZWlkPTEyODI4O+iHuueBo+WcmOmkkOWkp+i7iuaLvDvoh7rngaPlnJjppJDlpKfou4rmi7w7Pj47Oz47Pj47dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vdHJhdmVsLmFzcHg/bm9kZWlkPTEyODI5O+WsiemBiuWPsOWNlyDlt7Tlo6vlpb3nq5k75ayJ6YGK5Y+w5Y2XIOW3tOWjq+WlveermTs+Pjs7Pjs+Pjt0PDtsPGk8MT47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7aW5uZXJodG1sOz47bDwuLi90cmF2ZWwuYXNweD9ub2RlaWQ9MTI4NTQ76IWz6LiP6LuK56ef6LODO+iFs+i4j+i7iuenn+izgzs+Pjs7Pjs+Pjs+Pjt0PEAwPHA8cDxsPF8hSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDQ+O2w8Pjs+Pjs+Ozs7Ozs7Ozs+O2w8aTwwPjtpPDI+O2k8ND47aTw2Pjs+O2w8dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vZmVzdGl2YWwuYXNweD9ub2RlaWQ9MTI4MTQ75Y+w5Y2X5YuV6KeA5YWJ5bCI5Y2AO+WPsOWNl+WLleingOWFieWwiOWNgDs+Pjs7Pjs+Pjt0PDtsPGk8MT47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7aW5uZXJodG1sOz47bDwuLi9mZXN0aXZhbC5hc3B4P25vZGVpZD0xMjI3MDvpm7vlrZBETTvpm7vlrZBETTs+Pjs7Pjs+Pjt0PDtsPGk8MT47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7dGFyZ2V0O2lubmVyaHRtbDs+O2w8aHR0cDovL3ZyLm1pcy5mZXUuZWR1LnR3L3RhaW5hbnZyLzvoh7rljZfmma/pu543MjDluqZWUjtfYmxhbms76Ie65Y2X5pmv6bueNzIw5bqmVlI7Pj47Oz47Pj47dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vZmVzdGl2YWwuYXNweD9ub2RlaWQ9MTI4MjU755m+5bm05Y+k6YO96IiH5Y+w54Gj6KeA5YWJO+eZvuW5tOWPpOmDveiIh+WPsOeBo+ingOWFiTs+Pjs7Pjs+Pjs+Pjt0PEAwPHA8cDxsPF8hSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDk+O2w8Pjs+Pjs+Ozs7Ozs7Ozs+O2w8aTwwPjtpPDI+O2k8ND47aTw2PjtpPDg+O2k8MTA+O2k8MTI+O2k8MTQ+O2k8MTY+Oz47bDx0PDtsPGk8MT47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7aW5uZXJodG1sOz47bDwuLi9jdWx0dXJlLmFzcHg/bm9kZWlkPTEyNzYxO+WFrOmWi+izh+ioiuWwiOWNgDvlhazplovos4foqIrlsIjljYA7Pj47Oz47Pj47dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vY3VsdHVyZS5hc3B4P25vZGVpZD0xMjgxMjvlhazli5nntbHoqIjlsIjljYA75YWs5YuZ57Wx6KiI5bCI5Y2AOz4+Ozs+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL2N1bHR1cmUuYXNweD9ub2RlaWQ9MTI4MTM76KeA5YWJ5oqV6LOH5bCI5Y2AO+ingOWFieaKleizh+WwiOWNgDs+Pjs7Pjs+Pjt0PDtsPGk8MT47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7aW5uZXJodG1sOz47bDwuLi9jdWx0dXJlLmFzcHg/bm9kZWlkPTEyNzUyO+eUs+iri+aOiOasijvnlLPoq4vmjojmrIo7Pj47Oz47Pj47dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO3RhcmdldDtpbm5lcmh0bWw7PjtsPGh0dHA6Ly93d3cudGFpbmFuLmdvdi50dy90YWluYW4vZGVwYXJ0bWVudC5hc3A/bnN1Yj1CMDAwMDA76KGM5pS/6LOH6KiKO19ibGFuazvooYzmlL/os4foqIo7Pj47Oz47Pj47dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vY3VsdHVyZS5hc3B4P25vZGVpZD0xMjgwMTvpgYroqqrms5Xos4foqIrlsIjljYA76YGK6Kqq5rOV6LOH6KiK5bCI5Y2AOz4+Ozs+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL2N1bHR1cmUuYXNweD9ub2RlaWQ9MTI4MDg75rC05Z+f6YGK5oap5rS75YuV5bCI5Y2AO+awtOWfn+mBiuaGqea0u+WLleWwiOWNgDs+Pjs7Pjs+Pjt0PDtsPGk8MT47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7aW5uZXJodG1sOz47bDwuLi9jdWx0dXJlLmFzcHg/bm9kZWlkPTEyODE3O+WPsOWNl+WVj+i3r+W6lzvlj7DljZfllY/ot6/lupc7Pj47Oz47Pj47dDw7bDxpPDE+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vY3VsdHVyZS5hc3B4P25vZGVpZD0xMjgyMTvpoqjmma/ljYDpmLLngb3pgb/pm6Pot6/nt5rlsIjljYA76aKo5pmv5Y2A6Ziy54G96YG/6Zuj6Lev57ea5bCI5Y2AOz4+Ozs+Oz4+Oz4+Oz4+O3Q8cDxwPGw8TWVudTtTdWJNZW51SUQ7cGF0aDs+O2w8dmlldzswO3ZpZXc7Pj47PjtsPGk8MD47aTwxPjtpPDU+O2k8Nj47aTw3PjtpPDg+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPOaZr+m7nuS7i+e0uTs+Pjs+Ozs+O3Q8QDA8cDxwPGw8RGF0YUtleXM7XyFJdGVtQ291bnQ7PjtsPGw8PjtpPDEzPjs+Pjs+Ozs7Ozs7Ozs+O2w8aTwxPjtpPDM+O2k8NT47aTw3PjtpPDk+O2k8MTE+O2k8MTM+O2k8MTU+O2k8MTc+O2k8MTk+O2k8MjE+O2k8MjM+O2k8MjU+Oz47bDx0PDtsPGk8MD47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7aW5uZXJodG1sOz47bDwuLi92aWV3LmFzcHg/c3ViamVjdD1tb3VudGFpbjvnmbvlsbHmraXpgZM755m75bGx5q2l6YGTOz4+Ozs+Oz4+O3Q8O2w8aTwwPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3ZpZXcuYXNweD9zdWJqZWN0PW5hdHVyZTvnlJ/mhYvos4fmupA755Sf5oWL6LOH5rqQOz4+Ozs+Oz4+O3Q8O2w8aTwwPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3ZpZXcuYXNweD9zdWJqZWN0PWdlb2dyYXBoeTvoh6rnhLblnLDmma876Ieq54S25Zyw5pmvOz4+Ozs+Oz4+O3Q8O2w8aTwwPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3ZpZXcuYXNweD9zdWJqZWN0PWhvdHNwcmluZzvmuqvms4nluqblgYc75rqr5rOJ5bqm5YGHOz4+Ozs+Oz4+O3Q8O2w8aTwwPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3ZpZXcuYXNweD9zdWJqZWN0PWN1bHR1cmU75Lq65paH6Jed6KGTO+S6uuaWh+iXneihkzs+Pjs7Pjs+Pjt0PDtsPGk8MD47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7aW5uZXJodG1sOz47bDwuLi92aWV3LmFzcHg/c3ViamVjdD1yZXNvcnQ75LyR6ZaS6L6y5aC0O+S8kemWkui+suWgtDs+Pjs7Pjs+Pjt0PDtsPGk8MD47PjtsPHQ8cDxsPGhyZWY7dGFyZ2V0O3RpdGxlO2lubmVyaHRtbDs+O2w8aHR0cDovL3RvdXIudGFpbmFuLmdvdi50dy90ZW1wbGU7X2JsYW5rO+Wul+aVmeWQjeW7nzvlrpfmlZnlkI3lu587Pj47Oz47Pj47dDw7bDxpPDA+Oz47bDx0PHA8bDxocmVmO3RhcmdldDt0aXRsZTtpbm5lcmh0bWw7PjtsPGh0dHA6Ly93Mi1jdWx0dXJlLnRhaW5hbi5nb3YudHcvY29tbXVuaXR5LztfYmxhbms75Y+w5Y2X5paH5YyW6aSoO+WPsOWNl+aWh+WMlumkqDs+Pjs7Pjs+Pjt0PDtsPGk8MD47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7aW5uZXJodG1sOz47bDwuLi92aWV3LmFzcHg/bm9kZWlkPTEyODAwO+ingOWFieW3peW7oDvop4DlhYnlt6Xlu6A7Pj47Oz47Pj47dDw7bDxpPDA+Oz47bDx0PHA8bDxocmVmO3RpdGxlO2lubmVyaHRtbDs+O2w8Li4vVGFpamlhbmcuYXNweDvlj7DmsZ/lnIvlrrblhazlnJI75Y+w5rGf5ZyL5a625YWs5ZySOz4+Ozs+Oz4+O3Q8O2w8aTwwPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3ZpZXcuYXNweDvmma/pu57mkJzlsIs75pmv6bue5pCc5bCLOz4+Ozs+Oz4+O3Q8O2w8aTwwPjs+O2w8dDxwPGw8aHJlZjt0aXRsZTtpbm5lcmh0bWw7PjtsPC4uL3ZpZXcuYXNweD9zdWJqZWN0PXNpcmF5YS1uc2E76KW/5ouJ6ZuF5ZyL5a626aKo5pmv5Y2AO+ilv+aLiembheWci+WutumiqOaZr+WNgDs+Pjs7Pjs+Pjt0PDtsPGk8MD47PjtsPHQ8cDxsPGhyZWY7dGl0bGU7aW5uZXJodG1sOz47bDwuLi92aWV3LmFzcHg/bm9kZWlkPTEyMjU5O+mbsuWYieWNl+a/sea1t+Wci+WutumiqOaZr+WNgDvpm7LlmInljZfmv7HmtbflnIvlrrbpoqjmma/ljYA7Pj47Oz47Pj47Pj47dDxwPHA8bDxTeXM7PjtsPDs+Pjs+O2w8aTwwPjs+O2w8dDxwPGw8c3JjOz47bDwvVXNlckNvbnRyb2xzLy4uL2ltYWdlcy9idXR0XzEuanBnOz4+Ozs+Oz4+O3Q8cDxwPGw8U3lzOz47bDw7Pj47PjtsPGk8MD47PjtsPHQ8cDxsPHNyYzs+O2w8L1VzZXJDb250cm9scy8uLi9pbWFnZXMvYnV0dF8zLmpwZzs+Pjs7Pjs+Pjt0PHA8cDxsPFN5czs+O2w8Oz4+Oz47bDxpPDA+Oz47bDx0PHA8bDxzcmM7PjtsPC9Vc2VyQ29udHJvbHMvLi4vaW1hZ2VzL2J1dHRfNS5qcGc7Pj47Oz47Pj47dDxwPHA8bDxTeXM7PjtsPDs+Pjs+O2w8aTwwPjs+O2w8dDxwPGw8c3JjOz47bDwvVXNlckNvbnRyb2xzLy4uL2ltYWdlcy9idXR0XzcuanBnOz4+Ozs+Oz4+Oz4+O3Q8cDxwPGw8TWVudTtTeXM7RGlzcGxheTtTdWJqZWN0O1NlYXNvbjtTbjtGU3lzO0NzeXM7PjtsPHZpZXc7U3BvdDs7Z2VvZ3JhcGh5Ozs7Ozs+Pjs+O2w8aTwxPjs+O2w8dDxAMDxwPHA8bDxEYXRhS2V5cztfIUl0ZW1Db3VudDs+O2w8bDw+O2k8Mj47Pj47Pjs7Ozs7Ozs7PjtsPGk8MT47aTwzPjs+O2w8dDw7bDxpPDE+Oz47bDx0PHA8bDxjbGFzczs+O2w8aG9tZTs+PjtsPGk8MD47PjtsPHQ8cDxsPGhyZWY7aW5uZXJodG1sOz47bDwuLi92aWV3LmFzcHg75pmv6bue5LuL57S5Oz4+Ozs+Oz4+Oz4+O3Q8O2w8aTwxPjs+O2w8dDxwPGw8Y2xhc3M7PjtsPFxlOz4+O2w8aTwwPjs+O2w8dDxwPGw8aHJlZjtpbm5lcmh0bWw7PjtsPDvoh6rnhLblnLDmma87Pj47Oz47Pj47Pj47Pj47Pj47dDxwPHA8bDxWaXNpYmxlO0N1cnJlbnRQYWdlSW5kZXg7UGFnZUNvdW50O1N5cztUb3duU047U3BvdE5hbWU7U247U3ViamVjdDtEaXNwbGF5Oz47bDxvPHQ+O2k8Mj47aTwzPjtzcG90O2k8MD47OztnZW9ncmFwaHk7Oz4+Oz47bDxpPDA+O2k8MT47aTwyPjtpPDQ+O2k8Nj47aTw3PjtpPDg+O2k8OT47PjtsPHQ8cDxsPHNyYzthbHQ7PjtsPC4uL2ltYWdlcy8wMV80X3RpdGxlLmdpZjvoh6rnhLblnLDmma87Pj47Oz47dDw7bDxpPDE+O2k8Mz47aTw1Pjs+O2w8dDw7bDxpPDA+Oz47bDx0PHQ8cDxwPGw8RGF0YVRleHRGaWVsZDtEYXRhVmFsdWVGaWVsZDs+O2w8U3ViamVjdE5hbWU7U3ViamVjdEVuZ05hbWU7Pj47Pjt0PGk8MTE+O0A85LiN5ouYO+mbsuWYieWNl+a/sea1t+Wci+WutumiqOaZr+WNgDvopb/mi4npm4XlnIvlrrbpoqjmma/ljYA75Lq65paH6Jed6KGTO+eUn+aFi+izh+a6kDvmuqvms4nluqblgYc75rCR5L+X56+A5oW2O+e+jumjn+WQjeeUojvkvJHplpLovrLloLQ76Ieq54S25Zyw5pmvO+eZu+WxseatpemBkzs+O0A8XGU7c3djb2FzdC1uc2E7c2lyYXlhLW5zYTtjdWx0dXJlO25hdHVyZTtob3RzcHJpbmc7ZmVzdGl2aXR5O2ZpbmVmb29kO3Jlc29ydDtnZW9ncmFwaHk7bW91bnRhaW47Pj47Pjs7Pjs+Pjt0PDtsPGk8MT47PjtsPHQ8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDxUb3duTmFtZTtTTjs+Pjs+O3Q8aTwzOT47QDzoq4vpgbjmk4flnLDpu5475LiN5ouYO+S4reilv+WNgDvmnbHljYA75Y2X5Y2AO+WMl+WNgDvlronlubPljYA75a6J5Y2X5Y2AO+awuOW6t+WNgDvmrbjku4HljYA75paw5YyW5Y2AO+W3pumOruWNgDvnjonkupXljYA75qWg6KW/5Y2AO+WNl+WMluWNgDvku4HlvrfljYA76Zec5buf5Y2AO+m+jeW0juWNgDvlrpjnlLDljYA76bq76LGG5Y2AO+S9s+mHjOWNgDvopb/muK/ljYA75LiD6IKh5Y2AO+Wwh+i7jeWNgDvlrbjnlLLljYA75YyX6ZaA5Y2AO+aWsOeHn+WNgDvlvozlo4HljYA755m95rKz5Y2AO+adseWxseWNgDvlha3nlLLljYA75LiL54ef5Y2AO+afs+eHn+WNgDvpub3msLTljYA75ZaE5YyW5Y2AO+Wkp+WFp+WNgDvlsbHkuIrljYA75paw5biC5Y2AO+WuieWumuWNgDs+O0A8XGU7XGU7MzI7MzM7MzQ7MzU7MzY7Mzc7MTsyOzM7NDs1OzY7Nzs4Ozk7MTA7MTE7MTI7MTM7MTQ7MTU7MTY7MTc7MTg7MTk7MjA7MjE7MjI7MjM7MjQ7MjU7MjY7Mjc7Mjg7Mjk7MzA7MzE7Pj47Pjs7Pjs+Pjt0PDtsPGk8MT47PjtsPHQ8cDxwPGw8VGV4dDtWaXNpYmxlOz47bDw7bzxmPjs+Pjs+Ozs+Oz4+Oz4+O3Q8QDA8cDxwPGw8RGF0YUtleXM7XyFJdGVtQ291bnQ7PjtsPGw8PjtpPDE+Oz4+Oz47Ozs7Ozs7Oz47bDxpPDA+Oz47bDx0PDtsPGk8MD47aTwxPjs+O2w8dDxwPGw8aHJlZjt0YXJnZXQ7PjtsPC4uL3ZpZXcuYXNweD9zbj00ODc7X3NlbGY7Pj47bDxpPDA+Oz47bDx0PHA8bDxzcmM7YWx0Oz47bDwvVXNlckNvbnRyb2xzLy4uL1VwbG9hZC9TcG90L0ltZ0ZpbGUvNDg3NjM0OTkyODkyNDIwNzUwMDAwLkpQRzvlj7DljZfluILnmb3msrPljYDmnpfliJ3ln6Q7Pj47Oz47Pj47dDxwPGw8aHJlZjtpbm5lcmh0bWw7PjtsPC4uL3ZpZXcuYXNweD9zbj00ODc7Jmx0XDsmbHRcO+eZveays+WNgCZndFw7Jmd0XDvlj7DljZfluILnmb3msrPljYDmnpfliJ3ln6Q7Pj47Oz47Pj47Pj47dDx0PDt0PGk8Mz47QDznrKwx6aCBO+esrDLpoIE756ysM+mggTs+O0A856ysMemggTvnrKwy6aCBO+esrDPpoIE7Pj47bDxpPDI+Oz4+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MTM7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDY7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDM7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDM7Pj47Pjs7Pjs+Pjt0PHA8cDxsPFN5cztEaXNwbGF5O1NuOz47bDxzcG90Ozs7Pj47PjtsPGk8OT47aTwxMD47aTwxMT47aTwxNT47PjtsPHQ8O2w8aTwwPjs+O2w8dDxAMDw7Ozs7Ozs7Oz47Oz47Pj47dDw7bDxpPDA+Oz47bDx0PEAwPDs7Ozs7Ozs7Pjs7Pjs+Pjt0PDtsPGk8MD47PjtsPHQ8QDA8Ozs7Ozs7Ozs+Ozs+Oz4+O3Q8O2w8aTwwPjs+O2w8dDxAMDw7Ozs7Ozs7Oz47Oz47Pj47Pj47Pj47dDxwPHA8bDxTaXRlSUQ7PjtsPGk8NTU+Oz4+Oz47bDxpPDA+O2k8MT47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MjAxNC8xMS8xMDs+Pjs+Ozs+O3Q8cDxsPGlubmVyaHRtbDs+O2w84oCn57i954CP6Ka95Lq65qyh77yaMTE3MDQyNzHmrKE7Pj47Oz47Pj47Pj47Pj47bDxWaWV3MTpTcG90TGlzdDE6U3BvdFF1ZXJ5MTppbWdidG5SdW5RdWVyeTs+PghryBDphJ+jzOZOw2G76NlMiDiV'
      ,'View1:SpotList1:SpotQuery1:ddlSubject':'geography'
      ,'View1:SpotList1:SpotQuery1:ddlTown':''
      ,'View1:SpotList1:ddlPageList':form_data_number}
	  
    tainan_geography = requests.post(tainan_geography_link, data=payload) 
    tainan_geography_text = tainan_geography.text.encode('utf-8')
    tainan_geography_soup=BeautifulSoup(tainan_geography_text)
    tainan_geography_table=tainan_geography_soup.find('table',{"id":"View1_SpotList1_dtlList"})
    tainan_geography_spans = tainan_geography_table.findAll('span',{"id":"main-wrapper"})
	##另開連結取得景點名稱
    for tainan_geography_span in tainan_geography_spans:
        geography_alink = tainan_geography_span.find('a',{"href":True})['href']
        geography_link=urlparse.urljoin(tainan_geography_link,geography_alink)
        geography_page=requests.get(geography_link)
        geography_page_text = geography_page.text.encode('utf-8')
        geography_page_soup=BeautifulSoup(geography_page_text)
        geography_name = geography_page_soup.find('span',{"id":"View1_SpotDetail1_lblName"}).text.encode('utf-8')
        file.write(geography_name.strip()+"\n")