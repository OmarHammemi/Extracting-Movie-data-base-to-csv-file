#Library
from selenium import webdriver
from bs4 import BeautifulSoup 
import time
import os
import pandas as pd
import requests

if not os.path.exists('Movie_Picture'):
    os.makedirs('Movie_Picture')
driver = webdriver.Chrome(r'/home/omar/chromedriver')
driver.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
trs=soup.find_all('tr')
print(len(trs))
for tr in trs:
    for td in tr.find_all('td',class_="posterColumn"):
        a=td.find('a')
        img=a.find('img')
        n=img['alt']
        print(img['src'],'\n')
        f=open('Movie_Picture/{0}.jpg'.format(n),'wb')
        f.write(requests.get(img['src']).content)
        f.close()
    