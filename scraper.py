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



gear_container = driver.find_element(By.XPATH, '//div[@class="container collection-matrix"]')
gear_list = gear_container.find_elements(By.XPATH, './/a[@class="hidden-product-link"]')
gear_link_list = []

for gear in gear_list:
        link = gear.get_attribute('href')
        gear_link_list.append(link)

print(f'There are {len(gear_link_list)} products in this page')
print(gear_link_list)        