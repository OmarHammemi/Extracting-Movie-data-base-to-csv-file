#Library
from selenium import webdriver
from bs4 import BeautifulSoup 
import time
import os
import pandas as pd

#Building File 
if not os.path.exists('Database'):
    os.makedirs('Database')

#Building Class for Extracting movie database
#You can use Class for me I will use regular dictinary
class Movie():
    def __init__(self):
        self.rank=''
        self.year=''
        self.name=''
        self.rate=''
        
        
#Coding
driver = webdriver.Chrome(r'/home/omar/chromedriver')
driver.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
source=soup.find_all('tr')
i=0
l=[]
for tr in source:
    trf=tr.find_all('td',class_="titleColumn")
    trr=tr.find_all('td',class_="ratingColumn imdbRating")
    for tdn , tdr in zip(trf, trr):
            a=tdn.find('a')
            s=tdn.find('span')
            r=tdr.find('strong')
            i+=1
            s1=s.text
            year=s1.split('(')[1][:-1]
            l.append({'Rank':i,'Year':year,'Name':a.text,'Rate':r.text})
            #print('{0} Movie Name and Rate: {1} , {2} '.format(i,a.text,r.text))
            
print('Number of Movies :',len(source))

#Building a DataFrame

df=pd.DataFrame(data=l)
df.to_csv('Database/Movie_Rate.csv')
print(df.head())
driver.quit()