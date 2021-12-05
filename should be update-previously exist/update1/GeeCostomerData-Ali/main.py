from selenium import webdriver
from util import (init,Scarb)

driver = webdriver.Chrome('./chromedriver.exe')
# Xh : Excel handller ,DT:Date Time
Wb,DT=init(driver)

Scarb(driver,Wb)

driver.quit()
Wb.save(DT+'.xlsx')
