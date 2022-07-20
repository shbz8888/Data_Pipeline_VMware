# Data_Pipeline_VMware
Milestone 1 & 2:
* A web scraper was built 
* The website gorilla mind was chosen due to there being a lot of products available on the page to extract details from and me having some prior knowledge of the youtuber who owns the website and so some familiarity with its  contents
* Selenium was installed and imported in order to navigate the page autonomously
* Classes were used due to the functions within the scraper sharing similar outputs and inputs
* The new scraper class finds the button for the 'all products' page, collects the link of that page, closes the sign up pop up, scrolls to the bottom of the page, collects the link for the second page from the 'next' button and then navigates to the second page
* 'if __name__=="__main__":' was used so that the function only runs if its in the correct namespace 


the code:
```python
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
                '''initialise'''
                self.gear_link_list = []
                self.driver = webdriver.Chrome()

        def get_website(self):
                '''navigate to website'''
                self.driver.get("https://gorillamind.com/")
                time.sleep(1)

        def collect_all_products_link(self):
                '''collect link for all products and click button to navigate to page'''
                AllProducts = self.driver.find_element(By.LINK_TEXT,"All Products")
                time.sleep(1)
                link = AllProducts.get_attribute('href')
                #collects link for all products page 1
                self.gear_link_list.append(link)
                time.sleep(2)
                AllProducts.click()
                time.sleep(10)

        def close_modal(self):
                '''closes pop up window'''
                try: 
                        modal = self.driver.find_element(By.XPATH,'//button[@class="sc-75msgg-0 RlRPc close-button cw-close"]')
                        print(modal)
                        modal.click()
                        print('Button clicked')    
                except:
                        print('No button found...exiting')
                        self.driver.quit() 
        
        def collect_next_page_link(self):
                '''scrolls to bottom of page, gets link to final page and appends to link list'''
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
           
```

