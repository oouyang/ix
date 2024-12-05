import requests
import bs4
import json
import urllib3
urllib3.disable_warnings()

bu = 'https://ixdzs.tw'
novelList = '/novel/clist/'
def httpget(u):
    response = requests.request('GET', u, verify=False)
    return response.text
def getChapter(c, bid):
    url = bu + '/read/%d/p%d.html' % (bid, c)
    text = httpget(url)
    soup = bs4.BeautifulSoup(text,features="html.parser")
    return [i.get_text() for i in soup.select('section p')]
def getCList(bid):
    payload = 'bid=%d'%bid
    url = bu + novelList
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request('POST', url, headers=headers, data=payload, verify=False)
    return json.loads(response.text)
