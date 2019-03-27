from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

browser = Chrome()
browser.get("http://www.python.org")

element = browser.find_element_by_name('q')
element.clear()
element.send_keys("tensorflow")
element.send_keys(Keys.RETURN)
#browser.close()