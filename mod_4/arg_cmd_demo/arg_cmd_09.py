# Модуль sys позволяет работать с аргументами скрипта с помощью argv

import sys
import argparse
'''
необходимо в качестве первого параметра указывать имя команды,
за которой будут следовать параметры, специфические именно для этой команды. 
Такое разделение на команды позволяют сделать подпарсеры
'''
parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers (dest='command')
 
hello_parser = subparsers.add_parser ('hello')
hello_parser.add_argument ('--names', '-n', nargs='+', default=['Друг'])
	 
goodbye_parser = subparsers.add_parser ('goodbye')
goodbye_parser.add_argument ('-c', '--count', type=int, default=1)
goodbye_parser.add_argument ('--nameg', '-ng', default=['Друзья'])
       
param_value = parser.parse_args(sys.argv[1:])

if param_value.command == "hello":
    for name in param_value.names:
        print ("Привет, {}!".format (name) ) 
elif param_value.command == "goodbye":
    for _ in range(param_value.count):
        print ("Пока!{}!".format (param_value.nameg) ) 
else:
     print ("Что-то пошло не так...")

'''
В реальной программе каждую команду надо обернуть
в отдельный класс или реализовать хотя бы в виде отдельной функции

arg_cmd_demo> arg_cmd_09.py hello --names вася петя света
Привет, вася!
Привет, петя!
Привет, света!

arg_cmd_09.py goodbye --count 3 --nameg ТОварищи
Пока!ТОварищи!
Пока!ТОварищи!
Пока!ТОварищи!
'''
