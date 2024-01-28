print("Time to upload this")

import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# In this script will select client in configuration page

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("http://www.google.com")
driver.maximize_window()

time.sleep(10)
driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("Implement CICD in Selenium")
driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").click()
time.sleep(10)