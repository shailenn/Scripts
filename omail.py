import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.support.select import Select
#from time import sleep, time, timezone

a = 10

class Omail:

	def __init__(self):
		self.driver = main()


	def newemail(self, enteredkey):
		print('check')
		driver = self.driver
		
		#New EMail Extraction
	
		time.sleep(10)
	
		extraction = driver.find_element_by_xpath('//*[@id="id_button_extract"]')   
		extraction.click()
		
		#Inputs            
		
		time.sleep(1)
		
		#Selection of keyword
		keyword = driver.find_element_by_xpath('//*[@id="keywords"]').send_keys(enteredkey)
		
		#Select from dropdown
		sel = Select(driver.find_element_by_xpath('//*[@id="country"]'))
		sel.select_by_visible_text("Albania(Shqipëri)")
		time.sleep(1)
		#sel.select_by_index(0)
	
		#Start Extraction 
	
		start_extraction = driver.find_element_by_xpath('//*[@id="id_start_extract"]')
		start_extraction.click()
		
		#sleep to be increased if code stopped while extraction
		time.sleep(40)		
		
		#Click on cancel after extraction
		cancel = driver.find_element_by_xpath('//*[@id="id_dialog_mail_list_close"]')
		cancel.click()
		
		
	def get_data(self):
		print('loops')
		driver = self.driver
		
		#Reading file for keywords
		
		keyfile = open('omail.txt', 'r')
		keys = keyfile.readlines()

		#shifting keys from file to list named as list_of_keywords
		list_of_keywords = [key.strip() for key in keys]
		print(list_of_keywords) 
		
		clear = [2,4,6,8]
		#enteredkey is the current keyword for individual i in loop
		for i in range(5):
			#Clear the databse if it is full
			if i in clear:
				e = self.databse()
				#Now clear
				checkbox = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[6]/div[1]/table/thead/tr/th[1]/label/input')
				checkbox.click()
				
				#Click on remove
				time.sleep(5)
				remove = driver.find_element_by_xpath('//*[@id="id_button_remove"]')
				remove.click()
				
				#Popup remove 
				time.sleep(5)
				popupcheckbox = driver.find_element_by_xpath('//*[@id="id_dialog_remove"]')
				popupcheckbox.click()
				
				#GoTo Email Extractor page
				time.sleep(5)
				extra = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/ul/li[2]/a')
				extra.click()
								
				
				#Than continue the loop
				enteredkey = list_of_keywords[i]
				f = self.newemail(enteredkey)
				
			else:
			
				enteredkey = list_of_keywords[i]
				c = self.newemail(enteredkey)
			
		d = self.databse()

	def databse(self):
		driver = self.driver
		
		#Click on Email Database
		database1000 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/ul/li[3]/a')
		database1000.click()
		
		#soup = BeautifulSoup(driver.page_source, 'html.parser')		
		#print(soup didn't work so using selenium driver to extract data)
		
		email_list = []
		table_id = driver.find_element_by_xpath('//*[@id="table_mail_list"]')
		rows = table_id.find_elements(By.TAG_NAME, "tr")
		for row in rows:
			email_list.append(row.text)
		
		#Pop 0th element i.e. first row
		#email_list.pop(0)
		
		#Extracting from 1st page and after clicking on nextpage1 it will switch to page 2
		next_page1 = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[6]/div[2]/ul/li[6]/a')
		next_page1.click()
		time.sleep(5)
		#print(email_list)
		
		while True:
			try:

				#from page 2 till last page while will run to extract data
				table_id = driver.find_element_by_xpath('//*[@id="table_mail_list"]')
				rows = table_id.find_elements(By.TAG_NAME, "tr")
				for row in rows:
					email_list.append(row.text)
				print(email_list)
				
				next_page = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div[2]/div[6]/div[2]/ul/li[8]/a')
				next_page.click()
				time.sleep(5)
			
			#while break on reaching to last page				
		
			except:
				break
				
		#Remove duplicates of 1st heading row
		final_email_list = set(email_list)
		
		email_lists = list(final_email_list)
		
		#Pop 0th element i.e. first row
		email_lists.pop(0)
		
		file = open('omailemail.csv','a+')
		#file.join()
		
		for i in email_lists:
			print(i.split(' ')[0])
			#file.write(",".join(i.split(' ')[0], i.split(' ')[1], i.split(' ')[2], i.split(' ')[3]))
			file.write(i.split(' ')[0])
			
			
			file.write("\n")
			#Website :- print(i.split(' ')[1])
			#Mail_Type :- print(i.split(' ')[2])
			#Mail_Exchanger :- print(i.split(' ')[3])
		file.close()
		
		
	

def main():
	driver = webdriver.Chrome(executable_path=r"C:\Users\shailendra bisht\Downloads\chromedriver.exe")
	driver.maximize_window()
	baseUrl = 'https://omail.io/'

	driver.get(baseUrl)
	time.sleep(5)
		
	#Click on Extract Email from Websites
	
	button = driver.find_element_by_xpath('/html/body/div/div[2]/section[1]/div/div[1]/a')
	button.click()
	
	#Click on SignIn
		
	SignIn = driver.find_element_by_xpath('/html/body/div/div[2]/section/div/div/div/form/div/table/tbody/tr[5]/td[2]/a')
	SignIn.click()
	#time.sleep(50)
	
	#Login by email and password
	
	email = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[1]//*[@id="username"]').send_keys('ciarah273@eicircuitm.com')
	password = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[2]//*[@id="password"]').send_keys('109262')
	login = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/form/div[5]/button')
	login.click()
		
	return driver

if __name__ == '__main__':
	O = Omail()
	O.get_data()
	
#Account name: ciarah273@eicircuitm.com
#Password: 109262                         //*[@id="loginname"]


#1st :- /html/body/div/div[2]/section/div/div/div/form/div/table/tbody/tr[3]/td[2]//*[@id="loginname"]
