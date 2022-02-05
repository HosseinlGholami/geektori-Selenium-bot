from selenium import webdriver
from util import (init , changeprice , Go_page , select_sticker
                ,select_active,select_HighPrice)
from datetime import datetime
import time
NewPrice=2455
start_page=1
end_page=134
driver=webdriver.Chrome("./chromedriver.exe")

Page_loc=init(driver)

dt1=datetime.now()
# select_HighPrice(driver)
select_active(driver)
select_sticker(driver)
Go_page(driver, start_page)

for k in range(start_page,end_page+1):
    for i in range(20):
        try:
            changeprice(driver,Page_loc[i],NewPrice)
        except:
            print(i,'--',k)
    time.sleep(3)
    Go_page(driver, k)
    print('next_page')
    
    time.sleep(3)
dt2=datetime.now()
print(dt1,' \n ',dt2)
driver.quit()

