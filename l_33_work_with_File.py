# работа с файлами 
# https://pythonz.net/references/named/open/ 
# после открытия файл его нужно закрывать!! 

f = open('file.txt')
text = f.read(1)
print(f.encoding)
f.close

print(text)