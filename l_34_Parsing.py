# парсинг данных с ресурса -  "https://www.ua-football.com/sport"
# для парсинга нам понадобится сторонний модуль "beautifulsoup4" работает с html & xml содержимим
# получим его спомощью модуля urllib.request
# https://ru.wikipedia.org/wiki/pip_(менеджер_пакетов) - менеджер пакетов система управления пакетов позволяет управлять 
# https://pypi.org аналог composer 
# beautifulsoup4.pypl
# https://docs.python.org/3/library/urllib.request.html - познакомится с модулем 
# надо установиь питон по умолчанию после продолжу 
# pythonz.net/references/named/string.strip 
from os import close
from bs4 import BeautifulSoup
import urllib.request 

req = urllib.request.urlopen('https://www.ua-football.com/sport')
# print(req) # проверка все ли работает выдаст запрос 
# print(html) # в одну строку выдаст всю страничку без переносов 
html = req.read()  # функция получает запрос 

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('li', class_='liga-news-item') # ф. которая парсит данные 
# print(news)

results = []

for item in news: # ф. которая записывает данные в файл 
    title = item.find('span', class_='d-block').get_text(strip=True)
    desc = item.find('span', class_='name-dop').get_text(strip=True)
    href = item.a.get('href')
    results.append({
            'title': title,
            'desc': desc,
            'href': href,
    })
f =open ('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость № {i}\n\nНазвание: {item["titel"]}\nОписание: {item["desc"]}\n\Силка: {item["href"]}')
        i += 1
f.close()
# print(results) # распечаттаь масив словарей 