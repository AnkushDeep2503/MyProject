from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_link_text("Shop").click()
print(driver.find_element_by_link_text("Nokia Edge").text)
print(driver.find_element_by_class_name("text-muted").text)
driver.find

driver.close()