from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import requests

NNAME='Trendy'
end_page=1


def linke_of_page(x,NNAME):
    return f'https://stickerapp.com/custom-stickers/{NNAME}?p={x}/'

def download_pic(name,link,NNAME):
    driver.get(link)
    time.sleep(0.1)
    src=driver.find_element_by_xpath('/html/body/img').get_attribute('src')
    response = requests.get(src)
    with open(f'.//{NNAME}//{name}.png', 'wb') as file:
        file.write(response.content)
        file.close()

def link_of_item(x):
     return f"/html/body/div/div[1]/div[3]/div/div[2]/div[2]/div/div[1]/div[{x}]/div/div[1]/a"

def scrab_item(page,number,first,NNAME):
    #go to just sticker page
    driver.get(linke_of_page(page,NNAME))
    if first:
        WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,'/html/body/div/div[5]/div[2]/a'))
                    ).click()
    
    #go to item page
    time.sleep(0.5)
    WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,link_of_item(number)))
                ).click()
    #get link and name
    link=WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[3]/div/div[2]/div/div[1]/img'))
                ).get_attribute('src')
    name=WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[3]/div/div[2]/div/div[2]/h1'))
                ).text
    #download pic
    download_pic(name,link,NNAME)



first =True
driver=webdriver.Chrome("./chromedriver.exe")
for page in range(1,end_page+1):
    for number in range(1,32):
        try:
            scrab_item(page,number,first,NNAME)
            first=False
        except:
            pass
        time.sleep(0.5)


driver.quit()

