from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests

start_page=17
end_page=91

driver=webdriver.Chrome("./chromedriver.exe")

def linke_of_page(x):
    return 'https://juststickers.in/product-type/stickers/page/'+str(x)+'/'

def download_pic(name,link):
    driver.get('https:'+link)
    time.sleep(0.1)
    src=driver.find_element_by_xpath('/html/body/img').get_attribute('src')
    response = requests.get(src)
    with open('.//picture//'+name+'.png', 'wb') as file:
        file.write(response.content)
        file.close()
    
def download_pic1(name,link):
    driver.get('https:'+link)
    time.sleep(0.1)
    with open('.//pic//'+name+'.png', 'wb') as file:
        file.write(driver.find_element_by_xpath('/html/body/img').screenshot_as_png)

def get_link(yatri):
    x1=yatri.find('srcset')
    x2=yatri.find('528w')
    y=yatri[x1:x2].split(',')[-1].strip()
    name=y.split('/')[-1].split('.')[0].replace('-',' ')
    return name,y

def link_of_item(x):
    return '/html/body/section/div[2]/div[1]/div['+str(x)+']'

def scrab_item(page,item):
    #go to just sticker page
    driver.get(linke_of_page(page))
    #export links 
    y=WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,link_of_item(item)))
                )
    html_detail=y.get_attribute('innerHTML')
    name,link=get_link(html_detail)
    download_pic(name,link)
    
for page in range(start_page,end_page):
    for item in range(1,15):
        try:
            scrab_item(page,item)
        except:
            pass
        time.sleep(0.3)

driver.quit()

