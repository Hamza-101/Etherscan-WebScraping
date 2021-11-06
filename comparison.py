import csv
import pandas
from csv import reader,writer

ga=pandas.read_csv("adres.csv")
i=0
for i in range (ga.size):
    nui=0
    Aso=0
    with open('script_holders.csv','r') as js:
        print(ga.iloc[i][0])
        for line in js:
            if(str(line).find(ga.iloc[i][0])!=-1):
                Aso=line.count(ga.iloc[i][0])
    if(Aso!=0):
        Aso=Aso-1

    print(Aso)
    with open('results.csv','r') as resul:
        for line in resul:
            if(str(line).find(ga.iloc[i][0])!=-1):
                nui=nui+1
    print(nui)
    aas = open('fh.csv','a')
    rj = csv.writer(aas)
    rj.writerow(ga.iloc[i][0])
 
    if(Aso>nui):
            rj.writerow("unmatch")
    if(nui>Aso):
            rj.writerow("exceed")
    if(nui==Aso):
            rj.writerow("match")
    aas.close()
    i=i+1
  

        
