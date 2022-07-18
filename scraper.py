# gamma
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import gamma
class Scraper:
        def __init__(self):
                self.gear_link_list = []
                self.driver = webdriver.Chrome()




        def get_website(self):
                self.driver.get("https://gorillamind.com/")
                time.sleep(1)

        def go_to_all_products(self):
                AllProducts = self.driver.find_element(By.LINK_TEXT,"All Products")
                time.sleep(1)
                AllProducts.click()
                time.sleep(10)

        def close_modal(self):
                try: 
                        modal = self.driver.find_element(By.XPATH,'//button[@class="sc-75msgg-0 RlRPc close-button cw-close"]')
                        print(modal)
                        modal.click()
                        print('Button clicked')    
                except:
                        print('No button found...exiting')
                        self.driver.quit() 
        
        def extract_links(self):
                gear_container = self.driver.find_element(By.XPATH, '//div[@class="container collection-matrix"]')
                gear_list = gear_container.find_elements(By.XPATH, './/a[@class="hidden-product-link"]')
                

                for gear in gear_list:
                        link = gear.get_attribute('href')
                        self.gear_link_list.append(link)
                time.sleep(1)   
                return 
        
        def go_next_page(self):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                next = self.driver.find_element(By.LINK_TEXT,"Next")
                next.click()
                time.sleep(2) 

        def extract_links_2(self):
                gear_container2 = self.driver.find_element(By.XPATH, '//div[@class="container collection-matrix"]')
                gear_list2 = gear_container2.find_elements(By.XPATH, './/a[@class="hidden-product-link"]')
                for gear2 in gear_list2:
                        link = gear2.get_attribute('href')
                        self.gear_link_list.append(link)
                
                print(f'There are {len(self.gear_link_list)} products in this page')
                print(self.gear_link_list)

        def main(self):
            self.get_website()
            self.go_to_all_products()
            self.close_modal()
            self.extract_links()
            self.go_next_page()
            self.extract_links_2()

def go_function():
    go = Scraper()
    go.main()
    pass


if __name__=="__main__":
    go_function()
           







     


