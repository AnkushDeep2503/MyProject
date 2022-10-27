from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_css_selector("#autosuggest").send_keys("bel")
time.sleep(1)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "Belize":
        country.click()
        break

print(driver.find_element_by_css_selector("#autosuggest").text)
#assert is used to debug, to know if the test case is failed or passed
assert driver.find_element_by_css_selector("#autosuggest").get_attribute("value") == "Belize"

driver.close()