from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click()
mobiles = driver.find_elements_by_xpath("//div[@class='card h-100']")
for mobile in mobiles:
    mobileName = mobile.find_element_by_xpath("div/h4")
    if mobileName == "Samsung Note 8" and "Blackberry":
        mobile.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_css_selector("button[class='btn btn-success']").click()
driver.find_element_by_css_selector("input[class*='validate']").send_keys("In")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div.suggestions")))
countries = driver.find_elements_by_css_selector("div.suggestions")
print(len(countries))
for country in countries:
    if country.text == "China":
        country.click()
        break
# driver.find_element_by_link_text("India").click()
driver.find_element_by_css_selector("div.checkbox").click()