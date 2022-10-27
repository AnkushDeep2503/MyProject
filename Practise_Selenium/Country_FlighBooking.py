from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/#")
driver.find_element_by_css_selector("#autosuggest").send_keys("es")
time.sleep(1)
countries = driver.find_elements_by_xpath("//ul[@id='ui-id-1']/li")
print(len(countries))
time.sleep(1)
for country in countries:
    if country.text == "Indonesia":
        country.click()
        break

country_name = driver.find_element_by_css_selector("#autosuggest").get_attribute('value')
assert country_name == "Indonesia"
print("The name of the selected country is", country_name)
time.sleep(1)
driver.close()
