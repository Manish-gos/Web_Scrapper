import requests
from bs4 import BeautifulSoup
root="https://subslikescript.com/"
path='BeautifulSoup/data/'
website=f'{root}movies'
result=requests.get(website)
content=result.text
#print(content)
soup=BeautifulSoup(content,'lxml')
#print(soup.prettify())
box=soup.find('article',class_='main-article')
#print(box)
movies=box.find_all('a',href=True)
#print(movies[0]['href'])
lst=list()
for movie in movies:
    lst.append(movie['href'])
    

for mv in lst:
    try:
        website=f'{root}{mv}'
        result=requests.get(website).text
        soup=BeautifulSoup(result,'lxml')
        box=soup.find('article',class_='main-article')
        title=box.find('h1',class_="").get_text()
        script=box.find('div',class_="full-script").get_text(strip=True,separator=" ")
        with open(f"{path}{title}.txt",'w') as file:
            file.write(script)
    except:
        print("------link is not valid--------")   
        print(website) 