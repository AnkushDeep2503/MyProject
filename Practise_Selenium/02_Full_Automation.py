import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
list1 = []
list2 = []

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(8)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.find_element_by_css_selector(".search-keyword").send_keys("ber")
time.sleep(3)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(len(buttons))
for button in buttons:
    list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
print(list1)

driver.find_element_by_css_selector("a[class='cart-icon'] img").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
# WebDriverWait(driver, 8)
# wait = WebDriverWait(driver, 8)
# wait.until(expected_conditions.presence_of_element_located(By.CLASS_NAME, "promoCode"))

veggies = driver.find_elements_by_css_selector("p.product-name']")

for veg in veggies:
    list2.append(veg.text)

print(len(list2))
print(list2)

# assert list1 == list2

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//button[text()='Apply']").click()
# wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR, ".promoInfo"))
print(driver.find_element_by_css_selector(".promoInfo").text)
driver.find_element_by_xpath("//button[text()='Place Order']").click()
print("Ankush has successfully run the automation script!")
driver.minimize_window()
