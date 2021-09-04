from Helper import Helper
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

chrome_driver_path = ChromeDriverManager().install()
helper = Helper()

class BlogVisiter(object):
    browser = False
    keyword = False
    
    def __init__(self, driver, keyword):
        self.browser = driver
        self.keyword = keyword
    
    def open_blog(self, url=''):
        self.browser.get(url)
        time.sleep(1)
        href_list = helper.get_all_hrefs(self.browser, self.keyword)
        return href_list

    def click_href(self, a_tag=False):
        if a_tag == False: return []
        time.sleep(1)
        a_tag.click()
        time.sleep(1)
        href_list = helper.get_all_hrefs(self.browser, self.keyword)
        return href_list

    def visits_inside_blog(self, a_list):
        temp_list = a_list
        i = random.choice(list(range(1,10)))
        while i >= 0:
            if temp_list and len(temp_list) > 0 :
                atag = random.choice(temp_list)
                temp_list = self.click_href(atag)
                time.sleep(2)
                i = i - 1