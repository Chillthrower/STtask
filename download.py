from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time

# Set download directory
download_dir = os.getcwd()

# Chrome preferences to auto download
options = Options()
prefs = {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
}
options.add_experimental_option("prefs", prefs)

# Launch browser
driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/download")

time.sleep(2)  # wait for page load

# ✅ Locate the specific file link by text and click
file_name = "IMG-20170724-WA0109.jpg"
file_link = driver.find_element(By.LINK_TEXT, file_name)
file_link.click()

print(f"✅ Download triggered for: {file_name}")

# Wait for download
time.sleep(10)

# ✅ Confirm file exists
file_path = os.path.join(download_dir, file_name)
if os.path.exists(file_path):
    print(f"✅ File '{file_name}' downloaded successfully at {file_path}")
else:
    print(f"❌ File '{file_name}' not found in {download_dir}")

driver.quit()
