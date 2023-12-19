# Модуль sys позволяет работать с аргументами скрипта с помощью argv

import sys
import argparse
'''
необходимо добавить параметры, которые должны работать как флаги
и давали бы возможность изменять логику программы
'''
parser = argparse.ArgumentParser()
'''
В метод add_argument нужно добавить аргумент action,
который предназначен для выполнения некоторых действий над значениями
переданного параметра '''
parser.add_argument ('-n', '--name', default='Друг')   
parser.add_argument ('-c', '--count', default=1, type=int)
parser.add_argument ('-g', '--goodbye', action='store_true', default=False)
param_value = parser.parse_args(sys.argv[1:])          

if param_value.goodbye:
    for _ in range(param_value.count):
        print ("Пока, {}!".format (param_value.name) )       
else:
    for _ in range(param_value.count):
        print ("Привет, {}!".format (param_value.name) )  

'''
arg_cmd_08.py --name вася -c 3

Привет, вася!
Привет, вася!
Привет, вася!

arg_cmd_08.py --count 3 --name вася --goodbye
Пока, вася!
Пока, вася!
Пока, вася!
'''
