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
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = soup.find_all('li', class_='liga-news-items')

    def run (self):
        self.get_html()


