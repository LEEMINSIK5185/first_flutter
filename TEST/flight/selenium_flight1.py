from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_until(xpath_str):
    WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,xpath_str)))

browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://flight.naver.com/'
browser.get(url)

#광고창 닫기
close_btn = browser.find_element(By.XPATH,'//div[@class="btns"]/button[@title="닫기"]')
close_btn.click()

#가는 날 클릭
begin_date = browser.find_element(By.XPATH, '//button[text()="가는 날"]')
begin_date.click()

#time.sleep(3)

wait_until('//b[text()="20"]')
day20 = browser.find_elements(By.XPATH, '//b[text()="20"]')
day20[1].click()

time.sleep(2)

wait_until('//b[text()="27"]')
day27= browser.find_elements(By.XPATH, '//b[text()="27"]')
day27[1].click()

#도착지 클릭
wait_until('//b[text()="도착"]')
arrival = browser.find_element(By.XPATH,'//b[text()="도착"]')
arrival.click()

wait_until('//button[text()="국내"]')
domestic = browser.find_element(By.XPATH,'//button[text()="국내"]')
domestic.click()

wait_until('//i[contains(text(),"제주")]')
jeju = browser.find_element(By.XPATH,'//i[contains(text(),"제주")]')
jeju.click()

#항공권 검색
wait_until('//span[contains(text(),"항공권 검색")]')
search = browser.find_element(By.XPATH,'//span[contains(text(),"항공권 검색")]')
search.click()

elem = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,'//div[@class="domestic_Flight__sK0eA result"]')))

print(elem.text)


