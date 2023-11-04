from urllib.parse import urlparse

def getBaseUrl(url):

    parsed_url = urlparse(url)
    base_url = parsed_url.scheme + '://' + parsed_url.netloc
    return base_url

def getSchme(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme