import warnings
warnings.filterwarnings("ignore", category=Warning)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

import time

keyword = input("검색어를 입력해주세요: ")
url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=" + keyword

options_ = Options()
options_.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options_)
driver.get(url)
time.sleep(2)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

html = driver.page_source
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

time.sleep(3)
driver.quit()

print(len(result))