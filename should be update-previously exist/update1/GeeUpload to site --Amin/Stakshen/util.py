import time
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
internet_speed=0.6


add_product_Xpath='//*[@id="addProduct"]'
phisical_product_Xpath='//*[@id="root"]/div/div[4]/div/div[2]/div[4]/div/div/div/div/div/div[2]'
name_bar_xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div/input'
pic_bar_xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[1]/div/div/div[3]/div/div[1]/input'
s2_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/ul/div[2]'
listCategory_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/div/div/div[1]/div/div[1]'
pricePage_xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/ul/div[3]'
price_xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[3]'
inputPrice_Xpath='//*[@id="price"]'

done_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]'
    
    
def CategoryTextXpath(x):
    return '//*[@id="productCategory"]/div[2]/div['+str(x)+']/div/label'
def CategoryElXpath(x):
    return '//*[@id="productCategory"]/div[2]/div['+str(x)+']'

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


def search_inside_category(driver,category):
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,listCategory_Xpath))
        ).click()
    time.sleep(internet_speed)
    Sticker=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,CategoryTextXpath(1)))).text
    if (Sticker=='استیکر'):
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,CategoryElXpath(1)))).click()
    time.sleep(internet_speed)
    #condition
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
      
def add_new_product(driver,name,PicPath,category,price):
    #open new product
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,add_product_Xpath))
            ).click()
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,phisical_product_Xpath))
        ).click()
    time.sleep(internet_speed)
    #full form s1-name
    NameBar=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,name_bar_xpath))
        )
    time.sleep(internet_speed)
    NameBar.send_keys(name)
    #full form s1-picture
    PicBar=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,pic_bar_xpath))
        )
    time.sleep(internet_speed)
    PicBar.send_keys(PicPath)
    time.sleep(1)
    #swith s2
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,s2_Xpath))
        ).click()
    time.sleep(internet_speed)
    #search indise category list and mark it
    try:
        search_inside_category(driver,category)
    except:
        DT=datetime.now().strftime('%Y-%m-%d-%m--%H\'%M')
        f = open("Readme"+str(DT)+".txt", "a")
        f.write("We dont found catgory you choose \n please clone correctry from site and change the folder name")
        f.close()
        driver.quit()
        raise Exception("Category not found check readme file which just now created")
    time.sleep(internet_speed)
    #switch s3 and change price
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,pricePage_xpath))
        ).click()
    time.sleep(internet_speed)    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,price_xpath))
        ).click()
    time.sleep(internet_speed)    
    inputPrice=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,inputPrice_Xpath))
        )
    inputPrice.send_keys(price)
    inputPrice.send_keys(Keys.RETURN)
    time.sleep(internet_speed)    
    #done
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,done_Xpath))
        ).click()
    
    
    
