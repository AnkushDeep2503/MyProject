from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("I am a software developer in test")
driver.switch_to.default_content()

print(driver.find_element_by_tag_name("h3").text)
