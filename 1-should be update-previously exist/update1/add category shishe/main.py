import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

Worked_path=os.getcwd()
Content=os.listdir()

category_name ={"شفاف":2995,"شیشه ای":3100}

CONFIRM_XPATH="/html/body/div/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]"#its cancel Xpath and should be change with "/html/body/div/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[2]/div[3]"

internet_speed=1
def get_page_link(x):
    return f"https://geektori.ir/admin/products?page={x}"

def return_product_xpath(x):
    return f"/html/body/div/div/div[4]/div/div[2]/div[1]/div/div[1]/div[{x}]"
def return_product_xpath_Edit(x):
    return f"/html/body/div/div/div[4]/div/div[2]/div[1]/div/div[1]/div[{x}]/div/div[4]/div[1]/div[1]"
def retuen_feature_xpath(x):
    return f"//*[@id=\"tab-3\"]/div/div[1]/div[1]/div[2]/div[{x}]/div/div[8]/div/div/input"
def retuen_price_xpath(x):
    return f"/html/body/div/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{x}]/div/div[4]"
price_tag_Xpath="//*[@id=\"root\"]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/ul/div[3]"
price_tag_new_feature_Xpath="//*[@id=\"tab-3\"]/div/div[1]/div[1]/div[1]/div/div[8]/div[1]"
featuer_input_xpath="//*[@id=\"newColumn\"]"
Confirm_feature_type="//*[@id=\"tab-3\"]/div/div[3]/div/div/div/div/div[2]/div[2]"
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
    driver.implicitly_wait(30)
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
    
    time.sleep(internet_speed)

    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,price_tag_new_feature_Xpath))
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
            EC.element_to_be_clickable((By.XPATH,retuen_price_xpath(i+1)))
            ).click()
        
        InputPrice=WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//*[@id=\"price\"]"))
        )
        time.sleep(internet_speed)
        
        InputPrice.send_keys(str(category_name[feature]))
        InputPrice.send_keys(Keys.RETURN)
    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,CONFIRM_XPATH))
        ).click()    
    
    
def apply_on_one_page(driver,page):
    driver.get(get_page_link(page))
    time.sleep(10)
    for i in range(1,2):
        try:
            add_new_category_on_one_product(driver,i,category_name)
        except:
            driver.navigate().refresh();
            time.sleep(10)
            add_new_category_on_one_product(driver,i,category_name)
            
if __name__ == "__main__":
    driver = webdriver.Chrome('./chromedriver.exe')
    init(driver)
    time.sleep(10)
    apply_on_one_page(driver,2)
    
    time.sleep(50)
    driver.quit()