# Модуль sys позволяет работать с аргументами скрипта с помощью argv

import sys
import argparse
'''
необходимо, чтобы в качестве значения параметра принимался список строк.
Например, теперь нужно приветствовать нескольких человек
'''
parser = argparse.ArgumentParser()
'''
Использовать значение nargs='+',
обозначающее, что ожидаем одно или несколько значений '''
parser.add_argument ('-n', '--name', nargs='+', default='Друг')   
param_value = parser.parse_args(sys.argv[1:])          

for nm in param_value.name:
    print ("Привет, {}!".format (nm) )       


'''
arg_cmd_04.py --name вася коля света

Привет, вася!
Привет, коля!
Привет, света!
'''
