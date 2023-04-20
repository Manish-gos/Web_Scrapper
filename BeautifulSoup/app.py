import requests
from bs4 import BeautifulSoup
website="https://subslikescript.com/movie/Titanic-120338"
path='BeautifulSoup/data/'
result=requests.get(website)
contetnt=result.text
#print(contetnt)
soup=BeautifulSoup(contetnt,'lxml')
#print(soup.prettify())
box=soup.find('article',class_='main-article')
#print(box)
title=box.find('h1',class_="").get_text()
#print(title)
script=box.find('div',class_="full-script").get_text()
#print(script)
box=soup.find("article",class_='main-article')
#print (box)
title=box.find('h1').get_text()
#print(title)
script=box.find('div',class_='full-script').get_text(strip=True,separator=" ")
#print(script)
with open(f"{path}{title}.txt",'w') as file:
    file.write()