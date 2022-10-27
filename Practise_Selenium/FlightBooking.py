from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ca")
time.sleep(2)
countries = driver.find_elements_by_css_selector("ul[id='ui-id-1'] li")
print(len(countries))
for country in countries:
    if country.text == "Canada":
        country.click()
        break
# print(driver.find_element_by_id("autosuggest").text)
method = driver.find_element_by_id("autosuggest").get_attribute('value')
assert method == "Canada"
print(method)

driver.close()