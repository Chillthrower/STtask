from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")

# Wait for page to load
time.sleep(2)

# ✅ Step 1: Switch to the iframe containing the date picker
iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
driver.switch_to.frame(iframe)

# ✅ Step 2: Click the input box to open the date picker
date_input = driver.find_element(By.ID, "datepicker")
date_input.click()

time.sleep(1)  # Optional: wait for calendar to open

# ✅ Step 3: Select a date (e.g., 15th of the current month)
date_to_select = driver.find_element(By.XPATH, "//a[text()='15']")
date_to_select.click()

# ✅ Step 4: Validate selected date
selected_value = date_input.get_attribute("value")
print(f"✅ Selected date: {selected_value}")

# Cleanup
time.sleep(2)
driver.quit()
