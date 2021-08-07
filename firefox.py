# import org.openqa.selenium.By
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.proxy import Proxy, ProxyType

firefox_driver_path = GeckoDriverManager().install()
# driver = webdriver.Firefox(executable_path=firefox_driver_path)

# firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
# firefox_capabilities['proxy'] = {
#     # "httpProxy":p.get_address(),
#     "httpProxy":'123.108.201.91:1080',
#     "ftpProxy":'123.108.201.91:1080',
#     "sslProxy":'123.108.201.91:1080',
#     "proxyType":"MANUAL",
#     "noProxy":'',
#     "class":"org.openqa.selenium.Proxy",
#     "autodetect":False
# }
# firefox_capabilities['marionette'] = True
# firefox_capabilities['executable_path'] = firefox_driver_path
# browser = webdriver.Firefox(capabilities=firefox_capabilities)

myProxy = "123.108.201.91:1080"
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': None # set this value as desired
})

browser = webdriver.Firefox(executable_path=firefox_driver_path, proxy=proxy)
browser.get("https://www.google.com/search?q=my+ip")
# driver.quit()