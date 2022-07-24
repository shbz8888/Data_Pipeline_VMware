# gamma
from os import link
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

        def go_to_all_products_link(self):
                AllProducts = self.driver.find_element(By.LINK_TEXT,"All Products")
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
                        time.sleep(1)   
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
                print(self.gear_link_list)
                print(f' there are {len(self.gear_link_list)} products in this list')
                print(type(self.gear_link_list))
                time.sleep(1)
                return 

        def go_back_to_page_1(self):
                previous = self.driver.find_element(By.LINK_TEXT,"Previous")
                time.sleep(3)
                previous.click()
                time.sleep(3)

       
        def go_to_next_page(self):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                next = self.driver.find_element(By.LINK_TEXT,"Next")
                next.click()
                time.sleep(2) 

        def enter_link(self):
                gear_container = self.driver.find_element(By.XPATH, '//div[@class="container collection-matrix"]')
                link = gear_container.find_element(By.XPATH, './/a[@class="hidden-product-link"]')
                time.sleep(3)
                link.click()
                time.sleep(2)

        def extract_text(self):
                gear_container = self.driver.find_element(By.XPATH, '//div[@class="container"]')
                money = gear_container.find_element(By.XPATH, './/span[@class="money"]').text
                print(money)
                name = gear_container.find_element(By.XPATH, './/h1[@class="product_name title"]').text
                print(name)
                description_container= gear_container.find_element(By.XPATH, './/div[@class="description content"]')
                description = description_container.find_element(By.TAG_NAME, "p").text
                print(description)
                size = gear_container.find_element(By.XPATH, './/span[@class="variant-size"]').text
                print(size)
                num_reviews = gear_container.find_element(By.XPATH, './/a[@class="text-m"]').text
                print(num_reviews)
                time.sleep(2)

        def extract_image(self):
                gear_container = self.driver.find_element(By.XPATH, '//div[@class="container"]')
                image_container = gear_container.find_element(By.XPATH, './/img[@class="lazyload--fade-in lazyautosizes ls-is-cached lazyloaded"]')
                final_image  = image_container.get_attribute('data-zoom-src')
                print(final_image)
                time.sleep(1)

       

        def main(self):
            self.get_website()
            self.go_to_all_products_link()
            self.close_modal()
            self.extract_links()
            self.go_to_next_page()
            self.extract_links()
            self.go_back_to_page_1()
            self.enter_link()
            self.extract_text()
            self.extract_image()
            
def go_function():
    go = Scraper()
    go.main()
    pass

if __name__=="__main__":
    go_function()
           







     


