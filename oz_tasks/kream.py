import warnings
warnings.filterwarnings("ignore", category=Warning)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from bs4 import BeautifulSoup
import pymysql

url = "https://kream.co.kr"

option_ = Options()
option_.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = option_)
driver.get(url)
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)
time.sleep(3)

for i in range(5):
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

items = soup.select(".product_card")
product_list = []

for item in items:
    category = "상의"
    product_name = item.select_one(".text-lookup.display_paragraph.line_break_by_truncating_tail.text-element:not(.semibold)").text
    brand = item.select_one(".semibold.text-lookup.display_paragraph.line_break_by_truncating_tail.text-element").text
    product_price = item.select_one(".label-text-container").text

    # 클래스가 같을경우 구분하는 방법
    # bolds = item.select(".semibold.text-lookup.display_paragraph.line_break_by_truncating_tail.text-element")
    # brand = bolds [0].text
    # product_name = bolds [1].text 
    
    
    product = [category, brand, product_name, product_price]
    product_list.append(product)
    print(f"카테고리: {category}") 
    print(f"브랜드: {brand}")
    print(f"상품명: {product_name}")   
    print(f"가격: {product_price}")
    print()
    
driver.quit()

# DB 연결
connection = pymysql.connect(
    host= '127.0.0.1',
    user = 'root',
    password = 'euncher',
    db = 'kream',
    charset = 'utf8mb4',
    auth_plugin='caching_sha2_password'
)

def execute_query(connection, query, args=None):
    with connection.cursor() as cursor:
        cursor.execute(query, args or ()) #execute 실행 시 오류가 발생하지 않음-> pymysql 공식 문서 참고
        connection.commit()     

for i in product_list:
    query = "INSERT INTO kream (category, brand, product_name, product_price) VALUES (%s, %s, %s, %s)"
    execute_query(connection, query, (i[0], i[1], i[2], i[3]))
