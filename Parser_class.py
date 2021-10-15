from bs4 import BeautifulSoup # парсинг всегда надо настраивать 
import urllib.request

class Parser:

    raw_html = ''
    html = ''
    resalts = []

    def __init__(self, url, path):
        self.url = url
        self.path = path 
