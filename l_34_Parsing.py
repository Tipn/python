# парсинг данных с ресурса -  "https://www.ua-football.com/sport"
# для парсинга нам понадобится сторонний модуль "beautifulsoup4" работает с html & xml содержимим
# получим его спомощью модуля urllib.request
# https://ru.wikipedia.org/wiki/pip_(менеджер_пакетов) - менеджер пакетов система управления пакетов позволяет управлять 
# https://pypi.org аналог composer 
# beautifulsoup4.pypl
# https://docs.python.org/3/library/urllib.request.html - познакомится с модулем 
# надо установиь питон по умолчанию после продолжу 
from bs4 import BeautifulSoup
import urllib.request 

req = urllib.request.urlopen('https://www.ua-football.com/sport')

# print(req) # проверка все ли работает выдаст запрос 
# print(html) # в одну строку выдаст всю страничку без переносов 

html = req.read()

soup =BeautifulSoup(html)
print(soup) 