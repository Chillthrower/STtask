from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("https://jqueryui.com/checkboxradio/")
time.sleep(2)

# ✅ Step 1: Switch to iframe
iframe = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
driver.switch_to.frame(iframe)

# ✅ Checkbox 1: Select and Deselect
checkbox1_label = driver.find_element(By.XPATH, "//label[@for='checkbox-1']")
checkbox1_input = driver.find_element(By.ID, "checkbox-1")

checkbox1_label.click()
time.sleep(1)
assert checkbox1_input.is_selected()
print("✅ Checkbox 1 selected")

checkbox1_label.click()
time.sleep(1)
assert not checkbox1_input.is_selected()
print("✅ Checkbox 1 deselected")

# ✅ Checkbox 2: Select and Deselect
checkbox2_label = driver.find_element(By.XPATH, "//label[@for='checkbox-2']")
checkbox2_input = driver.find_element(By.ID, "checkbox-2")

checkbox2_label.click()
time.sleep(1)
assert checkbox2_input.is_selected()
print("✅ Checkbox 2 selected")

checkbox2_label.click()
time.sleep(1)
assert not checkbox2_input.is_selected()
print("✅ Checkbox 2 deselected")

# ✅ Radio button selection and deselection via switching
radio2_label = driver.find_element(By.XPATH, "//label[@for='radio-2']")
radio2_input = driver.find_element(By.ID, "radio-2")

radio2_label.click()
time.sleep(1)
assert radio2_input.is_selected()
print("✅ Radio button 2 selected")

# Switch to Radio 1 to deselect Radio 2
radio1_label = driver.find_element(By.XPATH, "//label[@for='radio-1']")
radio1_input = driver.find_element(By.ID, "radio-1")

radio1_label.click()
time.sleep(1)
assert radio1_input.is_selected()
assert not radio2_input.is_selected()
print("✅ Radio button 2 deselected, Radio button 1 selected")

# Final wait to observe
time.sleep(3)

driver.quit()
