from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.find_element_by_id("twotabsearchtextbox").send_keys("apple")
items = driver.find_elements_by_css_selector(".autocomplete-results-container")
# print(len(list))
for item in items:
    if item.text == "apple watch":
        item.click()
        break
assert driver.find_element_by_id("twotabsearchtextbox").get_attribute('value') == "apple watch"
time.sleep(2)
driver.close()