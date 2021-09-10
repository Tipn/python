# дан список words. составте из него список слов-полиндромовю сделать это двумя способами 
# произвольное решение и решение в одну стоку кода 
# дан список my-str со строками из часть из которых являются палиндромами. составить новый список слов палиндромовю

words = ['мадам', 'топот', 'test', 'madam', 'word']
my_str = ['око за око', 'а роза упала на лапу азора', 'около маши молоко', '', ]

palindroms = []
for word in words:
    if word == word[::-1]:
        palindroms.append(word)
print (palindroms)
************************

palindroms =[word for word in words if word == word[::-1]] # добавь в список word из word которое берется из words
print (palindroms)


    # word[::-1] # перевернуть слово 


# l1 = [i for i in words if i != 'test' and != 'word']
# print (l1)