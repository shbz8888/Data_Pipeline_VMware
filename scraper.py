# gamma
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Scraper:
        def __init__(self):
                #constants go within the function and variables go inside the brackets above
                self.gear_link_list = []
                self.driver = webdriver.Chrome()

        def get_website(self):
                self.driver.get("https://gorillamind.com/")
                time.sleep(1)

        def collect_all_products_link(self):
                AllProducts = self.driver.find_element(By.LINK_TEXT,"All Products")
                time.sleep(1)
                link = AllProducts.get_attribute('href')
                #collects link for all products page 1
                self.gear_link_list.append(link)
                time.sleep(2)
                AllProducts.click()
                time.sleep(10)

        def close_modal(self):
        #closes pop up window
                try: 
                        modal = self.driver.find_element(By.XPATH,'//button[@class="sc-75msgg-0 RlRPc close-button cw-close"]')
                        print(modal)
                        modal.click()
                        print('Button clicked')    
                except:
                        print('No button found...exiting')
                        self.driver.quit() 
        
        def collect_next_page_link(self):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                next = self.driver.find_element(By.LINK_TEXT,"Next")
                link = next.get_attribute('href')
                #collects link for all products page 2
                self.gear_link_list.append(link)
                print(self.gear_link_list)
                next.click()
                time.sleep(2) 

        def main(self):
            self.get_website()
            self.collect_all_products_link()
            self.close_modal()
            self.collect_next_page_link()
            
def go_function():
    go = Scraper()
    go.main()
    pass

if __name__=="__main__":
    go_function()
           







     


