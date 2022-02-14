from selenium import webdriver
from bs4 import BeautifulSoup 
import requests
import os
import time 


class Player():
    def __init__(self):
        self.name=''
        self.link=''
        # self.name=''
def get_player_list():
         driver = webdriver.Chrome(r'/home/omar/chromedriver')
         players=[]
         driver.get('http://stats.nba.com/players/?ls=iref:nba:gnav')
         html_doc=driver.page_source
         soup=BeautifulSoup(html_doc,'lxml')
         # for tr  in soup.find_all('tr'):  
         #     for td in soup.find_all('td'):
         #         print(td.text)
         #tags_a=soup.find_all('a')
         div = soup.find('div',class_='category-body')
         for a in div.find_all('a'):
             #print('Playernamne : ',a.text,'\n Href : ',a['href'])
             # print('Name :',a.text)
             # print('hreference :' ,'https://www.nba.com'+a['href'])
             new_player=Player()
             new_player.name=a.text
             new_player.link='https://www.nba.com'+a['href']    
             players.append(new_player)
         return players       
        
def get_player_image(players):
        driver = webdriver.Chrome(r'/home/omar/chromedriver')
        if not os.path.exists('NBA_Player'):
            os.makedirs('NBA_Player')
        for p in players:
                url=p.link
                driver.get(url) 
                # time.sleep(2)
                html_doc=driver.page_source
                soup=BeautifulSoup(html_doc,'lxml')
                div=soup.find('div',class_ ="summary-player__logo" )
                img=div.find('img')
                print(img['src'])
                f=open('NBA_Player/{0}.jpg'.format(p.name),'wb')
                f.write(requests.get(img['src']).content)
                f.close()
        driver.quit()
        return players
 
players= get_player_image(get_player_list())
