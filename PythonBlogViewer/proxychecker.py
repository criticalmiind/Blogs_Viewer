import urllib.request , socket

socket.setdefaulttimeout(180)

# read the list of proxy IPs in proxyList
proxyList = [] # there are two sample proxy ip
with open('proxies.txt') as f:
    proxyList = f.readlines()

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

def append_in_file(string):
    with open("temp_proxies.txt", "a+") as file_object:
        file_object.seek(0)
        file_object.write(string)

for item in proxyList:
    if is_bad_proxy(item):
        print ("Invalid:", item)
    else:
        print ("Valid:", item)
        append_in_file(item)