import unittest
from Project.scraper import Scraper 

class ScraperTestCase(unittest.TestCase):


      


    def test_create_dict(self):
        name = "GORILLA MODE"
        price = "$49.99"
        description = "\u2022 Intense Focus + Drive*\n\u2022 Huge Nitric Oxide Pump*\n\u2022 Increased Endurance + Power*"
        size = "40 Servings"
        num_reviews = "1521 Reviews"
        strID = "b0c08216-36ab-42cf-8c4d-59c9a22486d6"
        final_image_link = "https://cdn.shopify.com/s/files/1/0369/2580/0493/products/Gorilla-Mode-OG-Volcano-Burst_5000x.png?v=1656857311"
        B = Scraper.create_dict(self,name, price, description, size, num_reviews, strID, final_image_link)
        A = {'Name': ["GORILLA MODE"], 'Price': ["$49.99"], 'Description': ["\u2022 Intense Focus + Drive*\n\u2022 Huge Nitric Oxide Pump*\n\u2022 Increased Endurance + Power*"], 'Size': ["40 Servings"], 'Num_reviews': ["1521 Reviews"], 'UUID': ["b0c08216-36ab-42cf-8c4d-59c9a22486d6"], 'Image': ["https://cdn.shopify.com/s/files/1/0369/2580/0493/products/Gorilla-Mode-OG-Volcano-Burst_5000x.png?v=1656857311"]}
        self.assertDictEqual(A,B)

