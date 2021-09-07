#переменные. списки это масивы 
# список можно сравнить с картотекой, где у каждой карточки есть свое значение илил с много квартирным домом
 
l = [1, 2, 3, 'hello', ['test', 10], 'word', True] 

l2 = list ('hello')
l3 = list ((1,2,3))
l4 = [i for i in 'hello'] # использовали генератор списков
l5 = [i for i in 'hello world' if i != ' '] # без пробелов
l6 = [i for i in 'hello world' if i != ' ' and i !='e'] # без пробелов и без е
l7 = [i for i in 'hello world' if i not in ['a', 'e', 'i', 'u', 'o', ' ']] # без пробелов и без глассных

print (l, l2, l3, l4, l7, sep='\n' )

print (list(range(1,11,2)))