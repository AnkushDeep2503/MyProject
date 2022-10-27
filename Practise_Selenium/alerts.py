import time

from selenium import webdriver
validateText = "option2"
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_xpath("//input[@placeholder='Enter Your Name']").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text #for taking the texts present in the alert
assert validateText in alertText # for validating whether "option2" is present in alert text or not.
print(alert.text) #for printing the alert
time.sleep(1)
alert.accept() # for accepting the alert
driver.close()
