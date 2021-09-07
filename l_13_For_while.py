# циклы while & for 

# while stmt: 
    # do...
# https://pythonz.net/references/named/print

# i=1
# while i <= 10:
    # print (i, end=' ') 
    # i = i+1
    # i += 1

# print ('hello', 'world', sep='!', end=' | ')
# print ('hello2', 'world2')

# s= 'Hellow world'
# for l in s:   # для каждой буквы в строке s
    # if l == ' ':
        # continue
    # print (f'"{l}"', end=' ')  # "H" "e" "l" "l" "o" "w" "w" "o" "r" "l" "d"
    
for i in 'Hello world' :
    if i == ' ':
        break 
    print (i, end=' ') # работает в случае есле в переменной нет пробелов
else :
    print ('\nNo spaces') # работает в случае есле в переменной нет пробелов