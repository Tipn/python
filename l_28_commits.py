def get_sum(a, b):        
    """
    возвращает сумму аргументов a и b.  
    
    :param a: Первый аперанд
    :type a: int
    :param b: Второй аперфнд
    :type b: int
    :retern: Return type int
    """
    return a + b 
    # в области видимости переменной локальная  определяет контекст переменной для какой области он относится.
    #доступны только в функции

# print(get_sum(1,2))     
# все переменные определенные в глобальной переменной доступны везде 
# scope

def f():
    x=5
# print(x) # так работать не будет потому как переменная х внутри функции

a=5         # global
def f1():
    a = 10  # local 
    a += 1 
    print(a)
# print(a)
# f1()         # работает возвращает функцию 
# print(a)

def f2():
    global a
    a +=1
print(a)    # печатает глобальное значение
f2()        #выплняется функция 
print(a)    #печатает результат после обработки в функции
