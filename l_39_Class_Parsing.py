# класс парсинга
# создаем класс для парсинга из 34 урока  
from Parser_class import Parser

parser = Parser('https://www.ua-football.com/sport', 'news.txt')
parser.run()
# print(parser.raw_html)
# print(parser.html)
print(parser.resalts)