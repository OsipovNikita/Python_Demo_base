# Модуль sys позволяет работать с аргументами скрипта с помощью argv

import sys
import argparse
'''
необходимо в качестве параметров использовать другие типы:
целые числа или числа с плавающей точкой 
'''
parser = argparse.ArgumentParser()
'''
В метод add_argument достаточно добавить еще один именованный параметр,
а именно параметр type, который будет указывать ожидаемый тип значения параметра '''
parser.add_argument ('-n', '--name', default='Друг')   
parser.add_argument ('-c', '--count', default=1, type=int)
param_value = parser.parse_args(sys.argv[1:])          

for _ in range(param_value.count):
    print ("Привет, {}!".format (param_value.name) )       


'''
arg_cmd_06.py --name вася -c 3

Привет, вася!
Привет, вася!
Привет, вася!
'''
