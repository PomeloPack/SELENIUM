from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time


service_obj = Service(r"D:\UDEMY_SELENIUM\Python_selenium\msedgedriver.exe")
driver = webdriver.Edge(service = service_obj)

driver.maximize_window()
driver.get("http://rahulshettyacademy.com/client")

"""
# this is the previously way how to do it
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("mytestmail@gmail.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456.")
driver.find_element(By.ID, "confirmPassword").send_keys("123456.")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
"""

# second way with using SELECTORHUB selected by form
# write to hub //form/div[1]/input = got loggin input
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("mytestmail@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("123456.")
driver.find_element(By.XPATH, "//form/div[3]/input").send_keys("123456.")
driver.find_element(By.XPATH, "//form/div/button").click()




time.sleep(5000)

