from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import unittest
import time

from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

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
        pant_num = self.browser.find_element_by_id('Pant_quantity')
        pant_num.send_keys(Keys.CONTROL + "a");
        time.sleep(1)
        pant_num.send_keys(Keys.DELETE)
        time.sleep(1)
        pant_num.send_keys('5')
        time.sleep(1)

        self.assertTrue(pant_num.get_attribute("value") == '5', "Value did not get updated to 5")
        time.sleep(1)

        # He changes the number of shirts back to zero and this says OUT-OF-STOCK
        shirt_num = self.browser.find_element_by_id('Shirt_quantity')
        shirt_num.send_keys(Keys.CONTROL + "a");
        time.sleep(1)
        shirt_num.send_keys(Keys.DELETE)
        time.sleep(1)
        shirt_num.send_keys('0')
        time.sleep(1)

        shirt_content = self.browser.find_element_by_id('Shirt').text
        self.assertTrue(shirt_content == 'Shirt - OUT OF STOCK', "OUT OF STOCK not shown")
        time.sleep(1)

        # He checks the total inventory is the sum of all numbers (example 20)
        quantities = self.browser.find_elements_by_tag_name("input")
        totalsum = sum([int(num.get_attribute("value")) for num in quantities])
        print("total sum is", totalsum)

        total = self.browser.find_element_by_id("Total")
        self.assertTrue(int(total.text)==totalsum, "Total number incorrect")
        time.sleep(1)




if __name__ == '__main__':
    unittest.main(warnings='ignore')
