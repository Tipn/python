# дан масив, в котором среди прочих элементов есть слово "odd" (нечетный). Определите, есть ли в списке число, 
# которое является индексом элемента "odd". Напишите функцыю, которая будет возвращать True or False, соответсвенно.

def odd_ball(arr):
    return arr.index('odd') in arr #первая задача с масивом функции 
    # return 10 in arr # 

print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"])) # True
print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"]))  # False
print(odd_ball(["even",10,"odd",2,"even"]))          # True


# print(10 in ["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"])

"""
2 напишите функцию find_sum(n), где аргумент функция - это конечный элемент
последовательности включительно. Функция должна вернуть сумму всех чисел последовательности,
кратных 3 или 5. Попробуй решить задачу двумя способами (1 из способов в одну строку кода).
range 
"""

def find_sum(n):
    pass

find_sum(5) # return 8 (3 + 5)
find_sum(10) # return 33 (3 + 5 + 6 + 9 + 10)

"""
3 Дан список имен. Выберете в новый список только те имена, которые состоят из 4-х букв.
names - ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
"""

def get_names(names):
    pass