import unittest
from unittest.mock import patch, Mock
from Project.scraper import Scraper 
from os import link
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

class ScraperTestCase(unittest.TestCase):

    
    def setUp(self):
        self.panda_obj = Scraper()

    def tearDown(self) -> None:
        self.panda_obj
        return super().tearDown()
    
    def test_extract_text(self):
        self.panda_obj.__init__
        self.panda_obj.visit_individual_link("https://gorillamind.com/collections/all/products/gorilla-dream-to-go")
        time.sleep(10)
        self.panda_obj.close_modal()
        name, price, description, size, num_reviews, strID = self.panda_obj.extract_text() 
        self.assertEqual(price,"$0.00")
        self.assertEqual(num_reviews,"0 Reviews")
        self.assertEqual(len(strID),36)
        return  name, price, description, size, num_reviews, strID 

    def test_extract_image(self):
        self.panda_obj.__init__
        self.panda_obj.visit_individual_link("https://gorillamind.com/collections/all/products/gorilla-dream-to-go")
        time.sleep(10)
        self.panda_obj.close_modal()
        final_image_link = self.panda_obj.extract_image()  
        self.assertTrue(type(final_image_link) is str)
        
        return final_image_link

    def test_create_dict(self):
        print('test_dict')
        name = "GORILLA MODE"
        price = "$49.99"
        description = "Porduct description"
        size = "40 servings"
        num_reviews = "0 Reviews"
        strID = "c4c63eb3e331ab32678baea2da2b2db5"
        final_image_link = "https://cdn.shopify.com/s/files/1/0369/2580/0493/products/Gorilla-Mode-Bombsicle_600x.png?v=1660581253"
        dict_products = self.panda_obj.create_dict(name, price, description, size, num_reviews, strID, final_image_link)
        self.assertEqual(num_reviews,"0 Reviews")
        self.assertEqual(dict_products['Name'],name)
        self.assertEqual(dict_products['Price ($)'],price)
        self.assertEqual(dict_products['Description'],description)
        self.assertEqual(dict_products['Size'],size)
        self.assertEqual(dict_products['Number of reviews'],num_reviews)
        self.assertEqual(dict_products['UUID'],strID)
        self.assertEqual(dict_products['Image'],final_image_link)



    
    def test_save_options(self):
        first_option ='1'
        second_option ='2'
        third_option ='3'
        self.assertEqual(self.panda_obj.save_options(first_option),'1')
        self.assertEqual(self.panda_obj.save_options(second_option),'2')
        self.assertEqual(self.panda_obj.save_options(third_option),'3')

    def test_check_RDS(self):
        names = 'fake name'
        self.assertEqual(Scraper.check_RDS(names),[])
        
        

    
        

