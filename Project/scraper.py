
from os import link
import boto3
import selenium
import time
import uuid
import json
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
s3_client = boto3.client('s3')
s3 = boto3.resource('s3')
class Scraper:
        '''
        A scraper that extracts the product data from the website Gorilla Mind

        Methods:
        -------
        __get_website()
                opens the website in google chrome.
        __go_to_all_products_link()
                navigates to the all products section.
        __close_modal()
                Closes the sign up pop up window.
        __extract_links()
                begins extracting and storing the links for each individual product in the gear_link_list.
        __go_to_next_page()
                navigates to the next page.
        __go_back_to_page_1()
                navigates to page 1.
        extract_text()
                extracts the name, price, description, size, number of reviews, and generates a unique ID.
        extract_image()
                extracts the image link for the product.
        create_dict()
                stores all of the extacted text and image link in a dictionary.
        __save_dictionary_locally()
                creates a folder for the product and stores the dictionary inside.
        __download_image()
                creates an images folder within the product folder and downloads the image there.
        __extract_product_info()
                visits each link within the gear_link_list and extracts the text and image data by calling the above methods.
        __remove_obselete_link()
                remove 1 link from the gear_link_list which has a product without much data.
        visit_individual_link()
                made to make testing easier, called during unit testing.
        __main()
                calls all of the above methods in order.
        __save_to_S3_bucket()
                saves images and data dictionaries to AWS S3 bucket
        '''
        def __init__(self):
                '''
                initialiser

                Attributes:
                ----------
                gear_link_list: list
                        Empty list of product links to be filled by scraper
                driver: N/A (import)
                        module used to open and control google chrome for data scraping
                '''
                #constants go within the function and variables go inside the brackets above
                self.gear_link_list = []
                self.driver = webdriver.Chrome()
                 

        def __get_website(self):
                '''
                Opens a google chrome window and visits the website Gorilla Mind
                '''
                URL = "https://gorillamind.com/"
                self.driver.get(URL)
                time.sleep(2)

        def __go_to_all_products_link(self):
                '''
                Finds the All Products button and clicks it
                '''
                all_products = self.driver.find_element(By.LINK_TEXT,"All Products")
                time.sleep(1)
                all_products.click()
                time.sleep(10)

        def close_modal(self):
                '''
                Finds the cross off button on the sign up window and clicks it
                '''
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
                '''
                Finds the links to each product one by one and appends them to gear_link_list

                Attributes:
                ----------
                link: str
                        product page link
                '''
                gear_container = self.driver.find_element(By.XPATH, '//div[@class="container collection-matrix"]')
                gear_list = gear_container.find_elements(By.XPATH, './/a[@class="hidden-product-link"]')
                

                for gear in gear_list:
                        link = gear.get_attribute('href')
                        self.gear_link_list.append(link)
                time.sleep(1)   
                print(self.gear_link_list)
                print(f' there are {len(self.gear_link_list)} products in this list')
                time.sleep(1)
                return 
       
        def __go_to_next_page(self):
                '''
                Scrolls to the bottom of the page and clicks the next page button
                '''
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                next = self.driver.find_element(By.LINK_TEXT,"Next")
                next.click()
                time.sleep(2)

        def __go_back_to_page_1(self):
                '''
                Finds the previous page button and clicks it 
                '''
                previous_page_button = self.driver.find_element(By.LINK_TEXT,"Previous")
                time.sleep(4)
                previous_page_button.click()
                time.sleep(4) 

        def extract_text(self):
                '''
                Finds the name, price, description, product size, number of reviews of a product and generates a unique UUID

                Attributes:
                ----------
                name: str
                        Name of product
                price: str
                        price of product
                description: str
                        description of product
                size: str
                        product size
                num_reviews: str
                        number of product reviews
                ID: uuid.UUID
                        Unique ID generated for each product
                strID: str
                        Unique ID converted to a string
                '''
                gear_container = self.driver.find_element(By.XPATH, '//div[@class="container"]')
                name = gear_container.find_element(By.XPATH, './/h1[@class="product_name title"]').text
                price = gear_container.find_element(By.XPATH, './/span[@class="money"]').text
                description= gear_container.find_element(By.XPATH, './/div[@class="description content"]').text
                size = gear_container.find_element(By.XPATH, './/span[@class="variant-size"]').text
                try:
                        num_reviews = gear_container.find_element(By.XPATH, './/a[@class="text-m"]').text
                        ID = uuid.uuid4()
                        strID = str(ID)
                except:
                        num_reviews = "NaN"
                        ID = uuid.uuid4()
                        strID = str(ID)
                return name, price, description, size, num_reviews, strID 
                
        def extract_image(self):
                '''
                Finds the link for the product image, adding a 'https:' so that it can be downloaded later 
                
                Attribute:
                ---------
                final_image: str
                        shortened link for the product image
                https: str
                        prefix necessary for downloading from the image link later
                final_image_link: str
                        link for the product's image 
                '''
                try:
                        gear_container = self.driver.find_element(By.XPATH, '//div[@class="container"]')
                        image_container = gear_container.find_element(By.XPATH, './/img[@data-sizes="auto"]')
                        time.sleep(5)
                        final_image  = image_container.get_attribute('data-zoom-src')
                        https = 'https:'
                        final_image_link = https + final_image
                        time.sleep(1)
                except:
                        final_image_link = 'none'
                return final_image_link

        def create_dict(self, name, price, description, size, num_reviews, strID, final_image_link ):
                '''
                Saves all of the attributes extracted from the product page inside a dictionary

                Parameters:
                ----------
                name: str
                        Name of product
                price: str
                        price of product
                description: str
                        description of product
                size: str
                        product size
                num_reviews: str
                        number of product reviews
                strID: str
                        Unique ID converted to a string
                final_image_link: str
                        link for the product's image 

                '''
                dict_products = {'Name': [], 'Price': [], 'Description': [], 'Size': [], 'Num_reviews': [], 'UUID': [], 'Image': []}
                dict_products['Name'].append(name)
                dict_products['Image'].append(final_image_link)
                dict_products['Price'].append(price)
                dict_products['Description'].append(description)
                dict_products['Size'].append(size)
                dict_products['Num_reviews'].append(num_reviews)
                dict_products['UUID'].append(strID)
                return dict_products
               
        
        def __save_dictionary_locally(self,dict_products,strID,name):
                '''
                Creates a new folder for each product, converts the dictionary to json and stores it in the folder
                
                Parameters:
                ----------
                dict_products: dict
                        dictionary containing product details
                strID: str
                        UUID for a product converted to a string
                name: str
                        name of a product
                '''
                path = "/home/shahbaz/Data_Pipeline_NewVM/Data_Pipeline_VMware/Project/raw_data"
                os.chdir(path)
                os.makedirs(f'{name}')
                path2 = (f"/home/shahbaz/Data_Pipeline_NewVM/Data_Pipeline_VMware/Project/raw_data/{name}")
                os.chdir(path2)
                jsonString = json.dumps(dict_products)
                jsonFile = open("data.json", "w")
                #creates new folder for product in the 'raw_data' folder
                jsonFile.write(jsonString)
                jsonFile.close()
        

        def __save_to_S3_bucket(self,name,strID):
                '''
                Saves files to an amazon webservices S3 bucket

                Parameters:
                ----------
                name: str
                        name of a product
                strID: str
                        UUID for a product converted to a string
                '''
                s3.meta.client.upload_file(f'/home/shahbaz/Data_Pipeline_NewVM/Data_Pipeline_VMware/Project/raw_data/{name}/data.json','gorilla-mind-bucket', f'{name}.json')
                s3.meta.client.upload_file(f'/home/shahbaz/Data_Pipeline_NewVM/Data_Pipeline_VMware/Project/raw_data/{name}/Images/{strID}_1.png','gorilla-mind-bucket', f'{name}_image.png')


        def __download_image(self,strID,final_image_link,name):
                '''
                Creates a new folder within the individual product folder called 'Images' and downloads the image there
                
                Parameters:
                ----------
                strID: str
                        UUID for a product converted to a string
                final_image_link: str
                        link for the product's image 
                name: str
                        name of a product
                '''
                if final_image_link == 'none':
                        pass
                else:
                        os.makedirs('Images')
                        path3 = (f"/home/shahbaz/Data_Pipeline_NewVM/Data_Pipeline_VMware/Project/raw_data/{name}/Images")
                        os.chdir(path3)
                        with open(f'{strID}_1.png', 'wb') as f:
                                #downloads image in new 'Images' folder
                                f.write(requests.get(final_image_link).content)

        def extract_product_info(self):
                '''
                Iterates through the gear_link_list and collects and saves the data for each product

                Attribute:
                ---------
                link: str
                        product page link 
                gear_link_list: list
                       list of product links filled by scraper
                '''
                for link in self.gear_link_list:
                        self.driver.get(link)
                        time.sleep(5)
                        name, price, description, size, num_reviews, strID = self.extract_text()
                        final_image_link = self.extract_image()
                        dict_products =  self.create_dict(name, price, description, size, num_reviews, strID, final_image_link)
                        self.__save_dictionary_locally(dict_products, strID,name)
                        self.__download_image(strID,final_image_link,name)
                        self.__save_to_S3_bucket(name,strID)
                Scraper.data_saving_update()

        @staticmethod
        def data_saving_update():
                print('finished saving all dictionaries and images')
        
        def remove_obselete_link(self):
                '''
                Removes a product link which has very few details and so is not useful
                '''
                self.gear_link_list.remove('https://gorillamind.com/collections/all/products/gorilla-mode-energy-sample')


        def visit_individual_link(self, URL):
                '''
                Opens a google chrome window and visits the website Gorilla Mind
                '''
               
                self.driver.get(URL)
                time.sleep(1)

        
        def main(self):
                '''
                Main function which calls all the other functions ordered correctly
                '''
                self.__get_website()
                self.__go_to_all_products_link()
                self.close_modal()
                self.extract_links()
                self.__go_to_next_page()
                self.extract_links()
                self.__go_back_to_page_1()
                self.remove_obselete_link()
                self.extract_product_info()
            
            


def go_function():
    go = Scraper()
    go.main()
    pass

if __name__=="__main__":
    go_function()
           







     


