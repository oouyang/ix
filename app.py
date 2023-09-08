import requests
import bs4
import urllib3
urllib3.disable_warnings()

bu = 'https://ixdzs.tw'
def httpget(u):
    response = requests.request('GET', u, verify=False)
    return response.text
def getChapter(c, bid):
    url = bu + '/read/%d/p%d.html' % (bid, c)
    text = httpget(url)
    soup = bs4.BeautifulSoup(text)
    return [i.get_text() for i in soup.select('section p')]
