# gamma
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()



def open_website()-> webdriver.Chrome:
    '''
    Open Zoopla and accept the cookies
    
    Returns
    -------
    driver: webdriver.Chrome
        This driver is already in the Zoopla webpage
    '''
    driver = webdriver.Chrome() 
    driver.get("https://gorillamind.com/")
    time.sleep(3)
    link = driver.find_element(By.LINK_TEXT,"All Products")
    link.click()
    time.sleep(10)
    try:
        modal = driver.find_element(By.XPATH,'//button[@class="sc-75msgg-0 RlRPc close-button cw-close"]')
        modal.click()
        time.sleep(3)
    except:
        time.sleep(3)
        pass
       
open_website()




    