from Anonymize import Anonymize
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import random
from time import sleep

anon = Anonymize()

class Helper(object):
    """docstring for ClassName."""
    # browser = False
    # def __init__(self, driver):
    #     browser = driver

    def get_configure_browser(self, chrome_driver_path, p):
        if p != False:
            webdriver.DesiredCapabilities.CHROME['proxy']={
                "httpsProxy":p,
                "httpProxy":p,
                "ftpProxy":p,
                "sslProxy":p,
                "proxyType":"MANUAL",
                "noProxy":'',
                "class":"org.openqa.selenium.Proxy",
                "autodetect":False
            }

        user_agent = anon.generate_user_agent()

        print(user_agent)

        options = webdriver.chrome.options.Options()
        options.add_argument('user-agent="'+ user_agent +'"')
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])

        options.add_argument("--disable-extensions") # optional and off-topic, but it conveniently prevents the popup 'Disable developer mode extensions' 
        return webdriver.Chrome(chrome_driver_path, options=options)
        
    def isBrowserAlive(self, browser):
        try:
            browser.current_url
            # or driver.title
            return True
        except Exception as e:
            return False

    def on_close(self, browser, time=0):
        if self.isBrowserAlive(browser):
            sleep(int(time))
            browser.stop_client()
            browser.close()
            browser.quit()

    def open_google(self, browser):
        browser.get('https://www.google.com/')

    def search_in_google(self, browser, query=''):
        try:
            search = browser.find_element_by_name('q')
            search.send_keys(str(query))
            # search.send_keys(Keys.RETURN)
            sleep(1)
        except Exception as e:
            raise e

    def get_all_hrefs(self, browser, keyword=''):
        temp_list = []
        try:
            href_list = browser.find_elements_by_xpath("//a[@href]")
            for a_tag in href_list:
                url = a_tag.get_attribute("href")
                if keyword in url:
                    temp_list.append(a_tag)
        except Exception as e:
            raise e
        return temp_list

    def get_blog_links_from_google(self, browser, blog):
        google_links = browser.find_elements_by_class_name('yuRUbf') #I went on Google Search and found the container class for the link
        a_tags = []
        for link in google_links:
            url = link.find_element_by_tag_name('a').get_attribute("href") #this code extracts the url of the HTML link
            if blog in url:
                a_tags.append(link.find_element_by_tag_name('a'))
        return a_tags

    def click_random_link(self, a_tags_list):
        if len(a_tags_list) > 0 :
            a = random.choice(a_tags_list)
            a.click()
            return True
        else:
            return False

    def get_page_from_list(self, val, p_list):
        page = False
        for p in p_list:
            if str(p.text) == str(val): page = p
        return page

    def is_bad_proxy(self, pip):
        try:        
            proxy_handler = urllib.request.ProxyHandler({'http': pip})        
            opener = urllib.request.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib.request.install_opener(opener)        
            sock=urllib.request.urlopen('http://www.google.com')  # change the url address here
            #sock=urllib.urlopen(req)
        except urllib.error.HTTPError as e:
            return e.code
        except Exception as detail:
            return 1
        return 0

    def read_from_file(self, file=False):
        urls = []
        if file:
            with open(file) as f:
                urls = f.readlines()
        return urls