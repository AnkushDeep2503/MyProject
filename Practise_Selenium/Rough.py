from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# # service_obj = Service("C://Chrome//chromedriver.exe")
# # driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://www.wikipedia.org/")
#
# # driver.get("https://rahulshettyacademy.com/angularpractice/")
#
# print(driver.title)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://rahulshettyacademy.com/angularpractice/")