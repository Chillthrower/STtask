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
options.add_argument("--start-maximized")

# Launch browser
driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/download")

time.sleep(2)  # Wait for page to load

# ✅ Print all available file links
links = driver.find_elements(By.TAG_NAME, "a")
file_list = [link.text for link in links if link.get_attribute("href") and link.text.endswith(('.txt', '.jpg', '.png', '.pdf', '.csv'))]

if not file_list:
    print("❌ No downloadable files found.")
    driver.quit()
    exit()

# ✅ Choose a file from the list (first one for simplicity)
file_name = file_list[0]
print(f"📄 Found downloadable files: {file_list}")
print(f"⬇️ Downloading: {file_name}")

# ✅ Click to download the file
file_link = driver.find_element(By.LINK_TEXT, file_name)
file_link.click()

# ⏳ Wait for download to finish
time.sleep(10)

# ✅ Confirm file exists
file_path = os.path.join(download_dir, file_name)
if os.path.exists(file_path):
    print(f"✅ File '{file_name}' downloaded successfully at {file_path}")
else:
    print(f"❌ File '{file_name}' not found in {download_dir}")

driver.quit()
