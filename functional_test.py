from selenium import webdriver

browser = webdriver.Firefox()

browser.get('http://localhost:5000')

assert "Hello" in browser.title, "Title is not Hello"

browser.quit()
