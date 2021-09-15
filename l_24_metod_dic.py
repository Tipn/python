# dict.clear()    -очищает словарь
# dict.copy()     -возвращает копию
# dict.get(key[, default]) -возвращает значение ключа, но если его нет,
# не бросает исключение, а возвращет default (по умолчанию None)
# dict.items()    -возвращает пары(ключ, значение)
# dict.keys()     -возвращает ключи в словаре
# dict.pop(key[, default]) -удаляет ключи и возвращает значения. Если ключа нет,
# возвращает default (поумолчанию бросает исключение)
# dict.popitem()  -удаляет и возвращает пару (ключ, значение). Если словарь пуст,
# бросает исключение, KeyError. Помните что словари не упорядочены
# dict.setdefault(key[, default]) -вщзвращает значение ключа, но если его нет, не бросает исключение,
# а создает ключ с значением default (по умолчанию None)
# dict.update([other]) -обновляет словари, добавляя пары (ключ, значение) из other.
# существующие словари перезаписываются. Возвращая None (не новый словарь)
# dict.values()   -возвращает значение в словаре 

product1 = {'titel': 'Sony', 'price': '111'}
print(product1())
