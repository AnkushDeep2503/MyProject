import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector(".search-keyword").send_keys("ber")
time.sleep(4)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)
assert count == 3
buttons = driver.find_elements_by_css_selector("div[class='product-action'] button")
print(len(buttons))
for button in buttons:
    button.click()

driver.find_element_by_css_selector("a[class='cart-icon'] img").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

time.sleep(4)
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
time.sleep(4)
driver.find_element_by_xpath("//button[text()='Apply']").click()
time.sleep(8)
print(driver.find_element_by_css_selector(".promoInfo").text)
driver.find_element_by_xpath("//button[text()='Place Order']").click()
time.sleep(5)

