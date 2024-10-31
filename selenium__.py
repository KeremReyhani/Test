import time

from selenium import webdriver

driver=webdriver.Chrome()

url = "https://www.python.org/"

driver.get(url)
time.sleep(3)
driver.maximize_window()
#driver.save_screenshot("ekrangoruntusu.png")
time.sleep(3)
driver.minimize_window()
url="http://bologna2024.yildiz.edu.tr/index.php?r=program/view&id=37&aid=24"
driver.get(url)
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
driver.close()