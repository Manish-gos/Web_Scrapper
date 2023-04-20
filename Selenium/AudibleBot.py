from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.options import Options
import time
path="/config/workspace/Selenium/chromedriver.exe"

# option code is to avoid home popup windows
options=Options()
# change value to false when you dont want the it 
options.headless=False#True
#options.add_argument("window-size=1920x1080")

website="https://www.audible.in/search"
#with out headless
#driver=webdriver.Chrome(path)
#with headless
driver=webdriver.Chrome(path,options=options)
driver.get(website)
driver.maximize_window()


#Pagination 
pagination=driver.find_element_by_xpath('//ul[contains(@class,"pagingElements")]')
pages=pagination.find_elements_by_tag_name("li")
last_page=int(pages[-2].text)
page_no=1
#print(products[0])
title=[]
auhor=[]
narrator=[]
length=[]
ratings=[]
while page_no<=last_page:
    time.sleep(2)
    container=driver.find_element_by_class_name("adbl-impression-container ")
    products=container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')
    for product in products:
        title.append(product.find_element_by_xpath(".//h3[contains(@class,'bc-heading')]").text)
        auhor.append(product.find_element_by_xpath(".//li[contains(@class,'authorLabel')]").text[11:])
        narrator.append(product.find_element_by_xpath(".//li[contains(@class,'narratorLabel')]").text[12:])
        length.append(product.find_element_by_xpath(".//li[contains(@class,'runtimeLabel')]").text[7:])
        ratings.append(product.find_element_by_xpath(".//li[contains(@class,'ratingsLabel')]").text.split("\n")[0])
    page_no+=1
    try:
        next_page=driver.find_element_by_xpath('//span[contains(@class,"nextButton ")]')
        next_page.click()
    except:
        print('page not found')
        pass
driver.quit()
df=pd.DataFrame({"Book Name":title,
             "Author Name":auhor,
             "Narrator Name":narrator,
              "Book Size":length,
              "Book Ratings":ratings
             })
df.head(20)
df.to_csv("bookslistpagination.csv",index=False)
print("Task completed")
