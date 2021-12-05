import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from unidecode import unidecode

internet_speed=1

next_page_Xpath='//*[@id="root"]/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div'


address_Xpath=   '//*[@id="orderModalShippingDetails"]/div[3]/div/div'
mobile_Xpath=    '//*[@id="orderModalShippingDetails"]/div[2]/div[1]/div'
name_Xpath=      '//*[@id="orderModalShippingDetails"]/div[1]/div[1]/div'
postalcode_Xpath='//*[@id="orderModalShippingDetails"]/div[2]/div[2]/div'
joziyat_Xpath='//*[@id="orderModalPaymentDetails"]/div[2]/div[3]/div'



def init(driver):
    driver.get('https://geektori.ir/admin/orders')
    #loginPart
    INPUT_MAIL="farzam.mirmoeini@gmail.com"           
    PASS="AHAFA12345"
    InputMail=driver.find_element_by_id("username")
    InputMail.send_keys(INPUT_MAIL)
    InputPass=driver.find_element_by_id("password")
    InputPass.send_keys(PASS)
    InputPass.send_keys(Keys.RETURN)


def customer_item(x):
    return f"/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div/div[1]/div[{x}]"
def open_consumer(driver,i):
    time.sleep(internet_speed)
    WebDriverWait(driver,internet_speed).until(
            EC.presence_of_element_located((By.XPATH,customer_item(i)))
                ).click()
Filter_X='//*[@id="filter"]'
Entezar_X='//*[@id="filter"]/div/div[2]/div[1]'
def select_active(driver):
    driver.implicitly_wait(10)
    WebDriverWait(driver,internet_speed).until(
                EC.presence_of_element_located(
                    (By.XPATH,Filter_X)
                    )).click()
    driver.implicitly_wait(10)
    WebDriverWait(driver,internet_speed).until(
            EC.presence_of_element_located(
                (By.XPATH,Entezar_X)
                )).click()
    driver.implicitly_wait(10)
    WebDriverWait(driver,internet_speed).until(
                EC.presence_of_element_located(
                    (By.XPATH,Filter_X)
                    )).click()
    driver.implicitly_wait(10)


close_consumer_Xpath='//*[@id="root"]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]'
def close_consumer(driver):
    driver.find_element_by_xpath(close_consumer_Xpath).click()  
    
order_Xpath='//*[@id="orderModalDetails"]/div[1]/div[2]'
joziyat='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/ul/div[2]'
def export_name_of_product(x):
    return f"/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div[{x}]/div[1]/h3/a"
def scrab_details(driver):
    driver.implicitly_wait(10)
    order=WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,order_Xpath))
            ).text
    driver.implicitly_wait(10)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,joziyat))
            ).click()
    driver.implicitly_wait(10)
    
    try:
        i=0
        while(True):
            i+=1        
            mamali=WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH,export_name_of_product(i)))
                ).text
            print(mamali)
    except:
        print(order)

def scrap_page(driver):
    init(driver)
    select_active(driver)
    for i in range(2, 22):
        open_consumer(driver,i)    
        scrab_details(driver)
        close_consumer(driver)

next_page_Xpath= '/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div/div[2]/div[3]/div'
def next_page(driver,page):
    driver.find_element_by_xpath(next_page_Xpath).click()
    

def main(driver):
    try:
        while(True):
            scrap_page(driver)
            next_page(driver)
    except:
        print("ENDS")
driver=webdriver.Chrome("./chromedriver.exe")


main(driver)

driver.quit()

