# def set_register(s):
#     if ' ' in s:
#         return s.upper()
#     else:
#         return s.lower()
# print(set_register('hello world'))
# print(set_register('hello,world'))

def get_sum(a, b, c, d):        # позицыонные аргументы каждая буква соответсвует цыфре ниже
    return a + b + c + d
# print(get_sum(1, 2, 5, 7)) # если не передать 1 элемент то будет ошибка 

def get_sum(a, b, c=0, d=1): # есть именнованые аргументы
    return a + b + c + d

print(get_sum(5, 2)) # поскольку именнованые уже заданы сумма будет по всем остальным 


print('hello', end='', sep='') # именнованые аргументы должны следовать после позицыонных 

#
#переменное количество аргументов

def get_sum(*args, **kwards): #аргументы и ключивые слова
    print(args)

get_sum(1, 5, 10, 5)

print(sum([1,2,3,7])) # 

def func(**x):
    print(x)
func(a=1, b=5, c= 20) #{'a': 1, 'b': 5, 'c': 20}

def f(a, x, *args, **kwords):
    print(a)
    print(x)
    print(args)
    print(kwords)

f(1, 2, 3, 4, b='test', c='hi')

