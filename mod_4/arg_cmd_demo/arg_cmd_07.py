# Модуль sys позволяет работать с аргументами скрипта с помощью argv

import sys
import argparse
'''
необходимо в качестве входных параметров указать имена файлов,
в которые нужно записаит данные (или прочитать) 
'''
parser = argparse.ArgumentParser()
'''
В метод add_argument достаточно добавить в качестве параметра type не функцию open, а экземпляр класса,
полученного с помощью функции argparse.FileType, предназначенной для безопасной попытки открытия файла '''
parser.add_argument ('-n', '--name', default='Друг')   
parser.add_argument ('-c', '--count', default=1, type=int)
parser.add_argument ('-f', '--file', type=argparse.FileType(mode='w+'))
param_value = parser.parse_args(sys.argv[1:])          

for _ in range(param_value.count):
    param_value.file.write("Привет, {}!\n".format (param_value.name))       

       
param_value.file.close()
'''
arg_cmd_07.py --name вася -c 3 -f text.txt
в файле text будет записано:
Привет, вася!
Привет, вася!
Привет, вася!
'''
