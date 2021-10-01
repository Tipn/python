from typing import Text


"""
module OS
metod walk 

надо получить дерево каталога 

folder 
    file1.txt
    subfolder
        2.Text
        3.Text
    subfolder
metod walk 
on 
!!! https://pythoner.name/walk  метод возвращает обэкт генератор, 
из которого получают кортеджи для каждого каталога переданой файловой иерархии.
"""
import os
tree = os.walk('folder')
for files in tree:
    print(files)    #('folder', ['subfolder2', 'subfolder1'], [])
                    # ('folder/subfolder2', ['subfolder2-1'], ['1.txt'])
                    # ('folder/subfolder2/subfolder2-1', [], ['4.txt'])
                    # ('folder/subfolder1', [], ['3.txt', '2.txt'])

print(tree)
