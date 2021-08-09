from datetime import datetime
import random

class Anonymize():
    linux_proc = False
    mac_proc = False
    lang = False
    
    # default constructor
    def __init__(self):
        self.linux_proc = ['i686','x86_64']
        self.mac_proc = ['Intel','PPC','U; Intel','U; PPC']
        self.lang = ['en-US','sl-SI']
    
    def rand(min=5, max=7):
        return str(random.randint(min,max))
    
    def choose(list=[]):
        if list:
            return random.choice(list)
        else: return ''

    def firefox(self):
        time = datetime.today().strftime("%Y%m%d")
        ver = [
            'Gecko/'+time+' Firefox/'+self.rand()+'.0',
            'Gecko/'+time+' Firefox/'+self.rand()+'.0.1',
            'Gecko/'+time+' Firefox/3.6.'+self.rand(),
            'Gecko/'+time+' Firefox/3.8'
        ]

        platforms = [
            '(Windows NT '+self.rand(5,6)+'.'+self.rand(0,1)+'; '+self.choose(self.lang)+'; rv:1.9.'+self.rand(0, 2)+'.20) '+self.choose(ver),
            '(X11; Linux '+self.choose(self.linux_proc)+'; rv:'+self.rand(5, 7)+'.0) '+self.choose(ver),
            '(Macintosh; '+self.choose(self.mac_proc)+' Mac OS X 10_'+self.rand(5, 7)+'_'+self.rand(0, 9)+' rv:'+self.rand(2, 6)+'.0) '+self.choose(ver)
        ]

        return self.choose(platforms)

    def safari(self):
        saf = self.rand(531, 535) + '.' + self.rand(1, 50) + '.' + self.rand(1, 7)
        ver = self.rand(4, 5) + '.' + self.rand(0, 1)
        if self.rand(0, 1) == 0 :
    	    ver = self.rand(4, 5) + '.' + self.rand(0, 1)
        else:
    	    ver = self.rand(4, 5) + '.0.' + self.rand(1, 5)
    
        platforms = [
            '(Windows; U; Windows NT ' + self.rand(5, 6) + '.' + self.rand(0, 1) + ") AppleWebKit/" + saf + " (KHTML, like Gecko) Version/" + ver + "Safari/" + saf,
            '(Macintosh; U; ' + self.choose(self.mac_proc) + ' Mac OS X 10_' + self.rand(5, 7) + '_' + self.rand(0, 9) + ' rv:' + self.rand(2, 6) + '.0; ' + self.choose(self.lang) + ") AppleWebKit/" + saf + " (KHTML, like Gecko) Version/" + ver + " Safari/" + saf + "",
            '(iPod; U; CPU iPhone OS ' + self.rand(3, 4) + '_' + self.rand(0, 3) + ' like Mac OS X; ' + self.choose(self.lang) + ") AppleWebKit/" + saf + " (KHTML, like Gecko) Version/" + self.rand(3, 4) + ".0.5 Mobile/8B" + self.rand(111, 119) + " Safari/6" + saf + "",
        ]
    
        return self.choose(platforms)
    
    
    def iexplorer(self):
        ie_extra = [
            '',
            '; .NET CLR 1.1.' + self.rand(4320, 4325) + '',
            '; WOW64'
        ]
        platforms = ['(compatible; MSIE ' + self.rand(5, 9) + '.0; Windows NT ' + self.rand(5, 6) + '.' + self.rand(0, 1) + '; Trident/' + self.rand(3, 5) + '.' + self.rand(0, 1) + ')']
        return self.choose(platforms)
    
    def opera(self):
        op_extra = [
            '',
            '; .NET CLR 1.1.' + self.rand(4320, 4325) + '',
            '; WOW64'
        ]
        platforms = [
    	'(X11; Linux ' + self.choose(self.linux_proc) + '; U; ' + self.choose(self.lang) + ') Presto/2.9.' + self.rand(160, 190) + ' Version/' + self.rand(10, 12) + '.00',
    	'(Windows NT ' + self.rand(5, 6) + '.' + self.rand(0, 1) + '; U; ' + self.choose(self.lang) + ') Presto/2.9.' + self.rand(160, 190) + ' Version/' + self.rand(10, 12) + '.00'
        ]
    
        return self.choose(platforms)
    
    def chrome(self):
        saf = self.rand(531, 536) + self.rand(0, 2)
    
        platforms = [
            '(X11; Linux ' + self.choose(self.linux_proc) + ") AppleWebKit/" + saf + " (KHTML, like Gecko) Chrome/" + self.rand(13, 15) + '.0.' + self.rand(800, 899) + ".0 Safari/" + saf + "",
            '(Windows NT ' + self.rand(5, 6) + '.' + self.rand(0, 1) + ") AppleWebKit/" + saf + " (KHTML, like Gecko) Chrome/" + self.rand(13, 15) + '.0.' + self.rand(800, 899) + ".0 Safari/" + saf + "",
            '(Macintosh; U; ' + self.choose(self.mac_proc) + ' Mac OS X 10_' + self.rand(5, 7) + '_' + self.rand(0, 9) + ") AppleWebKit/" + saf + " (KHTML, like Gecko) Chrome/" + self.rand(13, 15) + '.0.' + self.rand(800, 899) + ".0 Safari/" + saf + ""
        ]
    
        return self.choose(platforms)
    
    # /**
    #  * Main def which will choose random browser
    #  * @return string user agent
    #  */
    def generate_user_agent(self):
        x = self.rand(1, 5)

        switcher = {
            1: "Mozilla/5.0 " + self.firefox(self),
            2: "Mozilla/5.0 " + self.safari(self),
            3: "Mozilla/" + self.rand(4, 5) + ".0 " + self.iexplorer(self),
            4: "Opera/" + self.rand(8, 9) + '.' + self.rand(10, 99) + ' ' + self.opera(self),
            5: 'Mozilla/5.0' + self.chrome(self)
        }
        getAgent = switcher.get(int(x))
        return getAgent