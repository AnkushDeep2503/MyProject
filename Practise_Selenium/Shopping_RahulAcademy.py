from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.i
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("an")
time.sleep(2)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 5
lists = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(len(lists))
for list in lists:
    list.click()
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promocode").send_keys("rahulshetty")
driver.find_element_by_class_name("promoBtn").click()
# time.sleep(4)
driver.close()
