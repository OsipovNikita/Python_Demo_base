# Модуль sys позволяет работать с аргументами скрипта с помощью argv

import sys
import argparse
'''
требования:
имя приветствуемого человека передавалось после именованного параметра --name или -n,
причем нужно следить, что в командной строке передано только одно имя
и именованный параметр должен быть обязательным. 
'''
''' решение с помощью argparse
https://docs.python.org/3/library/argparse.html
Порядок работы с argparse:
1. Создаем экземпляр класса ArgumentParser.
2. Добавляем в него информацию об ожидаемых параметрах с помощью метода add_argument (по одному вызову на каждый параметр).
3. Разбираем командную строку с помощью метода parse_args, передавая ему полученные параметры командной строки (кроме нулевого элемента списка sys.argv).
4. Используем полученные параметры.
'''
parser = argparse.ArgumentParser()                    # 1
'''можно указать, что этот параметр является обязательным -
в метод add_argument добавить параметр required=True'''
parser.add_argument ('-n', '--name', required=True)   # 2
param_value = parser.parse_args(sys.argv[1:])         # 3

print ("Привет, {}!".format (param_value.name) )      # 4

print (param_value) # Namespace(name='вася')
'''
arg_cmd_03_1_2.py --name вася

Привет, вася!

при попытке запустить программу без параметров пользователь увидит ошибку:
arg_cmd_03_1_2.py

usage: arg_cmd_03_1_2.py.py [-h] -n NAME
arg_cmd_03_1_2.py.py: error: the following arguments are required: -n/--name

'''
