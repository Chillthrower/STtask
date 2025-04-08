from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Path of the file to upload
file_to_upload = os.path.join(os.getcwd(), "test_upload.txt")

# Create a test file if it doesn't exist
if not os.path.exists(file_to_upload):
    with open(file_to_upload, "w") as f:
        f.write("This is a test upload file.")

# Launch browser
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")

time.sleep(1)

# ✅ Find the file input and upload the file
file_input = driver.find_element(By.ID, "file-upload")
file_input.send_keys(file_to_upload)

# ✅ Click the upload button
upload_button = driver.find_element(By.ID, "file-submit")
upload_button.click()

time.sleep(2)

# ✅ Verify upload
uploaded_file = driver.find_element(By.ID, "uploaded-files").text
if uploaded_file == "test_upload.txt":
    print("✅ File uploaded successfully!")
else:
    print("❌ Upload failed.")

driver.quit()
