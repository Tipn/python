# ошибки и исключения 
# отлавливать и исправить синтаксические 

# print(100 / 10 # пример синтаксической или критической ошибки 

# print(100 / 0 )# исключения ZeroDivisionError: division by zero

# print(1 + '2') # исключения TypeError: 

# print(int('test')) # исключения ValueError:
'''
try:                        # способ попробывать какойто кусок кода который может привести к ошибки
    num = 100 / 0           # ошибочный код
except ZeroDivisionError:   # описание при какой ошибки должно действовать исключение 
# except Exception:         # все исключения !
    num = 0                 # решение ошибочного значения 
print(num)                  # вывод без ошибки 
print('hi')
'''
'''
try:
    num = 100 / '2'
except Exception:
    num = 0
else:                   # else отрабатывает если код без ошибок 
    print('Else')
finally:                # finally выполняется всегда 
    print('Finally')
'''

while True:
    try:
        num = int(input('Enter your number: '))
        print(f'100 / {num} = {100 / num}')
        break
    except ZeroDivisionError:
        print('The number must be greater than zero')
    except ValueError:
        print('Must be a number')
