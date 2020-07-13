from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import unittest
import time

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

        # He presses the add button on shirts
        # Number of shirts increases by one
        # He changes the number of pants to 5
        # He changes the number of shirts back to zero and this says OUT-OF-STOCK
        # He checks the total inventory is the sum of all numbers (example 20)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
