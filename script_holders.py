
from datetime import datetime
from functools import total_ordering
from pandas.core.base import DataError
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
from datetime import datetime

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By



ga=pandas.read_csv("adres.csv")
d=[]
file= open('script_holders.csv', 'a')
for i in range((ga.size-1)):
    driver=webdriver.Firefox()
    fj=ga.iloc[i][0]
    print("jfnd")
    print(i)
    print("jfnd")
    wait1 = WebDriverWait(driver, 5)
    driver.get("https://etherscan.io/token/0x3146f5df6b081bda369b61d85f33bb517e62da53#balances")
    wait = WebDriverWait(driver, 20)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "tokeholdersiframe")))
    get = wait1.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div[3]/table/tbody/tr[1]/td/div"))).text
    timen = datetime.now()
    dt_string= timen.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string)
    if (str(get)!="There are no matching entries"):
        # d.append(str(fj))
        # d.append("")
        num = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(@class,'page-link text-nowrap')]/strong)[2]")))
        val=int(num.get_attribute('innerText'))
        print(val)
        print(i)
        print("sdjkbfkjsd") 
        writer = csv.writer(file)
        writer.writerow(fj)
        writer.writerow(dt_string)

        for i in range(val):  
                        num = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(@class,'page-link text-nowrap')]/strong)[1]")))
                        value=int(num.get_attribute('innerText'))
                        print(value)
                        print(i)    
                        print("udj")
                        # simpleTable = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/table")
                        rows = driver.find_elements(By.TAG_NAME,"tr")
                        for i in range(1,len(rows)):
                                cols = rows[i].find_elements(By.TAG_NAME,"td")
                                for g in cols:
                                        d.append(g.text)
                                        
                        
                        
                        print(d)
                        if((val!=value)):
                            next = wait1.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='d-inline-block']//a[@aria-label='Next']")))
                            driver.execute_script("arguments[0].scrollIntoView(true);",next)
                            driver.execute_script("window.scrollBy(0,-200);")
                            next.click() 
                        else:
                            writer.writerow(d)
                            
                            writer.writerow("\n")
                            break
                              
    driver.close()
    break
   

    
    

file.close()
