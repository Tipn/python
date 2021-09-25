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
