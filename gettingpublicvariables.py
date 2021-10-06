
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import string
from csv import reader
import code
import pandas

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
driver = webdriver.Firefox()


values="/0"
ga=pandas.read_csv("contracts/adresses.csv")
for i in range (ga.size-1):
        fj=ga.iloc[i][0]
        # driver.get("https://etherscan.io/address/"+str(fj))
        break
        

time.sleep(5)
      
driver.get("https://etherscan.io/token/0xB8c77482e45F1F44dE1745F52C74426C631bDD52#readContract")

wait = WebDriverWait(driver,30)

frame = wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID,"readcontractiframe")))

expandall = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@onclick='expandCollapseAll()']")))
expandall.click()
time.sleep(10)
d=[]
sd=[]

sik=driver.find_elements_by_css_selector("div.card.shadow-none.mb-3")
num=len(sik)
print(num)

for i in range(1,(num+1)):
        try:
            print('---', i, '---')
            d.append(driver.find_element_by_id(f"readHeading{i}").text)
            sd.append(driver.find_element_by_id(f"readCollapse{i}").text)
        except:
            print("Elements finished")
            break
        





    # driver.get("https://etherscan.io/token/"+str(fj)+"#balances")
    # driver.find_element_by_id("ContentPlaceHolder1_tabHolders")
    # print("dfsjkdfn")
    # while(True):
    #         if((driver.find_element("", "")).is_enabled()==True):
    #             driver.find_element("xpath", "/html/body/div[2]/div[3]/table").getText()
    #             driver.find_element("xpath", "/html/body/div[2]/div[3]/div/div/ul/li[4]/a").click()
    #         else:
    #             break
    #         driver.find_element("xpath", "/html/body/div[2]/div[3]/table").getText()

