from bs4 import BeautifulSoup # парсинг всегда надо настраивать 
import urllib.request

class Parser:

    raw_html = ''
    html = ''
    resalts = []

    def __init__(self, url, path):
        self.url = url
        self.path = path 
    
    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()

    def run (self):
        self.get_html()


