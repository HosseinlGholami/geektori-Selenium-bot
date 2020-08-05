from selenium import webdriver
from util import (init,Scarb)

driver = webdriver.Chrome('./chromedriver.exe')
#Xh : Excel handller ,DT:Date Time
init(driver)

x=Scarb(driver,1)


driver.quit()