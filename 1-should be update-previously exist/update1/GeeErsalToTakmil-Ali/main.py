from selenium import webdriver
from util import (init ,scrab_details ,
                  next_page,open_consumer,check_open_dar_entezar)

driver = webdriver.Chrome('./chromedriver.exe')


#Xh : Excel handller ,DT:Date Time
Page_item=init(driver)

#local parameter
stop=False
page=65
end_page=200
i=0
while(stop==False):
    i +=1
    print (page , ' - ' , end_page,' : ', i)
    if check_open_dar_entezar(driver,Page_item,i) :
        try:
            open_consumer(driver,Page_item,i)
            scrab_details(driver)
            end_page = page +10
        except:
            print('stm wrong')
            
    #stop condition
    # stop =True
    if(i==20):
        i=0
        if(page==end_page):
            stop=True
        else:
            page=next_page(driver,page)
        
driver.quit()

