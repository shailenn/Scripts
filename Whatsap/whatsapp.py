from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Load the Excel sheet with the contact and message details
df = pd.read_excel('contacts.xlsx')

# Set up the Selenium webdriver
driver = webdriver.Chrome('C:/Users/bisht/OneDrive/Desktop/Shailen/Whatsap/chromedriver_win32/chromedriver.exe')

# Navigate to WhatsApp Web
driver.get('https://web.whatsapp.com/')
input('Scan the QR code and press Enter to continue')

# Loop through each row in the sheet and send the message to each contact
for i, row in df.iterrows():
    to_number = str(row['Phone'])
    message = str(row['Message'])

    # Search for the contact by name or phone number
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(to_number)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

    # Wait for the message box to be visible
    message_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'))
    )

    # Type the message and send it 
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    time.sleep(2)

    print(f"Message sent to {to_number}")

# Close the browser window
driver.quit()
