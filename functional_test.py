from selenium import webdriver
import unittest

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

        # He adds a shirt and the number of shirts increases + 1
        # He changes the number of pants to 5
        # He changes the number of shirts back to zero and this says OUT-OF-STOCK
        # He checks the total inventory is the sum of all numbers (example 20)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
