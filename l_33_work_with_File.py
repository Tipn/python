# работа с файлами 
# https://pythonz.net/references/named/open/ 
# после открытия файл его нужно закрывать!! 
'''
f = open('file.txt', encoding='utf-8')
text = f.read(2)
text2 = f.read(8)
print(f.encoding) # UTF-f

f.close

print(text) # Ст
print(text2) # рока 1
'''
f = open('file.txt', 'r', encoding='utf-8')
text = f.read() # прочитать весь файл целиком 

f.close

print(text) # Ст