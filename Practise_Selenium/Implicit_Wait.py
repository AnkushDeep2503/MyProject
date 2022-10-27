from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
# assert count == 3
lists = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(len(lists))
for list in lists:
    list.click()
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# WebDriverWait(driver, 5)

driver.find_element_by_class_name("promocode").send_keys("rahulshettyacaddemy")
driver.find_element_by_class_name("promoBtn").click()
# time.sleep(4)
# driver.close()