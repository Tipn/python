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
'''
f = open('file.txt', 'r', encoding='utf-8')# read
text = f.read() # прочитать весь файл целиком 
f.close
print(text) # Ст
'''
# file.write
# from os import write

'''
f = open('file.txt', 'a', encoding='utf-8') # write
f.write('Новая строка\n') # ток каждый раз надо добавлять перенос, и моменты форматирования, бо размещения в файле будет в строку
f.close
'''
#  добавить несколько строк в конце файла 
'''
lines = ['Новая строка 1', 'Новая строка 2']
f = open('file.txt', 'a', encoding='utf-8') #
for i in lines:
    f.write(i + '\n')
#f.writelines(lines) # добавляет строки без разделителей 
f.writelines(f'{i}\n' for i in lines) # добавляет строки с разделителями 

f.close()
'''
# file.readline or readlines
f = open('file.txt', 'r', encoding='utf-8') # парпметр r читает все в файле 
for line in f:
    print (line, end='')# end='' выводит без ненужных переносов 
f.close()
