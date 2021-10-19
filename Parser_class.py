from bs4 import BeautifulSoup # парсинг всегда надо настраивать  Желательно разбивать на несколько елементов 
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
        news = self.html.find_all('li', class_='liga-news-items') # мы ищим все элементы li с классом =

        for item in news: # ф. которая записывает данные в файл 
            title = item.find('span', class_='d-block').get_text(strip=True)
            desc = item.find('span', class_='name-dop').get_text(strip=True)
            href = item.a.get('href')
            self.results.append({
                'title': title,
                'desc': desc,
                'href': href,
            })
    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(f'Новость № {i}\n\nНазвание: {item["titel"]}\nОписание: {item["desc"]}\n\Силка: {item["href"]}')
                i += 1


    def run (self):
        self.get_html()
        self.parsing()  # вызывает метод парсинга
        self.save()     # вызывает метод сохранения 
