# изминяемые типы можно сменить не изменив ссылку на них
# обект хранится в оперативной памяти  
# https://pythonz.net/references/named/id/

# x = 10
# print(x, id(x)) #10 139780684282448

# x = 20
# print(x, id(x)) #20 139780684282768

# s = 'hello'
# print(s, id(s)) #hello 140431108384496
# s+='world'
# print(s,id(s))  #helloworld 140431108027120

# l =[1,2,3,4]
# print(1, id(l))#l 140250064950656
# l.append(5)
# print(l, id(l))#[1, 2, 3, 4, 5] 140250064950656

# x=10
# y=x
# print(x, id(x)) #10 140515758660176
# print(y, id(y)) #10 140515758660176

# x=15
# print(x, id(x)) #15 139824776157936
# print(y, id(y)) #10 140515758660176

l1=[1,2,3,]
l2=l1

print(l1, id(l1))
print(l2, id(l2))