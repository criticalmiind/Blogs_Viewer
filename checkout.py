
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = ChromeDriverManager().install()
team = 'https://erp.pandoratech.ae/web/login'
team_u = 'shawal.ahmad@pandoratech.ae'
team_p = 'Adilhassan008.'
# mectrl_headerPicture

browser = webdriver.Chrome(chrome_driver_path)
browser.get(team)

try:
    # signin_button = browser.find_element_by_id('mectrl_headerPicture')
    # signin_button.click()
    # time.sleep(1)

    input = browser.find_element_by_name('login')
    input.send_keys(team_u)
    input.send_keys(Keys.RETURN)

    input = browser.find_element_by_name('password')
    input.send_keys(team_p)
    input.send_keys(Keys.RETURN)
    time.sleep(1)

    input = browser.find_element_by_class_name('drawer-toggle')
    input.click()
except:
    browser.close()
    raise

# query = 'https://www.onlypakistan.pk/google-cloud-hosting-vs-others/'

# browser = webdriver.Chrome(chrome_driver_path)
# browser.get('https://hide.me/en/proxy')

# search = browser.find_element_by_name('u')
# search.send_keys(query)
# search.send_keys(Keys.RETURN)

# element = browser.find_element_by_class_name('LC20lb')

# element.click()