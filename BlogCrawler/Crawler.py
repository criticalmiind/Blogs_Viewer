from BlogCrawler import BlogVisiter
from time import sleep
from Helper import Helper
import os
from webdriver_manager.chrome import ChromeDriverManager
import socket
import random

socket.setdefaulttimeout(180)
helper = Helper()

class Crawler(object):
    chrome_driver_path = ChromeDriverManager().install()
    pass_random_urls = False
    page_no = 1
    google_pages = 1
    keywords = []
    proxies = []
    my_blog = 0

    def __init__(self, *args):
        self.my_blog = 'devssecops.blogspot.com' # input("Enter your domain/subdomain name(e.g example.com/test.example.com):")

        self.keywords = helper.read_from_file('files/keywords.txt')
        if len(self.keywords) < 1:
            print("keywords not found in keywords.txt file.\nplease add your keywords in keywords.txt file.")
            exit();

        self.proxies = helper.read_from_file('files/proxies.txt')
        if len(self.proxies) < 1:
            print("proxies not found in proxies.txt file.\ncrawler will serf without proxies!")

    def get_proxy(self, proxy):
        print("Checking proxy server:",proxy)
        if helper.is_bad_proxy(proxy):
            print("Bad proxy ip and port :",proxy)
            return False
        else:
            print("Opeing chrome...","\nProxy:",proxy)
            return proxy

    def crawler(self, proxy=False):
        for keyword in self.keywords:
            browser = helper.get_configure_browser(self.chrome_driver_path, proxy)
            # instance of Blog Visiter
            blog_vister = BlogVisiter(browser, self.my_blog)

            try:
                helper.open_google(browser)
                helper.search_in_google(browser, keyword)
                if self.google_pages > 0 and self.page_no <= self.google_pages:
                    while self.page_no <= self.google_pages:
                        self.page_no = self.page_no + 1
                        pages_list = browser.find_elements_by_xpath("//table[@class='AaVjTc']/tbody/tr/td/a")

                        self.google_pages = len(pages_list)
                        
                        page = helper.get_page_from_list(self.page_no, pages_list)
                        if page == False or self.google_pages < self.page_no:
                            sleep(1)
                            helper.on_close(browser, 0)
                            sleep(1)
                            break

                        a_tags = helper.get_blog_links_from_google(browser, self.my_blog)
                        sleep(1)
                        if len(a_tags) > 0 :
                            print("your keyword for your blog/website found on google search page:", page.text)
                            
                            try:
                                blog_vister.visits_inside_blog(a_tags)
                            except Exception as e:
                                helper.on_close(browser,0)
                                raise e

                        else:
                            print("your keyword for your blog/website not found on google search page:", page.text)
                            page.click()
                else:
                    self.google_pages = 1
                    self.page_no = 1
                    helper.on_close(browser, 0)
            except Exception as e:
                print(e)
                helper.on_close(browser, 0)

            # reset google page
            self.google_pages = 1
            self.page_no = 1
            helper.on_close(browser, 0)

    def start(self):
        if len(self.proxies) > 0 :
            for proxy in self.proxies:
                is_proxy = self.get_proxy(proxy)
                if is_proxy: self.crawler(proxy)
        else: self.crawler(False)

crawler = Crawler()
crawler.start()