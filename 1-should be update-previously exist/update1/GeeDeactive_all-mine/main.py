from selenium import webdriver
from util import (init
                ,select_active,deactive)
from datetime import datetime
import time

start_page=1
end_page=150
driver=webdriver.Chrome("./chromedriver.exe")

init(driver)

dt1=datetime.now()
# select_HighPrice(driver)
select_active(driver)
#select_sticker(driver)
#Go_page(driver, start_page)

for k in range(start_page,end_page+1):
    for i in range(100):
        try:
            deactive(driver,i)
        except:
            print(i,'--',k)
    #time.sleep(1)
    #Go_page(driver, k)
    #print('next_page')
    #time.sleep(1)

time.sleep(5)
dt=datetime.now()-dt1
print(dt.second,' \n ',)
driver.quit()

