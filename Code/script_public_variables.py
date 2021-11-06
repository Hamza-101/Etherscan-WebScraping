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
import re

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By


ga=pandas.read_csv("adresses.csv")
file= open('script_public_variables.csv', 'a')
writer = csv.writer(file)

for i in range (ga.size-1):
        
        fj=ga.iloc[i][0]
        print(fj)
        print(i)
        driver = webdriver.Firefox()
        url="https://etherscan.io/token/"+str(fj)+"#readContract"


#driver = webdriver.Chrome()
        
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

        ha=[]
        num=len(sik)
        print(i)
        
        for i in range(1,(num+1)):
            print('---', i, '---')
            
            fd=(driver.find_element_by_id(f"readHeading{i}").text)
            fd = re.sub("[0-9]", "",fd)
            
            
            c=(driver.find_element_by_id(f"readCollapse{i}").text)
            print(c)
            if(c.find('Query') == -1):
                data=[fj,fd,c,val]
                print(data)
                # fd.replace(",", "")
                # c.replace(",","")
                writer.writerow(data)        

        print(fd)
        print(c)
 
        
        driver.close()
