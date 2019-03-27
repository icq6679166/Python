# encoding=UTF-8
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

browser = Chrome()
browser.get('https://shopping.pchome.com.tw/')
e1 = browser.find_element_by_id('keyword')
e1.clear()
e1.send_keys(u'獅王')
e1.send_keys(Keys.RETURN)
