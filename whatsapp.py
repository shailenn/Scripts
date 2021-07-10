from selenium import webdriver
import time
#from time import sleep

driver_path =r"C:\Users\shailendra bisht\Downloads\chromedriver"
driver = webdriver.Chrome(driver_path)
driver.get('https://web.whatsapp.com/')


input("Enter anything after scanning QR code ")


user = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]')
user.click()

#change the user by copying its xpath
count = 0
for i in range(5000):
	try :
		count = count + 1
		driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys('Bhai bas kar yaar')
		#time.sleep(2)
		#https://chat.whatsapp.com/GlzkkxP5zEX8pvYslQXz3a
		#'Check'+ str(count)
		button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')

		button.click()
	except :
		pass


#Pin the chat at the top for not to change any xpath

# yu2CQLR64EJAFQ3A
