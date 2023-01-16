from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# implicitly wait -> driver.implicitly_wait(20) : WebDriver instance polls the HTML DOM for a certain duration when trying to find any element. 
# This is useful when certain elements on the webpage are not available immediately and need some time to load. 
# Implicit waiting for elements to appear is disabled by default and will need to be manually enabled on a per-session basis

# explcit wait -> wait = WebDriverWait(driver, 5) : Explicit waits allows our code to halt program execution, or freeze the thread, until the condition we pass it resolves. 
# The condition is called with a certain frequency until the timeout of the wait is elapsed. 
# This means that for as long as the condition returns a falsy value, it will keep trying and waiting. 
# Thus Explicit waits allows us to wait for a condition to occur which inturn synchronises the state between the browser and its DOM Tree, and the WebDriver script.

service_obj = Service(r"D:\UDEMY_SELENIUM\Python_selenium\msedgedriver.exe")
driver = webdriver.Edge(service = service_obj)
wait = WebDriverWait(driver, 5) # waiting for definition time and after that open the driver

driver.maximize_window()
driver.get("https://www.facebook.com/")
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//img[@alt = 'Facebook']"))) # function which waiting for showing element in our case is image alt = Facebook ( waiting for loading webside no sleep !!!)
driver.find_element(By.ID, "email").send_keys("youremail@gmail.cz")
driver.find_element(By.ID, "pass").send_keys("123456")
wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-cookiebanner = 'accept_button']")))
driver.find_element(By.XPATH, "//button[@data-cookiebanner = 'accept_button']").click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()



time.sleep(5000)
