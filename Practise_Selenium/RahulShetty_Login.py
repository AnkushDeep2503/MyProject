from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
# driver.find_element_by_css_selector("input[name='name']").send_keys("Ankush Deep")
driver.find_element_by_xpath("//input[@name='name']").send_keys("dimag na khaa subha subah yaar")
driver.find_element_by_xpath("//input[@name='email']").send_keys("abc@google.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("anything")

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
dropdown.select_by_index(1)
driver.find_element_by_xpath("//input[@value='Submit']").click()
print(driver.find_element_by_class_name("alert-dismissible").text)
message = driver.find_element_by_css_selector(".alert-success").text
# message = driver.find_element_by_class_name("alert-dismissible").text
assert "success" in message
# driver.find_element_by_class_name('form-control ng-pristine ng-invalid ng-touched')
# time.sleep(1)
driver.close()