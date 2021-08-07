from time import sleep
import urllib.request , socket

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
        return 1
    return 0

def write_in_file(proxy):
    with open('proxies.txt', 'a') as outfile:
        outfile.write(proxy)
    sleep(1)

def read_proxies_from_file(file='temp_proxies.txt'):
    proxies = []
    with open(file) as f:
        proxies = f.readlines()
    return proxies

proxies = read_proxies_from_file()

count = 0
for p in proxies:
    count = count + 1
    print(count,").  Check your proxy ip:",p)
    if is_bad_proxy(p): print("Invalid")
    else:
        print(count,"). Valid Address: ",p)
        write_in_file(p)