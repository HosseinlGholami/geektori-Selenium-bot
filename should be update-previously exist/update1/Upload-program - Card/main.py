import os
from selenium import webdriver
from util import init , add_new_product

from functools import reduce

Worked_path=os.getcwd()
Content=os.listdir()

names=[name for name in Content if name.split('.')[-1]=='png']
category = Worked_path.split('\\')[-1]
price='4995'

driver = webdriver.Chrome('./chromedriver.exe')
init(driver)

for name in names:
    picPath=Worked_path+'\\'+name
    Name=reduce(lambda x,y: x+y,name.split('.')[0:-1])
    add_new_product(driver,Name,picPath,category,price)
                
driver.quit()
