import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import random
import urllib.request , socket
from anonymize import Anonymize

chrome_driver_path = ChromeDriverManager().install()
socket.setdefaulttimeout(180)
stay_on_page = 15
pass_random_urls = False

def is_bad_proxy(pip):
    try:        
        proxy_handler = urllib.request.ProxyHandler({'http': pip})        
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)        
        sock=urllib.request.urlopen('http://www.google.com')  # change the url address here
        #sock=urllib.urlopen(req)
    except urllib.error.HTTPError as e:        
        # print('Error code: ', e.code)
        return e.code
    except Exception as detail:
        # print( "ERROR:", detail)
        return 1
    return 0

def read_proxies_from_file(file='proxies.txt'):
    proxies = []
    with open(file) as f:
        proxies = f.readlines()
    return proxies

def read_urls_from_file(file='urls.txt'):
    urls = []
    with open('urls.txt') as f:
        urls = f.readlines()
    return urls

proxies = read_proxies_from_file()
if len(proxies) < 1 :
    print("No proxy found")
    exit()

urls = read_urls_from_file()
if len(urls) < 1 :
    print("No url found")
    exit()

stay = input("Enter delay time(seconds) on page:")
if stay: stay_on_page = stay
os.system('cls||clear')
print("Default delay time set:", stay_on_page, "seconds... \n")

for p in proxies:
    print("Checking proxy server:",p)
    if is_bad_proxy(p):
        os.system('cls||clear')
        print("Bad proxy ip and port :",p)
        continue
    else:
        os.system('cls||clear')
        print("Valid proxy...","\nOpeing chrome...","\nProxy:",p)
    

    try:
        webdriver.DesiredCapabilities.CHROME['proxy']={
            # "httpProxy":p.get_address(),
            "httpsProxy":p,
            "httpProxy":p,
            "ftpProxy":p,
            "sslProxy":p,
            "proxyType":"MANUAL",
            "noProxy":'',
            "class":"org.openqa.selenium.Proxy",
            "autodetect":False
        }

        options = webdriver.chrome.options.Options()
        options.add_argument(chrome_driver_path)
        options.add_argument("--disable-extensions") # optional and off-topic, but it conveniently prevents the popup 'Disable developer mode extensions' 
        options.add_argument('--proxy-server=%s' % p)

        for u in urls:
            url = u
            try:
                user_agent = Anonymize.generate_user_agent(Anonymize)
                # options.add_argument('referer="https://devssecops.blogspot.com"')
                options.add_argument('user-agent="'+ user_agent +'"')
                # options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"')
                browser = webdriver.Chrome(chrome_driver_path, options=options)
                if pass_random_urls: url = random.choice(urls)
                os.system('cls||clear')
                print("proxy set:", p)
                print("user agent set:", user_agent)
                print("Opening url:",url)
                browser.get(url)
                time.sleep(int(stay_on_page))
                browser.stop_client()
                browser.close()
                browser.quit()
            except Exception as a:
                options = webdriver.ChromeOptions()
                options.add_experimental_option("detach", True)
                driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
                print("\n\n Error 001???", a)
                break
    except:
        print("\n\n Error 002???")
        raise

