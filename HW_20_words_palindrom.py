# дан список words. составте из него список слов-полиндромовю сделать это двумя способами 
# произвольное решение и решение в одну стоку кода 
# дан список my-str со строками из часть из которых являются палиндромами. составить новый список слов палиндромовю

words = ['мадам', 'топот', 'test', 'madam', 'word']
my_str = ['око за око', 'А роза упала на лапу Азора', 'около Миши молоко', '', ]

# palindroms = []
# for word in words:
#     if word == word[::-1]:
#         palindroms.append(word)
# print (palindroms)
# ************************второе решение**********************

palindroms =[word for word in words if word == word[::-1]] # добавь в список word из word которое берется из words
print (palindroms)
# *************************следующая задача*********************

np = []
for word in my_str:
    word_r = word.replace(' ', '').lower() # вырезаем все пробеды после приводим к нижнему регистру # word_r = word_r.lower())
    if word_r == word_r[::-1]:
        np.append(word)

print(np)
    # word[::-1] # перевернуть слово 


# l1 = [i for i in words if i != 'test' and != 'word']
# print (l1)