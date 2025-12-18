import requests
from bs4 import BeautifulSoup

keyword = input("검색어를 입력해주세요")
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + keyword

req = requests.get(url)
# print(req)

html = req.text
# print(html)
soup = BeautifulSoup(html, "html.parser")
result = soup.select(".sds-comps-vertical-layout.sds-comps-full-layout.pSGytgqBoO_qDdSTbXs9")
for i in result:
    ad = i.select_one(".fender-ui_9e91b986")

    if not ad:
        writer = i.select_one(".sds-comps-text.sds-comps-text-ellipsis.sds-comps-text-ellipsis-1").text
        title = i.select_one(".sds-comps-text.sds-comps-text-ellipsis.sds-comps-text-ellipsis-1.sds-comps-text-type-headline1.sds-comps-text-weight-sm").text
        dsc = i.select_one(".sds-comps-text.sds-comps-text-type-body1.sds-comps-text-weight-sm").text
        link = i.select_one(".fender-ui_228e3bd1.zsOIyFgaikMtT9gmM_tR")["href"]

        print(f"제목 : {title}")
        print(f'제목 : {title}')
        print(f'작성자 : {writer}')
        print(f'글요약 : {dsc}')
        print(f'링크 : {link}')
        print()