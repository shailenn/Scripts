import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
#from time import sleep, time, timezone

class PlayStore:

    def __init__(self):
    	self.driver = main()


    def traverse(self):
        print('1HI')
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

        for i in range(5):
            c = self.traverse()

        scrolls = 5
        while True:
            scrolls -= 1
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            if scrolls < 0:
                break

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        names = soup.find_all('span', class_ = 'X43Kjb')
        dates = soup.find_all('span', class_ = "p2TkOb")
        ratings = soup.find_all('div', class_= 'pf5lIe')
        reviews = soup.find_all('div', class_ = "UD7Dzf")

        r = 1
        d = 0
        n = 0
        re = 0

        len_ratings = len(ratings)

        file  = open("reviews.csv","w+")
        while r < len_ratings:
            try:
                while str(names[n].text).find("Kotak") != -1:
                    d += 1
                    n += 1

                val = reviews[re].text.replace(',',';').find('Full Review')

                if val == -1:
                    file.write(",".join([names[n].text, ratings[r].next_element["aria-label"], dates[d].text, reviews[re].text.replace(',',';')]))
                else:
                    file.write(",".join([names[n].text, ratings[r].next_element["aria-label"], dates[d].text, reviews[re].text.replace(',',';').split('Full Review')[1]]))
                file.write('\n')
                #file.write(",".join([names[n].text, ratings[r].next_element["aria-label"], dates[d].text, val = reviews[re].text.replace(',',';').find('Full Review')

            except:
                pass

            r += 1
            d += 1
            n += 1
            re += 1

        time.sleep(5)

def main():
    a = 10

    driver = webdriver.Chrome(executable_path=r"C:\Users\shailendra bisht\Downloads\chromedriver")
    driver.maximize_window()
    baseUrl = 'https://play.google.com/store/apps/details?id=com.divinememorygames.pedometer&showAllReviews=true'
    #baseUrl = 'https://play.google.com/store/apps/details?id=com.msf.kotak&hl=en_IN&showAllReviews=true'
    driver.get(baseUrl)
    time.sleep(5)
    button = driver.find_element_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/c-wiz/div[1]/div/div[1]/div[1]')
    #/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/c-wiz/div[1]/div/div[1]/div[2]/span
    button.click()

    button1 = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/c-wiz/div[1]/div/div[2]/div[1]/span")))
    button1.click()

    return driver



if __name__ == '__main__':
    P = PlayStore()
    P.get_data()
    #P.traverse()
