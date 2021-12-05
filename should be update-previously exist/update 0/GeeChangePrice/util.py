from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

location=     '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div[1]/div'
cost_page='//*[@id="root"]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/ul/div[3]'
price_tag='//*[@id="productTablePrice"]/span'
go_page='//*[@id="root"]/div/div/div[3]/div/div[2]/div[1]/div[2]/div/div[2]/div/input'
submit_price='/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div[3]'

sticker_tag='/html/body/div[1]/div/div/div[3]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]'
sticker_active_tag='/html/body/div[1]/div/div/div[3]/div/div[1]/div[2]/div[2]/div/div[2]/div[3]'


HighPrice='/html/body/div[1]/div/div/div[3]/div/div[1]/div[2]/div[4]/div/div[2]/div[2]'

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
    return [location+'['+str(i)+']' for i in range(1,21) ]


def changeprice(driver,loc,NewPrice):
    driver.implicitly_wait(5)
    x=WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,loc))
            )
    action=ActionChains(driver)
    action.move_to_element(x)
    action.perform()
    driver.implicitly_wait(5)
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,loc+'/div[4]/div[1]/div[1]'))
            ).click()
    driver.implicitly_wait(5)
    time.sleep(0.1)
    driver.find_element_by_xpath(cost_page).click()
    driver.find_element_by_xpath(price_tag).click()
    InputPrice=WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="price"]'))
            )
    InputPrice.clear()
    driver.implicitly_wait(5)
    time.sleep(0.2)
    InputPrice.send_keys(NewPrice)
    InputPrice.send_keys(Keys.RETURN)
    time.sleep(0.2)
    driver.implicitly_wait(5)
    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,submit_price))
            ).click()

    
    

def Go_page(driver,page):
    x=WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,go_page))
        )
    x.send_keys(Keys.CONTROL + "a")
    x.send_keys(page)
    x.send_keys(Keys.RETURN)
    

def select_sticker(driver):
    driver.implicitly_wait(5)

    x=WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID,'filter-2'))
            )
    action=ActionChains(driver)
    action.move_to_element(x)
    action.click(x)
    action.perform()
    WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH,sticker_tag))
            ).click()
    action=ActionChains(driver)
    action.move_to_element(x)
    action.click(x)
    action.perform()    
    
def select_active(driver):
    driver.implicitly_wait(5)

    x=WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID,'filter-1'))
            )
    action=ActionChains(driver)
    action.move_to_element(x)
    action.click(x)
    action.perform()
    WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH,sticker_active_tag))
            ).click()
    action=ActionChains(driver)
    action.move_to_element(x)
    action.click(x)
    action.perform()    
    
def select_HighPrice(driver):
    driver.implicitly_wait(5)

    x=WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID,'sort'))
            )
    action=ActionChains(driver)
    action.move_to_element(x)
    action.click(x)
    action.perform()
    WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH,HighPrice))
            ).click()
    action=ActionChains(driver)
    action.move_to_element(x)
    action.click(x)
    action.perform()    
