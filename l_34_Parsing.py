# парсинг данных с ресурса -  
# https://ru.wikipedia.org/wiki/pip_(менеджер_пакетов) - менеджер пакетов система управления пакетов
# https://pypi.org аналог composer 
# beautifulsoup4.pypl
# https://docs.python.org/3/library/urllib.request.html - познакомится с модулем 
# надо установиь питон по умолчанию после продолжу 
from base64 import BeautifulSoup
import urllib.request 

req = urllib.request.urlopen('https://www.ua-football.com/sport')
print(req)