from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url="https://www.dr.com.tr/"

driver.get(url)

time.sleep(2)
driver.maximize_window()
time.sleep(5)

kitap=driver.find_element("xpath","/html/body/div[1]/header/div[3]/div[2]/ul/li[1]/a")
kitap.click()
driver.get(kitap)
time.sleep(10)