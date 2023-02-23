import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
url = 'https://flight.naver.com/'
browser.get(url)

close_btn_class = browser.find_element(By.XPATH,'//div[@class = "btns"]/button[@title="한 달간 안보기"]')
close_btn_class.click()

begin_date = browser.find_element(By.XPATH, '//button[text()= "가는 날"]')
begin_date.click()

time.sleep(1) # 1초 대기
day30 = browser.find_elements(By.XPATH, '//b[text()= "30"]')
day30[0].click()

day31 = browser.find_elements(By.XPATH,'//b[text()= "31"]')
day31[0].click()

time.sleep(1) # 1초 대기
departure = browser.find_element(By.XPATH,'//b[text()="ICN"]')
departure.click()

d_domestic = browser.find_element(By.XPATH,'//button[contains(text(),"국내")]')
d_domestic.click()

d_domestic_ICN = browser.find_element(By.XPATH,'//i[contains(text(),"인천국제공항")]')
d_domestic_ICN.click()



arrival = browser.find_element(By.XPATH,'//b[text()="도착"]')
arrival.click()

domestic = browser.find_element(By.XPATH,'//button[text()="국내"]')
domestic.click()

jeju = browser.find_element(By.XPATH,'//i[contains(text(),"제주국제공항")]')
jeju.click()

elem = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
print(elem.text)

