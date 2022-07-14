# gamma
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("https://gorillamind.com/")
time.sleep(1)
link = driver.find_element(By.LINK_TEXT,"All Products")
time.sleep(1)
link.click()
time.sleep(10)

try: 
        modal = driver.find_element(By.XPATH,'//button[@class="sc-75msgg-0 RlRPc close-button cw-close"]')
        print(modal)
        modal.click()
        print('Button clicked')    

except:
        print('No button found...exiting')
        driver.quit() 


page_1 = driver.find_element(By.XPATH, '//a[@class="hidden-product-link"]')
#a_tag = page_1.find_element(By.TAG_NAME,'a')
link = page_1.get_attribute('href')
print(link)