from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
email = driver.find_element(By.CSS_SELECTOR, "strong a").text
print(email)
driver.close()
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.CSS_SELECTOR, "#username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
# error_message = driver.find_element(By.XPATH,"//form/div[1]/strong").text
# print(error_message)
wait = WebDriverWait(driver, 15)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
error_message = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
print(error_message)