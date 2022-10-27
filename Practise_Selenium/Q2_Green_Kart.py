from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

list1 = []
list2 = []
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
# time.sleep(3)
driver.find_element_by_css_selector(".search-keyword").send_keys("al")
time.sleep(2)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count ==3
buttons = driver.find_elements_by_xpath("//div[@class ='product-action']/button")
print(len(buttons))

for button in buttons:
    # list1.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
# print(list1)

veggies1 = driver.find_elements_by_xpath("//div[@class='product']/h4")
for vegg in veggies1:
    list1.append(vegg.text)
print(list1)


driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 8)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

veggies = driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    list2.append(veg.text)
print(list2)

assert list1 == list2

totAmt = driver.find_element_by_css_selector("span.totAmt").text

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")

driver.find_element_by_class_name("promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print(driver.find_element_by_css_selector("span.promoInfo").text)

discAmt = driver.find_element_by_css_selector("span.discountAmt").text

assert float(discAmt) < int(totAmt)
driver.find_element_by_xpath("//button[text()='Place Order']").click()

dropdown = Select(driver.find_element_by_xpath("//div[@class='wrapperTwo']/div/select"))
dropdown.select_by_visible_text("India")
driver.find_element_by_css_selector("input[type='checkbox']").click()
time.sleep(1)
driver.find_element_by_xpath("//button[text()='Proceed']").click()
time.sleep(2)
driver.minimize_window()
time.sleep(1)
print("The order has been placed successfully")