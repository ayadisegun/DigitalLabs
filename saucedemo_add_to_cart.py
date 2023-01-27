import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.CLASS_NAME, "input_error").send_keys("standard_user")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(10)

#add five items to cart
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()
time.sleep(5)

#removing 2 of the added items
driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-backpack']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-bolt-t-shirt']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-onesie']").click()
time.sleep(5)

#adding two more item
driver.find_element(By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
time.sleep(5)

#checkout
driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='checkout']").click()
time.sleep(5)

#Logout
driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()
time.sleep(5)

#close browser
driver.quit()

#pip install webdriver-manager
#pip installchromdriver-autoinstaller