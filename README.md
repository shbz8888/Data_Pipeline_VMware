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

Milestone 3:
* Methods were created to retrieve key details from one of the pages, those details being: name, price, description, size, number of reviews, and the link for an image
* these methods were called extract_image and extract_text
```python
def extract_text(self):
        gear_container = self.driver.find_element(By.XPATH, '//div[@class="container"]')
        name = gear_container.find_element(By.XPATH, './/h1[@class="product_name title"]').text
        price = gear_container.find_element(By.XPATH, './/span[@class="money"]').text
        description_container= gear_container.find_element(By.XPATH, './/div[@class="description content"]')
        description = description_container.find_element(By.TAG_NAME, "p").text
        size = gear_container.find_element(By.XPATH, './/span[@class="variant-size"]').text
        num_reviews = gear_container.find_element(By.XPATH, './/a[@class="text-m"]').text
        time.sleep(2)
        ID = self.uid 
        strID = str(ID)
        print(strID)
        time.sleep(1)
        return name, price, description, size, num_reviews, strID 

def extract_image(self):
        gear_container = self.driver.find_element(By.XPATH, '//div[@class="container"]')
        image_container = gear_container.find_element(By.XPATH, './/img[@alt="Gorilla Mode"]')
        final_image  = image_container.get_attribute('data-zoom-src')
        https = 'https:'
        final_image_link = https + final_image
        time.sleep(1)
        return final_image_link
```
* the information was stored in a dictionary and a UUID was generated, UUID was used because it would generate a unique ID each time the code ran and could be used later to refer to the product dictionary saved earlier
* the information was then stored and saved locally in a folder called raw_data, the dictionary being saved as a .json file and the image being downloaded using the link in the dictionary
* a new folder was created for the product within the raw_data folder, this new folder was named using the UUID so that each product tha would eventually be scraped would not be confused
* within this new prodoct folder alongside the .json file for the dictionary an images folder was created which contained the downloaded image, the image was downloaded using the image link in the dictionary 
```python
def save_dictionary_locally(self,dict_products,strID,final_image_link):
        path = "/home/shahbaz/Data_Pipeline_NewVM/Data_Pipeline_VMware/raw_data"
        os.chdir(path)
        os.makedirs(f'{strID}')
        path2 = (f"/home/shahbaz/Data_Pipeline_NewVM/Data_Pipeline_VMware/raw_data/{strID}")
        os.chdir(path2)
        jsonString = json.dumps(dict_products)
        jsonFile = open("data.json", "w")
        #creates new folder for product in the 'raw_data' folder
        jsonFile.write(jsonString)
        jsonFile.close()
        
```
* the code for extracting the text, extracting the image link, downloading the image, and saving these locally were split into individual methods in order to increase granularity for easier reading and debugging in line with good software engineering practice. This meant that each method only dealt with one concern.
```python
   def download_image(self,strID,final_image_link):
        os.makedirs('Images')
        path3 = (f"/home/shahbaz/Data_Pipeline_NewVM/Data_Pipeline_VMware/raw_data/{strID}/Images")
        os.chdir(path3)
        with open(f'{strID}_1.png', 'wb') as f:
                #downloads image in new 'Images' folder
                f.write(requests.get(final_image_link).content)
```
* the main method was also expanded in order to accomodate the new methods
![Alt text](Images/Screenshot2.png)

