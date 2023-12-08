import os
''' os.getcwd() возвращает текущую рабочую директорию
Current Working Directory (текущая рабочая директория)'''
dirfile = os.getcwd()
'''глобальная перемення __file__ - возвращает относительный
путь файла скрипта относительно рабочей директории'''
filePath = __file__
print("This script file path is ", filePath)

'''
os.path.abspath(__file__) - возвращает абсолютный путь заданного относительного пути '''
absFilePath = os.path.abspath(__file__)
print("This script absolute path is ", absFilePath)

'''
Функция os.path.split() разделяет имя файла на чистый путь и чистое имя файла'''
path, filename = os.path.split(absFilePath)
print(f"Script file path: '{path}'\n filename: '{filename}'")
