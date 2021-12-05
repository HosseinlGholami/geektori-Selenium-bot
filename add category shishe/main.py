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

category_name ={"شفاف":2995,"سفید":3255}
total_page=264
start_page=8

CONFIRM_XPATH="/html/body/div/div/div[5]/div/div[2]/div[2]/div/div/div/div/div[2]/div[3]"#its cancel Xpath and should be change with "/html/body/div/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[2]/div[3]"


internet_speed=1
def get_page_link(x):
    return f"https://geektori.ir/admin/products?page={x}"

def return_product_xpath(x):
             
    return f"/html/body/div/div/div[5]/div/div[2]/div[1]/div/div[1]/div[{x}]"
def return_product_xpath_Edit(x):
    return f"/html/body/div/div/div[5]/div/div[2]/div[1]/div/div[1]/div[{x}]/div/div[4]/div[1]/div[1]"
def retuen_feature_xpath(x):
    return f"""//*[@id="tab-3"]/div/div[1]/div[1]/div[2]/div[{x}]/div/div[8]/div/div/input"""

def retuen_price_xpath(x):
    return f"/html/body/div/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[{x}]/div/div[4]"

price_tag_Xpath="/html/body/div/div/div[5]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/ul/div[3]"
price_tag_new_feature_Xpath="/html/body/div/div/div[5]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[8]/div[1]/div/span"
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
            EC.element_to_be_clickable((By.XPATH,"""//*[@id="productTablePrice"]"""))#retuen_price_xpath(i+1)))
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
    
    
def active_sticker_fileld():
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"""//*[@id="filter-2"] """))
        ).click()
    time.sleep(1)    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"""//*[@id="filter-2"]/div/div[2]/div[1]"""))
        ).click()        
    time.sleep(1)
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,"""//*[@id="filter-2"] """))
    ).click()
    time.sleep(3)

def active_moojood_fileld():
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"""//*[@id="filter-1"] """))
        ).click()
    time.sleep(1)    
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"""//*[@id="filter-1"]/div/div[2]/div[3]"""))
        ).click()        
    time.sleep(1)
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,"""//*[@id="filter-1"] """))
    ).click()
    time.sleep(3)

def run_this_shit_on_one_page(page):
    for i in range(1,21):
        try:
            add_new_category_on_one_product(driver,i,category_name)
            time.sleep(1)    
        except:
            try:
                print( page,"---",i)
                WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH,"""//*[@id="root"]/div/div[5]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]"""))
                ).click()
                time.sleep(3)    
            except:
                pass
            

def go_fucking_next_page():
    WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,"""/html/body/div/div/div[5]/div/div[2]/div[1]/div/div[2]/div/div[3]/div"""))
    ).click()
    time.sleep(5)

def go_to_page(page):
    InputPrice=WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,'''/html/body/div/div/div[5]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/input'''))
        )
    time.sleep(internet_speed)
    InputPrice.send_keys(Keys.CONTROL + "a")
    InputPrice.send_keys(page)
    InputPrice.send_keys(Keys.RETURN)


if __name__ == "__main__":
    driver = webdriver.Chrome('./chromedriver.exe')
    init(driver)
    time.sleep(10)
    active_sticker_fileld()
    time.sleep(10)
    active_moojood_fileld()
    go_to_page(start_page)
    time.sleep(10)
    
    for page in [84,130,184,188,228,230,233,234,235]:#range(start_page,total_page):
        run_this_shit_on_one_page(page)
        go_to_page(page+1)
        # go_fucking_next_page()
        
    print("end")
    time.sleep(3)
    driver.quit()
