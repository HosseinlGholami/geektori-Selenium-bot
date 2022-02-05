import os
from selenium import webdriver
from functools import reduce
# from selenium import webdriver
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

Worked_path=os.getcwd()
Content=os.listdir()


category_name ={"سفید":3255,"شفاف":3255}


CONFIRM_XPATH="/html/body/div/div/div[5]/div/div[3]/div/div/div/div/div[2]/div[2]"


internet_speed=2

def get_page_link(x):
    return f"https://geektori.ir/admin/products?page={x}"


def retuen_feature_xpath(x):
    return f"""/html/body/div/div/div[5]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{x}]/div/div[7]/div/div/input"""

def retuen_price_xpath(x):
    return f"""/html/body/div/div/div[5]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{x}]/div/div[4]/div"""


def init(driver):
    driver.get('https://geektori.ir/admin/products')
    #loginPart
    INPUT_MAIL="farzam.mirmoeini@gmail.com"           
    PASS="AHAFA12345"
    InputMail=driver.find_element_by_id("username")
    InputMail.send_keys(INPUT_MAIL)
    InputPass=driver.find_element_by_id("password")
    InputPass.send_keys(PASS)
    InputPass.send_keys(Keys.RETURN)
                   


def CategoryTextXpath(x):
    return '//*[@id="productCategory"]/div[2]/div['+str(x)+']/div/label'
def CategoryElXpath(x):
    return '//*[@id="productCategory"]/div[2]/div['+str(x)+']'      
      
def search_inside_category(driver,category):
    time.sleep(internet_speed)    
    stop=False
    i=1
    while(stop==False):
        Ctg=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,CategoryTextXpath(i)))).text    
        if (Ctg==category):
            WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,CategoryElXpath(i))
                                           )).click()
            stop=True
        else:
            i=i+1
    time.sleep(internet_speed*2)
           

def add_new_product(driver,name,PicPath,category):
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,"""//*[@id="addProduct"]"""))
    ).click()
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,"""//*[@id="simple"]"""))
    ).click()
    
    NameBar=WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"""/html/body/div/div/div[5]/div/div[3]/div/div/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/input"""))
        )
    time.sleep(internet_speed)
    NameBar.send_keys("استیکر "+name)
    
    time.sleep(internet_speed)
    PicBar=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"""//*[@id="productImages"]/div[1]/input"""))
    )
    time.sleep(internet_speed)
    PicBar.send_keys(PicPath)
    time.sleep(internet_speed*2)
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"""/html/body/div/div/div[5]/div/div[3]/div/div/div/div/div[1]/div[1]/ul/div[2]"""))
    ).click()
    time.sleep(internet_speed)
    #press category option
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"""//*[@id="productCategory"]"""))
        ).click()
    try:
        for cat in category.split(',')+["استیکر"]:
            search_inside_category(driver,cat)
    except:
        DT=datetime.now().strftime('%Y-%m-%d-%m--%H\'%M')
        f = open("Readme"+str(DT)+".txt", "a")
        f.write("We dont found catgory you choose \n please clone correctry from site and change the folder name")
        f.close()
        driver.quit()
        raise Exception("Category not found check readme file which just now created")
    
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"""/html/body/div/div/div[5]/div/div[3]/div/div/div/div/div[1]/div[1]/ul/div[3]"""))
    ).click()
    time.sleep(internet_speed)
    
    #create new feature
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"""//*[@id="productTableAddCol"]"""))
            ).click() 
    time.sleep(internet_speed)
    #config the new category
    InputPrice=WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        """//*[@id="newColumn"]"""
                                        ))
            )
    InputPrice.clear()
    time.sleep(internet_speed)
    InputPrice.send_keys("جنس محصول")
    InputPrice.send_keys(Keys.RETURN)
    #end config the new category
    
    time.sleep(internet_speed)
    #add new product
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        """//*[@id="productTableAddRow"]"""
                                        ))
            ).click()
    #end add new product
    time.sleep(internet_speed)
    
    for i,feature in enumerate(category_name):
        #click on the price
        InputPrice=WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,retuen_feature_xpath(i+1)))
            )
        time.sleep(internet_speed)
        InputPrice.send_keys(feature)
        InputPrice.send_keys(Keys.RETURN)
        #end add price
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,retuen_price_xpath(i+1)))#retuen_price_xpath(i+1)))
            ).click()
        InputPrice=WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"""//*[@id="price"]"""))
                                   )
        time.sleep(internet_speed)
        InputPrice.send_keys(str(category_name[feature]))
        InputPrice.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,CONFIRM_XPATH))
        ).click()    


if __name__ == "__main__":

    driver = webdriver.Chrome('./chromedriver.exe')
    init(driver)
    Worked_path=os.getcwd()
    All_artist_name=os.listdir()
    time.sleep(10)
    for artist_name in [x for x in All_artist_name if "." not in x]:
        Content=os.listdir(artist_name)
        names=[name for name in Content if name.split('.')[-1]=='png']
        for name in names:
            picPath=Worked_path+'\\'+artist_name+'\\'+name
            print(picPath)    
            Name=reduce(lambda x,y: x+y,name.split('.')[0:-1])
            print(Name)
            add_new_product(driver,Name,picPath,artist_name)
            time.sleep(10)
    driver.quit()

    