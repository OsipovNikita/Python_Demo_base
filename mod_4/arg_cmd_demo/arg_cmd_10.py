# Модуль sys позволяет работать с аргументами скрипта с помощью argv

import sys
import argparse
'''
необходимо реализовать возможность вызова справки
используя специальный параметр командной строки --help или -h
Решение: Для того, чтобы повлиять на внешний вид выводимой справки,
используются дополнительные параметры конструкторе ArgumentParser,
а также в методах add_argument, add_subparsers и add_parser

'''
parser = argparse.ArgumentParser(
    prog = 'arg_cmd_help',
    description = '''Это полезная программа,
которая позволяет поприветствовать нужных людей,
или попрощаться с ними.''',
    epilog = '''(c) NikO 2023. Пользуйтесь на здоровье....'''
    )

subparsers = parser.add_subparsers (dest='command',
                                    title='Возможные команды',
                                    description='Команды, которые должны быть в качестве первого параметра %(prog)s')
 
hello_parser = subparsers.add_parser ('hello')
'''hello_parser.add_argument ('--names', '-n', nargs='+', default=['Друг'],
                           help='Список приветствуемых персон',
                           metavar = 'ИМЯ')'''
'''
Можно создать свою группу с помощью метода add_argument_group
и вызывать метод add_argument для добавления параметров уже не парсера, а группы
'''
hello_group = hello_parser.add_argument_group (title='Параметры')

hello_group.add_argument ('--names', '-n', nargs='+', default=['Друг'],
                           help='Список приветствуемых персон',
                           metavar = 'ИМЯ')
	 
goodbye_parser = subparsers.add_parser ('goodbye')
goodbye_parser.add_argument ('-c', '--count', type=int, default=1,
                             help = 'Сколько раз прощаться',
                             metavar = 'КОЛИЧЕСТВО')
goodbye_parser.add_argument ('--nameg', '-ng', default=['Друзья'],
                             help = 'С кем прощаться',
                             metavar = 'ИМЯ')
       
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
справка о прграмме:
arg_cmd_10.py --help

справка о подпарсерах:
arg_cmd_10.py hello --help

arg_cmd_10.py goodbye --help

'''
