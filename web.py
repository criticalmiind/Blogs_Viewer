from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import random
import urllib.request , socket

chrome_driver_path = ChromeDriverManager().install()
socket.setdefaulttimeout(180)

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

for p in proxies:
    url = random.choice(urls)

    print("Check your proxy ip:",p)
    time.sleep(1)
    if is_bad_proxy(p):
        # print("Bad proxy ip and port :",p,"\n\n")
        continue
    else:
        print("Valid proxy...\n","Opeing chrome...\n","Link:",url)
        time.sleep(1)
    

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
        # browser = webdriver.Chrome(chrome_options=options)
        # options.add_argument('--proxy-server=%s' % p)

        # browser = webdriver.Chrome(options=options)

        browser = webdriver.Chrome(chrome_driver_path, options=options)
        browser.get(url)
        # browser.get("https://api.scrapingdog.com/scrape?api_key=610b78ecd667b826c9b6816e&url=https://www.youtube.com/watch?v=Gq0YD1E8f70")
        time.sleep(15)
        browser.stop_client()
        browser.close()
        browser.quit()
    except:
        print("\n\n Error???")
        raise

