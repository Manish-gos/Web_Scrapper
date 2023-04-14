import requests
from bs4 import BeautifulSoup
root="https://subslikescript.com/"
path='BeautifulSoup/data/'
website=f'{root}movies'
result=requests.get(website)
content=result.text
#print(content)
soup=BeautifulSoup(content,'lxml')
#pagination
pagination=soup.find('ul',class_='pagination')
pages=pagination.find_all('li',class_='page-item')
last_page=pages[-2].text
print(last_page)
for page in range(1,int(last_page)+1):
    website=f'{root}movies?page={page}'
    print(website)
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
            web=f'{root}{mv}'
            result=requests.get(web).text
            soup=BeautifulSoup(result,'lxml')
            box=soup.find('article',class_='main-article')
            title=box.find('h1',class_="").get_text()
            script=box.find('div',class_="full-script").get_text(strip=True,separator=" ")
            with open(f"{path}{title}.txt",'w') as file:
                file.write(script)
        except:
            print("------link is not valid--------")   
            print(web) 