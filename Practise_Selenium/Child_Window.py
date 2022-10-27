from selenium import webdriver
# import time

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()

childWindow = driver.window_handles[1]
driver.switch_to.window(childWindow)
print(driver.find_element_by_tag_name("h3").text)
assert "New Window" == driver.find_element_by_tag_name("h3").text
# time.sleep(2)
driver.close()


parentWindow = driver.window_handles[0]
driver.switch_to.window(parentWindow)
print(driver.find_element_by_tag_name("h3").text)

assert "Opening a new window" == driver.find_element_by_tag_name("h3").text

