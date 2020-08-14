from selenium import webdriver

driver_path =r"C:\Users\shailendra bisht\Downloads\chromedriver"
driver = webdriver.Chrome(driver_path)
driver.get('https://web.whatsapp.com/')


input("Enter anything after scanning QR code ")


user = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]')
user.click()

#change the user by copying its xpath

for i in range(2):
	driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys('Automation test')
	
	button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')

	button.click()
	
	
#Pin the chat at the top for not to change any xpath


