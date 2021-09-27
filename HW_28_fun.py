# дан масив, в котором среди прочих элементов есть слово "odd" (нечетный). Определите, есть ли в списке число, 
# которое является индексом элемента "odd". Напишите функцыю, которая будет возвращать True or False, соответсвенно.

def odd_ball(arr):
    return arr.index('odd') in arr #первая задача с масивом функции 
    # return 10 in arr # 

print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"])) # True
print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"]))  # False
print(odd_ball(["even",10,"odd",2,"even"]))          # True


# print(10 in ["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"])