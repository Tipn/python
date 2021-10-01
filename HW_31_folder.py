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
"""
tree = os.walk('folder') # возвращает кортеджи 
for files in tree:
    print(files)    #('folder', ['subfolder2', 'subfolder1'], [])
                    # ('folder/subfolder2', ['subfolder2-1'], ['1.txt'])
                    # ('folder/subfolder2/subfolder2-1', [], ['4.txt'])
                    # ('folder/subfolder1', [], ['3.txt', '2.txt'])
"""

def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        #print(root, dirs, files)
                    #folder ['subfolder2', 'subfolder1'] []
                    # folder/subfolder2 ['subfolder2-1'] ['1.txt']
                    # folder/subfolder2/subfolder2-1 [] ['4.txt']
                    # folder/subfolder1 [] ['3.txt', '2.txt']
        level = root.count(os.sep)
        indent = ' ' * 4 * level # для пробела между путем и папкой
        print(f'{indent}[{os.path.basename(root)}]')
        sub_indent = ' ' * 4 * (level + 1)
        # print(root, files, level, indent, sub_indent)
        for file in files:
            print(f'{sub_indent}{file}')
            
                    #         [folder]
                    # [subfolder2]
                    #     1.txt
                    #     [subfolder2-1]
                    #         4.txt
                    # [subfolder1]
                    #     3.txt
                    #     2.txt

read_dir('folder') 
