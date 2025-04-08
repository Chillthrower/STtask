from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()
password = os.getenv("PASSWORD")

# Setup Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 15)

# 1. Login
driver.get("https://lms.nmamit.in/login/index.php")
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("nnm22ad048@nmamit.in")
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "password").send_keys(Keys.RETURN)

# 2. Go to NLP Course
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Natural Language Processing"))).click()

# 3. Wait and Download the Syllabus
syllabus_link_elem = wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'NLP Syllabus')]/ancestor::a"))
)
syllabus_url = syllabus_link_elem.get_attribute("href")
print("📎 Syllabus URL:", syllabus_url)

# Get cookies for download
cookies = driver.get_cookies()
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])

response = session.get(syllabus_url)

if response.status_code == 200:
    filename = "NLP_Syllabus.pdf"
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"✅ Downloaded: {filename}")
else:
    print("❌ Failed to download file:", response.status_code)

# 4. Slowly navigate back step-by-step
time.sleep(2)
print("🔙 Going back to course page...")
driver.back()

time.sleep(2)
print("🔙 Going back to dashboard or courses list...")
driver.back()

time.sleep(2)
print("🔙 Going back to login page...")
driver.back()

# Optional: wait and capture current page title to confirm
time.sleep(2)
print("📄 Current page title:", driver.title)

driver.quit()
