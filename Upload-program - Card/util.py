import time
import  os
from datetime import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
internet_speed=1


add_product_Xpath='/html/body/div[1]/div/div[4]/div/div[1]/div[1]/div[1]/div[2]/div[3]'

phisical_product_Xpath='//*[@id="root"]/div/div[4]/div/div[2]/div[5]/div/div/div/div/div/div[2]'
name_bar_xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div/input'
pic_bar_xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[1]/div/div/div[3]/div/div[1]/input'
s2_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/ul/div[2]'
listCategory_Xpath='//*[@id="productCategory"]/div[1]/div[2]'
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

def feature_Xpath_name(i):
    return f"/html/body/div/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{i}]/div/div[6]/div/div/input"
            

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
    time.sleep(internet_speed)
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH,s2_Xpath))
    #     ).click()
    time.sleep(internet_speed)
      
def add_new_product(driver,name,PicPath,category,price):
    time.sleep(5)
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
    NameBar.send_keys("استیکر "+name)

    #add template
    temp_PicPath=''.join(str(e)+'\\' for e in PicPath.split('\\')[:-1])
    name_PicPath=PicPath.split('\\')[-1]
    PicBar=WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,pic_bar_xpath))
            )
    #full form s1-picture
    time.sleep(internet_speed)
    PicBar.send_keys(PicPath)
    time.sleep(10)
    
    
    # add sade
    time.sleep(internet_speed)
    print(temp_PicPath+'sade\\'+name_PicPath)
    PicBar.send_keys(temp_PicPath+'sade\\'+name_PicPath)
    time.sleep(10)
    
    for i in range(1,6):
        time.sleep(internet_speed)
        print(temp_PicPath+'template\\'+str(i)+'.png')
        PicBar.send_keys(os.path.abspath(temp_PicPath+'template\\'+str(i)+'.png'))
        time.sleep(internet_speed)
        time.sleep(5)
    
    

    #swith s2
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,s2_Xpath))
        ).click()
    time.sleep(internet_speed)
    #search indise category list and mark it
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,listCategory_Xpath))
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
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,s2_Xpath))
        ).click()
    
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
    #add new feature click
    add_fetaure_Xpath='/html/body/div/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[6]/div[1]/div'
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,add_fetaure_Xpath))
        ).click()
    #fill the feature title
    new_fetaure_title_Xpath='/html/body/div/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div[3]/div/div/div[3]/div/div/div/div/div[1]/div[2]/input'
    time.sleep(internet_speed)    
    inputFeatuteTitle=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,new_fetaure_title_Xpath))
        )
    inputFeatuteTitle.send_keys("نوع برش")
    inputFeatuteTitle.send_keys(Keys.RETURN)
    time.sleep(internet_speed)
    cr_fr_Xpath="/html/body/div/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div[3]/div/div/div[2]"
    for i in range(5):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,cr_fr_Xpath))
            ).click()
    #complete the feature
    feature_list=["simple","A","B","C","D","E"]
    for i,feature_name in enumerate(feature_list):
        temp_feature=WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,feature_Xpath_name(i+1)))
            )
        temp_feature.send_keys(feature_name)
        temp_feature.send_keys(Keys.RETURN)
    
    #done
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,done_Xpath))
        ).click()
    
    
    
