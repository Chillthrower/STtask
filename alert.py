from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

# 1️⃣ Handle JS Alert
alert_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
alert_button.click()
time.sleep(1)

alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()
print("✅ JS Alert accepted\n")
time.sleep(2)

# 2️⃣ Handle JS Confirm
confirm_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
confirm_button.click()
time.sleep(1)

confirm = driver.switch_to.alert
print("Confirm text:", confirm.text)
confirm.dismiss()  # or .accept() to accept
print("✅ JS Confirm dismissed\n")
time.sleep(2)

# 3️⃣ Handle JS Prompt
prompt_button = driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']")
prompt_button.click()
time.sleep(1)

prompt = driver.switch_to.alert
print("Prompt text:", prompt.text)
prompt.send_keys("Selenium Test")
time.sleep(1)
prompt.accept()
print("✅ JS Prompt accepted with input\n")

# Wrap up
time.sleep(3)
driver.quit()
