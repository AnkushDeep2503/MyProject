from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    checkbox.click() #for clicking all the checkboxes
    assert checkbox.is_selected()

# for selecting single checkbox out of many
# for checkbox in checkboxes:
#     if checkbox.get_attribute("value") == "option3":
#         checkbox.click()
#         assert checkbox.is_selected()

radiobuttons = driver.find_elements_by_xpath("//input[@class='radioButton']")
print(len(radiobuttons))
# for radiobutton in radiobuttons:
#     radiobutton.click()
#     assert radiobutton.is_selected()

for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value") == "radio2":
        radiobutton.click()
        assert radiobutton.is_selected()
