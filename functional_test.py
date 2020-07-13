from selenium import webdriver
import unittest
import time

from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_inventory(self):
        # Luis knows of this website and opens it
        self.browser.get('http://localhost:5000')


        # He checks the title says “Inventory”
        self.assertIn('Inventory', self.browser.title)
        time.sleep(1)


        shirt_num = self.browser.find_element_by_id('Shirt_quantity').get_attribute("value")
        print("shirt number is:", shirt_num)

        # He presses the add button on shirts
        shirt_button = self.browser.find_element_by_id('Shirt_button')
        shirt_button.click()
        time.sleep(1)

        # Number of shirts increases by one
        new_shirt_num = self.browser.find_element_by_id('Shirt_quantity').get_attribute("value")
        self.assertTrue(int(shirt_num) + 1 == int(new_shirt_num), 'number did not update')
        time.sleep(1)

        # He changes the number of pants to 5


        # He changes the number of shirts back to zero and this says OUT-OF-STOCK


        # He checks the total inventory is the sum of all numbers (example 20)




if __name__ == '__main__':
    unittest.main(warnings='ignore')
