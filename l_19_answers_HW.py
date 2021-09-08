l1 = [1,2,3]

# l2 = [i * 2 for i in l1] # без *2 дублирование списка
# print (l2)

res =0
for num in l1: # берем каждый элемент списка 
    res += num **2 # возводим его в степень 
print (res)

time1 = 3 #--> liters +1
time2 = 6.7 #--> liters =3
time3 = 11.8 #--> liters =5

print (time1//2)
print (time2//2)
print (int(time3//2)) # вернет без нуля


s= 'hello world'

if ' ' in s:
    s=s.upper()
    # print(s.capitalize())
else:
    s = s.lower()
print (s)