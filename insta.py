from instabilgi import kullanici_adi,sifre
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
url="https://www.instagram.com/accounts/login/?next=%2Facccounts%2Flogin%2F&source=desktop_nav&hl=tr"
driver.get(url)
time.sleep(10)
ka=driver.find_element("xpath","//*[@id='loginForm']/div/div[1]/div/label/input")
ka.send_keys(kullanici_adi)
sif=driver.find_element("xpath","//*[@id='loginForm']/div/div[2]/div/label/input")
sif.send_keys(sifre)
sif.send_keys(Keys.ENTER)
time.sleep(2)
driver.maximize_window()
time.sleep(15)