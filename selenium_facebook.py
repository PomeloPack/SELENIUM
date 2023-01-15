from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time


service_obj = Service(r"D:\UDEMY_SELENIUM\Python_selenium\msedgedriver.exe")
driver = webdriver.Edge(service = service_obj)

driver.get("https://www.facebook.com/")

driver.find_element(By.ID, "email").send_keys("youremail@gmail.com")
driver.find_element(By.ID, "pass").send_keys("123456")

time.sleep(100)
