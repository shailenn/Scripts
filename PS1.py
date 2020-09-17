import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

class PlayStore:

    def __init__(self):
    	self.driver = main()


    def traverse(self):
        print('Hi')
        driver = self.driver
        scrolls = 5
        while True:
            scrolls -= 1
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            if scrolls < 0:
                break

        show_more = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'RveJvd snByac')]")))
        show_more.click()

    def get_data(self):
        print('Hello')
        driver = self.driver
        #driver = webdriver.Chrome(executable_path=r"C:\Users\shailendra bisht\Downloads\chromedriver")
        #driver.maximize_window()
        #baseUrl = 'https://play.google.com/store/apps/details?id=com.msf.kotak&hl=en_IN&showAllReviews=true'
        #driver.get(baseUrl)

        for i in range(1):
            c = self.traverse()

        scrolls = 5
        while True:
            scrolls -= 1
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            if scrolls < 0:
                break


        reviews = WebDriverWait(driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[@class='UD7Dzf']")))

        names = WebDriverWait(driver, 30).until(
            #.EC.presence_of_all_elements_located((By.XPATH, "//*[@class='X43Kjb']")))

        dates = WebDriverWait(driver, 30).until(
            #.EC.presence_of_all_elements_located((By.XPATH, "//*[@class='p2TkOb']")))

        ratings = WebDriverWait(driver, 30).until(
            #.EC.presence_of_all_elements_located((By.XPATH, "//*[@class='pf5lIe'].find_next()['aria-label']")))



        #reviews = driver.find_elements_by_xpath("//*[@class='UD7Dzf']")
        l1 = list()
        l2 = list()
        l3 = list()
        l4 = list()

        for review in reviews:
            l1.append(review.text)
        #print(l1)

        for name in names:
            l2.append(name.text) #Odd and even separated below
        #print(l2)

        for date in dates:
            l3.append(date.text)
        #print(l3)

        for rating in ratings:
            l4.append(rating.text)
        print(l4)

        #Remove even_indexed element from thelist
        odd_i = []
        even_i = []
        for i in range(0, len(l2)):
            if i % 2:
                even_i.append(l2[i]) # List of Kotak
            else :
                odd_i.append(l2[i])  #List of names

        res = odd_i + even_i
        #print("Seprated odd and even index list: " + str(res))

        # d15Mdf bAhLNe
        #check = driver.find_elements(By.CLASS_NAME, 'X43Kjb')
        #print(check)

        no_of_reviewers = len(driver.find_elements(By.CLASS_NAME, 'd15Mdf'))
        print(no_of_reviewers)



def main():
    a = 10

    driver = webdriver.Chrome(executable_path=r"C:\Users\shailendra bisht\Downloads\chromedriver")
    driver.maximize_window()
    baseUrl = 'https://play.google.com/store/apps/details?id=com.msf.kotak&hl=en_IN&showAllReviews=true'
    driver.get(baseUrl)

    return driver



if __name__ == '__main__':
    P = PlayStore()
    P.get_data()
    #P.traverse()
