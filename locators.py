from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time


service_obj = Service(r"D:\UDEMY_SELENIUM\Python_selenium\msedgedriver.exe")
driver = webdriver.Edge(service = service_obj)

driver.maximize_window()
driver.get("http://rahulshettyacademy.com/angularpractice/")

# selenum locators: ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# XPATH tagname[@attribute = "value"] -> //input[@type = "submit"]
driver.find_element(By.XPATH, "//input[@type = 'submit']").click
message = driver.find_element(By.CLASS_NAME, "alert-success").text # grab the text from class
print(message)

time.sleep(100)