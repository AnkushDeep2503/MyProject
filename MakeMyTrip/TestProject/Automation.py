import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
# men = driver.find_element(By.LINK_TEXT, "Home & Living")
# actions = ActionChains(driver)
# time.sleep(5)
# actions.move_to_element(men).click().perform()
# time.sleep(3)
# driver.close()
