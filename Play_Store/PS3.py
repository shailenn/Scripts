import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
import re
#from time import sleep, time, timezone

### Global Variables ###
filename = "rahullinks.txt"
skiprating = "5"
filelist = []

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


class PlayStore:

    def __init__(self, url, date):
        # driver = webdriver.Firefox(executable_path=r"./geckodriver")
        driver = webdriver.Chrome(executable_path=r"C:\Users\shailendra bisht\Downloads\chromedriver.exe")
        driver.maximize_window()
        driver.get(url)
        time.sleep(5)
        if len(driver.window_handles) > 1 :
            driver.switch_to_window(driver.window_handles[1])
        self.name = driver.find_elements_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div/main/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1/span')[0].text
        self.name.strip()
        self.name = deEmojify(self.name)
        self.name = " ".join([i for i in self.name.split(" ") if i.isalnum()])
        self.skipname = driver.find_element_by_css_selector('span.T32cc:nth-child(1) > a:nth-child(1)').text
        self.skipname.strip()
        baseUrl = url + '&showAllReviews=true'
        driver.get(baseUrl)
        time.sleep(5)
        button = driver.find_element_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/c-wiz/div[1]/div/div[1]/div[1]')
        button.click()
        button1 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/div/main/div/div[1]/div[2]/c-wiz/div[1]/div/div[2]/div[1]/span")))
        button1.click()
        print(self.name, self.skipname)
        self.driver = driver
        self.date = date.strip()
        


    def traverse(self):
        driver = self.driver
        scrolls = 5
        while scrolls > 0:
            try:
                scrolls -= 1
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(3)
            except:
                break
        try:       
            show_more = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'RveJvd snByac')]")))
            show_more.click()
        except:
            return True
        return False

    def get_data(self):
        driver = self.driver

        for i in range(10):
            c = self.traverse()
            if c:
                break
        scrolls = 5
        while scrolls > 0:
            try:
                scrolls -= 1
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                time.sleep(3)
            except:
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
        
        file  = open("Excelfiles\\" + self.name + " " + self.date + ".csv","w+",encoding="utf8")
        
        filelist.append(self.name + " " + self.date + ".csv")
        while r < len_ratings:
            try:
                while str(names[n].text).find(self.skipname) != -1:
                    d += 1
                    n += 1
                if ratings[r].next_element["aria-label"] == "Rated " + skiprating + " stars out of five stars":
                    val = reviews[re].text.replace(',',';').find('Full Review')
                    if val == -1:
                        review_text = reviews[re].text.replace(',',';')
                    else:
                        review_text = reviews[re].text.replace(',',';').split('Full Review')[1]
                    review_text = deEmojify(review_text)
                    file.write(",".join([names[n].text, ratings[r].next_element["aria-label"], dates[d].text, review_text, "\n"]))
                    file.flush()

            except Exception as e:
                print("------------- Error ------------------- ")
                print(e)
                print("------------- Error ------------------- ")

            r += 1
            d += 1
            n += 1
            re += 1
        file.close()
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    f = open(filename, "r")
    while True:
        url = f.readline()
        if not url:
            break
        date = f.readline()
        try:
            print("---------------------" + url + "----------------------------")
            P = PlayStore(url, date)
            P.get_data()
        except Exception as e:
            print(e)
        print(filelist)
    print(filelist)
    # P = PlayStore("https://play.google.com/store/apps/details?id=in.co.qwikly", "")
    # P.get_data()

