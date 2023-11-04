import requests
from bs4 import BeautifulSoup
from util.urlUtil import getBaseUrl, getSchme

def getHyperTexts(url):

    baseUrl = getBaseUrl(url)
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')

    aTags = html.find_all('a')
    result = []
    for (idx, aTag) in enumerate(aTags):
        nextUrl = aTag['href']
        if nextUrl[0] != '/':
            continue
        if len(nextUrl) <= 1:
            continue
        v = nextUrl.split('/')
        del v[0]
        t = False
        for i in v:
            if i.find('tag') != -1:
                t = True
                break
        if t:
            continue
        if v[0].startswith('search'):
            continue

        nextUrl = baseUrl + nextUrl
        result.append(nextUrl)
    return result