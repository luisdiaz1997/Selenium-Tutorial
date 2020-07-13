from selenium import webdriver

browser = webdriver.Firefox()

# Luis knows of this website and opens it
browser.get('http://localhost:5000')

# He checks the title says “Inventory”
assert "Inventory" in browser.title, "Title was " + browser.title

# He presses the add button on shirts
# Number of shirts increases by one
# He changes the number of pants to 5
# He changes the number of shirts back to zero and this says OUT-OF-STOCK
# He checks the total inventory is the sum of all numbers (example 10)

browser.quit()
