from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click()
mobiles = driver.find_elements_by_xpath("//div[@class='card h-100']")
print(len(mobiles))
for mobile in mobiles:
    # mobile.driver.find_element_by_css_selector("h4[class='card-title']").text
    mobileName = mobile.find_element_by_xpath("div/h4/a").text
    if mobileName == "Nokia Edge":
        mobile.find_element_by_xpath("div[2]/button").click()

driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_css_selector("input#country").send_keys("india")

wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element_by_link_text("India").click()
driver.find_element_by_css_selector("div.checkbox").click()
driver.find_element_by_xpath("//input[@value='Purchase']").click()
successMessage = driver.find_element_by_css_selector("div[class*='alert-dismissible']").text
assert "delivered" in successMessage

driver.get_screenshot_as_file("success-screenshot.png")