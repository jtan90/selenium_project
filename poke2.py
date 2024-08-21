import time
from seleniumbase import BaseCase
from seleniumbase import Driver
from seleniumbase import SB
 
class get_card_details(BaseCase):
   
    def test_swag_labs(self):
        index=10000
        start_card=1
       
 
        with open("card.txt", "a", encoding='utf-8') as output_file:  
                # Construct the URL with the current page number
                url = f"https://yuyu-tei.jp/sell/poc/s/sv07"
                # url = f"https://yuyu-tei.jp/sell/poc/s/svk"
 
                # Open the current page
                self.open(url)
 
                elements=self.find_elements("//div[@class='col-md']")
                card_count=len(elements)
               
 
                for card_number in range(start_card, card_count):
                        self.open(f"https://yuyu-tei.jp/sell/poc/card/sv07/{index + card_number}")
                        self.sleep(1)
                        self.go_back()
                        self.sleep(1)