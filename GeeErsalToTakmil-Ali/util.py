import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import pickle


internet_speed=1

TEXT='Salam'

darentezar_filter_Xpath='/html/body/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div/div[1]'
Ersal_shode_Xpath='/html/body/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div/div[2]/div[3]'
                 
def costumer_Xpath(x):
    return'/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div/div[1]/div['+str(x)+']'

close_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]'



ersal_payam_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div/div[3]/div/div/div[5]/div'
                  
Select_yes_ersal_payam_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div/div[3]/div/div/div/div[2]'
input_text_ersal_payam_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div/div[4]/div/textarea'
Done_Text_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]'


def init(driver):    
    driver.maximize_window()
    with open("Geektori.ir", "rb") as fp:
        file = pickle.load(fp)
    driver.get('https://geektori.ir/admin/orders')
    #loginPart
    INPUT_MAIL=file[0]
    PASS=file[1]
    InputMail=driver.find_element_by_id("username")
    InputMail.send_keys(INPUT_MAIL)
    InputPass=driver.find_element_by_id("password")
    InputPass.send_keys(PASS)
    InputPass.send_keys(Keys.RETURN)


def Scarb(driver):
    time.sleep(3)
    #select_Ersal_Sohde
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,darentezar_filter_Xpath))
            ).click()
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,Ersal_shode_Xpath))
            ).click()
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,darentezar_filter_Xpath))
            ).click()
    time.sleep(internet_speed)
    #ScrabDetail
    stop=False
    i=1
    while(stop==False):
        i=i+1
        try:
            time.sleep(internet_speed)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,costumer_Xpath(i)))
                ).click()
            time.sleep(internet_speed)
#_____________________________________________________
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,Takmil_Xpath))
                ).click()
            time.sleep(internet_speed)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,ersal_payam_Xpath))
                ).click()
            time.sleep(internet_speed)
            
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,Select_yes_ersal_payam_Xpath))
                ).click()
            time.sleep(internet_speed)
            texBox=WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,input_text_ersal_payam_Xpath
                                                )))
            texBox.send_keys(TEXT)
            time.sleep(internet_speed)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,Done_Text_Xpath))
                ).click()
            time.sleep(internet_speed)
    
#_____________________________________________________            
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH,close_Xpath))
                ).click()
            time.sleep(internet_speed)
            
        except:
            stop=True
            if i==21:
                i=1
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,nextPage_Xpath))
                    ).click()
       
        
        
        
    
    
    
    