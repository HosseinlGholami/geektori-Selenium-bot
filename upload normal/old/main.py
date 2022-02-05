import os
from selenium import webdriver
from functools import reduce

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

Worked_path=os.getcwd()
Content=os.listdir()


category_name ={"سفید":3255,"شفاف":3255}


CONFIRM_XPATH="/html/body/div/div/div[5]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]"


internet_speed=1
def get_page_link(x):
    return f"https://geektori.ir/admin/products?page={x}"

def return_product_xpath(x):
             
    return f"/html/body/div/div/div[5]/div/div[2]/div[1]/div/div[1]/div[{x}]"
def return_product_xpath_Edit(x):
    return f"/html/body/div/div/div[5]/div/div[2]/div[1]/div/div[1]/div[{x}]/div/div[4]/div[1]/div[1]"

def retuen_feature_xpath(x):
    return f"""//*[@id="tab-3"]/div/div[1]/div[1]/div[2]/div[{x}]/div/div[7]/div/div/input"""
def retuen_price_xpath(x):
    return f"""/html/body/div/div/div[5]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{x}]/div/div[4]/div"""

price_tag_Xpath="/html/body/div/div/div[5]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/ul/div[3]"

featuer_input_xpath="//*[@id=\"newColumn\"]"
# Confirm_feature_type="//*[@id=\"tab-3\"]/div/div[3]/div/div/div/div/div[2]/div[2]"
add_variety_xpath="//*[@id=\"productTableAddRow\"]"

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
               
def add_new_category_on_one_product(driver,i,category_name):
    driver.implicitly_wait(10)
    x=WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,return_product_xpath(i)))
            )
    action=ActionChains(driver)
    action.move_to_element(x)
    action.perform()
    
    time.sleep(internet_speed)
    
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,return_product_xpath_Edit(i)))
            ).click()
    time.sleep(internet_speed)
    
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,price_tag_Xpath))
            ).click() 
    
    


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
    time.sleep(2)
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,"""//*[@id="simple"]"""))
    ).click()
    time.sleep(2)
    NameBar=WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"""/html/body/div/div/div[5]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/input"""))
        )
    time.sleep(internet_speed)
    NameBar.send_keys("استیکر "+name)
    
    time.sleep(2)
    PicBar=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"""//*[@id="productImages"]/div[1]/input"""))
    )
    time.sleep(internet_speed)
    PicBar.send_keys(PicPath)
    time.sleep(4)
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"""//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/ul/div[2]"""))
    ).click()
    time.sleep(2)
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
    time.sleep(2)
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"""//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/ul/div[3]"""))
    ).click()
    time.sleep(2)
    #click on new feautre tab
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,"""//*[@id="tab-3"]/div/div[1]/div[1]/div[1]/div/div[7]/div[1]"""))
            ).click() 
    
    InputPrice=WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,featuer_input_xpath))
            )
    InputPrice.clear()
    time.sleep(internet_speed)
    InputPrice.send_keys("جنس محصول")
    InputPrice.send_keys(Keys.RETURN)

    
    time.sleep(internet_speed)
    
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,add_variety_xpath))
            ).click()
    
    time.sleep(internet_speed)
    
    for i,feature in enumerate(category_name):
        InputPrice=WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,retuen_feature_xpath(i+1)))
            )
        time.sleep(internet_speed)
        InputPrice.send_keys(feature)
        InputPrice.send_keys(Keys.RETURN)
        
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
    Worked_path=os.getcwd()
    Content=os.listdir()
    
    names=[name for name in Content if name.split('.')[-1]=='png']
    category = Worked_path.split('\\')[-1]

    driver = webdriver.Chrome('./chromedriver.exe')
    init(driver)
    time.sleep(10)
    for name in names:
        picPath=Worked_path+'\\'+name
        Name=reduce(lambda x,y: x+y,name.split('.')[0:-1])
        add_new_product(driver,Name,picPath,category)
        time.sleep(10)
    driver.quit()

    