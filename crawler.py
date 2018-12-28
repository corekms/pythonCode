# sudo easy_install beaufulsoup4 -- GCP의 경우 sudo
# sudo pip3 install requests

# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

def checkUrl(urlStr):
        try: req = urllib.request.Request(urlStr)
        except Exception as e: return str(e)

        try: rawStr = urllib.request.urlopen(req)
        except Exception as e: return str(e)
        #convStr = unicode(rawStr).encode('utf-8') #python2.X
        convStr = rawStr.read() # python3 treates string as 'utf-8'
        rawStr.close()

        soup = BeautifulSoup(convStr, 'html.parser')
        table = soup.findAll('td',{"align":"center"})

        try:
                result = table[5].text.rstrip().lstrip()+"/"+table[4].text+":"+table[8].text
        except IndexError:
                result = "Exception arise / IndexError"
        return result
        

if __name__ == "__main__":
        print(checkUrl("http://www.kumkangho.co.kr/bk.popup.info.php?date=20190413&pa_uid=1"))

#print table[1].text.rstrip().lstrip()
#print table[2].text.rstrip().lstrip()
#print table[3].text.rstrip().lstrip()
#print table[4].text.rstrip().lstrip()
#print table[5].text.rstrip().lstrip()
#print table[6].text.rstrip().lstrip()
#print table[7].text.rstrip().lstrip()
#print table[8].text.rstrip().lstrip()