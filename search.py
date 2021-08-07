import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = ChromeDriverManager().install()
query = 'https://www.onlypakistan.pk/google-cloud-hosting-vs-others/'

browser = webdriver.Chrome(chrome_driver_path)
browser.get('https://hide.me/en/proxy')

search = browser.find_element_by_name('u')
search.send_keys(query)
search.send_keys(Keys.RETURN)

element = browser.find_element_by_class_name('LC20lb')

element.click()