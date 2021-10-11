
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import string
from csv import reader,writer
import code
import pandas

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By


ga=pandas.read_csv("adresses.csv")

for i in range (ga.size-1):
        
        fj=ga.iloc[i+1][0]
        print(fj)
        driver = webdriver.Firefox()
        url="https://etherscan.io/token/"+str(fj)+"#readContract"



        driver.get(url)

        time.sleep(5)  # JavaScript needs time to add elements on page

        frame = driver.find_element_by_id('readcontractiframe')
        driver.switch_to.frame(frame)

        driver.find_element_by_xpath('//a[text()="[Expand all]"]').click()
        time.sleep(0.5)  # JavaScript needs time to expand all

        sik=driver.find_elements_by_css_selector("div.card.shadow-none.mb-3")
        
        driver1=webdriver.Firefox()
        driver1.get("https://etherscan.io")
        wait = WebDriverWait(driver1,5)
        key=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/main/div/div[3]/div[1]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[2]/a")))
        val=key.text
        print(val)
        driver1.close()

        fd=[]
        c=[]

        num=len(sik)
        for i in range(1,(num+1)):
            print('---', i, '---')
            fd.append(driver.find_element_by_id(f"readHeading{i}").text)
            c.append(driver.find_element_by_id(f"readCollapse{i}").text)
            

        print(fd)
        print(c)
        
        file= open('scraping.csv', 'a')


        writer = csv.writer(file)
        writer.writerow(val)
        writer.writerow(fd) 
        writer.writerow(c) 
        writer.writerow("\n")
        file.close()
        driver.close()
