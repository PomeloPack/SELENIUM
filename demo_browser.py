from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time



# microsoft edge driver
service_obj = Service(r"D:\UDEMY_SELENIUM\Python_selenium\msedgedriver.exe")

# create driver for edge borwser
driver = webdriver.Edge(service = service_obj)

driver.maximize_window()
driver.get("https://google.com")
print(driver.title)
print(driver.current_url)

driver.get("https://www.hogwartslegacy.com/en-us")
driver.minimize_window
driver.back()
driver.refresh()
driver.forward()

time.sleep(100)





