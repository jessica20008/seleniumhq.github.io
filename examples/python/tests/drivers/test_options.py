from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set path to your WebDriver (e.g., chromedriver)
driver_path = 'path_to_your_chromedriver'

# Open the browser
driver = webdriver.Chrome(executable_path=driver_path)

# Go to the website URL
url = "https://hajj.nusuk.sa/package/10ba0000-56b2-0050-812b-08dd6172ab77/booking/6c2f0000-56b2-0050-f4e5-08dd6238bcf5/checkout"
driver.get(url)

# Wait for the page to load (you can adjust the sleep time or use WebDriverWait for better handling)
time.sleep(5)

# Locate the "Purchase" button (modify the selector to match the button you need)
purchase_button = driver.find_element(By.XPATH, '//button[contains(text(), "Purchase")]')

# Click the purchase button
purchase_button.click()

# Optionally, add more steps for filling in payment details, etc. 
# (if you want to automate more actions, you would need to inspect the page and find the correct elements)

# Wait for a few seconds to see the action
time.sleep(10)

# Close the browser
driver.quit()
