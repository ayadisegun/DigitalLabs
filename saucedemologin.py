import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.get("https://www.saucedemo.com/")

driver.find_element(By.CLASS_NAME, "input_error").send_keys("standard_user")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(5)

#pip install webdriver-manager
#pip installchromdriver-autoinstaller