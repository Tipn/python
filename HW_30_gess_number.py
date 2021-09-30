import random

x = random.randint(1, 100)
user_num = 0
cnt = 0

while True:         # запускаем цыкл 
    user_num = int(input('Угадайте заданное число от 1 до 100 - угодай его:')) # ввести значение переменной с консоли   
    cnt += 1        
    if user_num == x:               # если заданное значение user_num равно x то выолни следующее 
        print(f'ты угадал число за {cnt} попыток')
        print('УРРА!!!')

        if input('Сыграем Еще? "y|n":') == 'y':
            x = random.randint(1,100)
            cnt = 0
        else:
            print('спасибо за игру')
            break                       # закончи программу и выведи все значения 
    elif user_num > x:
        print('мое число меньше')
    else:
        print('мое число больше')