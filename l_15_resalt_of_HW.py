print('таблица умножения') 

for x  in range(1, 10):
    for y in range(2, 10):
        print (f'{x} * {y} = {x*y}\t', end='')
    print(' ')
else:
    print('Well done')
