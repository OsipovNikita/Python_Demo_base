# Модуль sys позволяет работать с аргументами скрипта с помощью argv

import sys
import argparse
'''
необходимо ограничить значения некоторого параметра заранее заданным списком значений 
'''
parser = argparse.ArgumentParser()
'''
В метод add_argument передать еще один параметр - choices,
который принимает список возможных значений параметра '''
parser.add_argument ('-n', '--name', choices=['вася', 'коля', 'света'], default='Друг')   
param_value = parser.parse_args(sys.argv[1:])          

print ("Привет, {}!".format (param_value.name) )       


'''
arg_cmd_05.py --name вася
Привет, вася!

arg_cmd_05.py --name васятка

usage: arg_cmd_05.py [-h] [-n {вася,коля,света}]
arg_cmd_05.py: error: argument -n/--name: invalid choice: 'васятка' (choose from 'вася', 'коля', 'света')
'''
