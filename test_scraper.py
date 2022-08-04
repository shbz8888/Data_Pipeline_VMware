import unittest
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

    
    Scraper.__init__(unittest.TestCase)

    Scraper.visit_individual_link(unittest.TestCase)
    time.sleep(10)
    Scraper.__close_modal__(unittest.TestCase)

    
    def test_extract_text(self):
        name, price, description, size, num_reviews, strID = Scraper.extract_text(unittest.TestCase) 
        self.assertEqual(num_reviews,"NaN")
        self.assertEqual(len(strID),36)
        return  name, price, description, size, num_reviews, strID 

    def test_extract_image(self):
        final_image_link, final_image = Scraper.extract_image(unittest.TestCase)  
        self.assertTrue(type(final_image_link) is str)
        self.assertEqual((len(final_image_link)-len(final_image)),6)
        return final_image_link, final_image 




    def test_create_dict(self):
        print('test_dict')
        name, price, description, size, num_reviews, strID = Scraper.extract_text(unittest.TestCase) 
        final_image_link, final_image = Scraper.extract_image(unittest.TestCase)  
        dict_products = Scraper.create_dict(unittest.TestCase, name, price, description, size, num_reviews,strID,final_image_link)
        self.assertEqual(num_reviews,"NaN")
        self.assertEqual(dict_products['Name'],[name])
        self.assertEqual(dict_products['Price'],[price])
        self.assertEqual(dict_products['Description'],[description])
        self.assertEqual(dict_products['Size'],[size])
        self.assertEqual(dict_products['Num_reviews'],[num_reviews])
        self.assertEqual(dict_products['UUID'],[strID])
        self.assertEqual(dict_products['Image'],[final_image_link])
        

    
        

