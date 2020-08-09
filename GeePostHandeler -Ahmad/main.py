from selenium import webdriver
from Util import (check_open_dar_entezar,
                  init,
                  open_consumer,
                  scrab_details,
                  close_consumer,
                  next_page,
                  save_not_done,
                )

    
driver = webdriver.Chrome('./chromedriver.exe')


#Xh : Excel handller ,DT:Date Time
DT,Page_item,sefareshat_list=init(driver)


#local parameter
stop=False
page=1
end_page=0
i=0
while(stop==False):
    i +=1
    if check_open_dar_entezar(driver,Page_item,i) :
        open_consumer(driver,Page_item,i)
        scrab_details(driver,sefareshat_list)
        close_consumer(driver)
        end_page = page +1    
    #stop condition
    # stop =True
    if(i==20):
        i=0
        if(page==end_page):
            stop=True
        else:
            page=next_page(driver,page)
        
driver.quit()

save_not_done(sefareshat_list)        

