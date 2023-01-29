from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time


service_obj = Service(r"D:\UDEMY_SELENIUM\Python_selenium\msedgedriver.exe")
driver = webdriver.Edge(service = service_obj)

driver.maximize_window()
driver.get("http://rahulshettyacademy.com/angularpractice/")

# selenum locators: ID, Xpath, CSSSelector, Classname, Name, linkText

# ID, Name select
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# CSS tagname[attribute = "value"] -> //input[@type = "submit"] in selectorhub we can usefor id #idname; for classname .classname
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Martin")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(" ")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear() # to clear the window


# XPATH tagname[@attribute = "value"] -> //input[@type = "submit"]
driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text # grab the text from class
print(message)
assert "Success" in message





time.sleep(5000)