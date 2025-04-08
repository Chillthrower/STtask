from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.w3schools.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Step 1: Click on "Log in"
login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in")))
login_button.click()

# Step 2: Click on "Forgot Password?" button
forgot_password_button = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//button[text()='Forgot Password?']")))
forgot_password_button.click()

# Step 3: Enter email into the email input
email_input = wait.until(EC.presence_of_element_located((
    By.CLASS_NAME, "ResetPasswordForm_reset_password_email_input__W7j0k")))
email_input.send_keys("ringoroadagain41@gmail.com")

# Step 4: Click on "Reset Password" button
reset_button = wait.until(EC.element_to_be_clickable((
    By.XPATH, "//button[text()='Reset Password']")))
reset_button.click()

# Step 5: Wait and close (optional)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Snackbar_snackbar__message__3p_wI")))
print("Reset password request submitted.")

driver.quit()
