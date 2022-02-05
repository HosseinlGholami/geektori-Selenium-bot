import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pickle

internet_speed=0.1

next_page_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div/div[2]/div[3]'

TNK_TXT='''دوست گیکتوری سلام
کم کم داریم به روزای اخر سال نزدیک میشیم و چی بهتر از این که روزای اخر رو با خوشحالی و هیجان کنار هم سپری کنیم
برای همین تیم گیکتوری میخواد ازت دعوت کنه تا بیای عیدی بگیری

از ۱۷اسفند تا ۲۳ام
قراره که داخل پیج اینستاگرام هر روز به ۴نفر جایزه بدیم

حالا جایزه ها چیه ؟؟
از کد۱۰۰هزار تومنی خرید محصولات اردیبهشت گرفته(یه عالمه سررسید ۱۴۰۰جذاب و...)
تا کد ۶۰هزارتومنی خرید استیکر 
و ارسال رایگان و پین هم که خواهیم داشت
جذاب تر از همههه قرار ۲تا پاور بانک عیدی بدیم
پس آب دستته بزار زمین، زنگوله ی پیج رو فعال کن که قراره برنده شی'''

confirm_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]'
Takmil_Xpath='//*[@id="orderModalStatus"]/div/div/div[5]'
edit_ersal_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div/div[3]/div/div/div[5]/div'
edit_ersal_yes_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div/div[3]/div/div/div/div[2]'
input_edit_ersal_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div/div[4]/div/textarea'
confrim_edit_ersal_Xpath='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]'


def init(driver):
    driver.get('https://geektori.ir/admin/orders')
    #loginPart
    with open("Geektori.ir", "rb") as fp:
            file = pickle.load(fp)
    INPUT_MAIL=file[0]
    PASS=file[1]
    InputMail=driver.find_element_by_id("username")
    InputMail.send_keys(INPUT_MAIL)
    InputPass=driver.find_element_by_id("password")
    InputPass.send_keys(PASS)
    InputPass.send_keys(Keys.RETURN)
    #define costomer_listapth
    COUSTOMER_XPATH='/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div/div[1]/div'
    Page_item=[COUSTOMER_XPATH+'['+str(i)+']' for i in range(1,22) ]
    return Page_item
                
def next_page(driver,page):
    driver.find_element_by_xpath(next_page_Xpath).click()
    return page + 1
def open_consumer(driver,Page_item,index):
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,Page_item[index]))
        ).click()
def check_open_dar_entezar(driver,Page_item,i):
    x=Page_item[i]+'/div[6]/div'
    y=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,x))
        ).text
    print(y)
    return y=='ارسال شده'

def scrab_details(driver):
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,Takmil_Xpath))
            ).click()
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,edit_ersal_Xpath))
            ).click()
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,edit_ersal_yes_Xpath))
            ).click()
    time.sleep(internet_speed)
    input_edit_ersal=WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,input_edit_ersal_Xpath))
            )
    input_edit_ersal.send_keys(TNK_TXT)
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,confrim_edit_ersal_Xpath))
            ).click()
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH,confirm_Xpath))
      ).click()

#     if Name in sefareshat_list:
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH,ersal_Xpath))
#             ).click()
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH,marsoole_Xpath))
#             ).click()
#         time.sleep(internet_speed)
#         InputMarsoole=WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH,inputmarso_Xpath))
#             )
#         InputMarsoole.send_keys(sefareshat_list[Name][0])
#         time.sleep(internet_speed)
#         InputMarsoole.send_keys(Keys.RETURN)
#         time.sleep(internet_speed)
  