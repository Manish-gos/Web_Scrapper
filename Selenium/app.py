from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import Select
import time
website="https://www.adamchoi.co.uk/overs/detailed"
path="/config/workspace/Selenium/chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get(website)
clickButton=driver.find_element_by_xpath("//label[@analytics-event='All matches']")
clickButton.click()
dropdown=Select(driver.find_element_by_id("country"))
dropdown.select_by_visible_text("Spain")
time.sleep(3)
matches=driver.find_elements_by_tag_name("tr")
date=[]
home_team=[]
score=[]
away_team=[]
for match in matches:
    date.append(match.find_element_by_xpath("./td[1]").text)
    home=match.find_element_by_xpath("./td[2]").text
    #print(home)
    home_team.append(home)
    score.append(match.find_element_by_xpath("./td[3]").text)
    away_team.append(match.find_element_by_xpath("./td[4]").text)
driver.quit()
df=pd.DataFrame({"date":date,"home_team":home_team,"score":score,"away_team":away_team})
df.info()
df.to_csv("footbal.csv",index=False)