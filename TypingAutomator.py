from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time

# Assuming you're using Chrome as the WebDriver. Update this based on your browser driver.
driver = webdriver.Chrome()

# Open a webpage
driver.get('https://humanbenchmark.com/tests/typing')

# Wait for the elements with class name 'incomplete' to be present
wait = WebDriverWait(driver, 5)
incomplete_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'incomplete')))

# Collect text content from each element and interpret '<span class="incomplete"> </span>' as spaces
text_to_type = ''
for element in incomplete_elements:
    # Check if the element represents a space (using the outerHTML attribute)
    if element.get_attribute('outerHTML') == '<span class="incomplete"> </span>':
        text_to_type += ' '  # Interpret '<span class="incomplete"> </span>' as space
    else:
        text_to_type += element.text  # Append the text content

# Sleep for a few seconds to allow switching to the input field
time.sleep(1)  # Adjust this delay as needed

# Simulate typing the collected text using pyautogui
pyautogui.write(text_to_type, interval=0)

time.sleep(100)  # Adjust this delay as needed

driver.quit()
