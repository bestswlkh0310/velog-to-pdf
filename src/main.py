import requests
from bs4 import BeautifulSoup
from util.htmlUtil import getHyperTexts
import random
from util.htmlToPdf import htmlToPdf
from datetime import datetime
import os

startUrl = 'https://velog.io/@greencloud/%EA%B7%B8-async-%EA%BC%AD-%EC%8D%A8%EC%95%BC-%ED%95%98%EB%8B%88'

from collections import deque

q = deque()
q.append(startUrl)

memo = dict()

n = 20
i = 0

currentPath = os.getcwd()
now = datetime.now()

formatted_time = now.strftime("%Y-%m-%d %H:%M")

resultPath = currentPath + "/" + formatted_time

if not os.path.exists(resultPath):
    os.mkdir(resultPath)

while q and n > i:
    url = q.pop()
    (urlList) = getHyperTexts(url)
    random.shuffle(urlList)
    for u in urlList:
        if not u in memo:
            q.append(u)
            memo[u] = 1
            print(u)
            htmlToPdf(u, resultPath + f'/velog{i}')

            i += 1