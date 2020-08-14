from selenium import webdriver

driver_path =r"C:\Users\shailendra bisht\Downloads\chromedriver"
driver = webdriver.Chrome(driver_path)
driver.get('https://web.whatsapp.com/')

#name = input("Enter the name of the user of the group : ")
#msg = input("Enter your message : ")
#count = int(input("Enter the count "))

input("Enter anything after scanning QR code ")

#user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))             
#user = driver.find_element_by_xpath('//*[@id="pane-side"]')
user = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]')
user.click()

#msg_box = driver.find_element_by_class_name('_13mgZ')

msg_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]').send_keys('Hi')
#msg_box = driver.find_element_by_xpath('//*[@id="main"]').send_keys('Hi')

for i in range(5):
	msg_box.send_keys(msg)
	#button = driver.find_element_by_class_name('_3M-N-')
	button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')
	#button = driver.find_element_by_xpath('//*[@id="main"]')
	button.click()
	
#Merged	
#class="_19RFN _1ovWX _F7Vk"
#Msg Box
#class="_3u328 copyable-text selectable-text"
#SendKey
