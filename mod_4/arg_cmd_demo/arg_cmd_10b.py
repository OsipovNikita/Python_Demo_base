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
version = "1.0.1"
parser = argparse.ArgumentParser(
    prog = 'arg_cmd_help',
    description = '''Это полезная программа,
которая позволяет поприветствовать нужных людей,
или попрощаться с ними.''',
    epilog = '''(c) NikO 2023. Пользуйтесь на здоровье....''',
    add_help = False
    )

''' Создаем группу параметров для родительского парсера,
ведь у него тоже должен быть параметр --help / -h
'''
parent_group = parser.add_argument_group (title='Параметры')
parent_group.add_argument ('--help', '-h', action='help', help='Справка')
parent_group.add_argument ('--version',
                           action='version',
                           help = 'Вывести номер версии',
                           version='%(prog)s {}'.format (version))


''' Создаем группу подпарсеров '''
subparsers = parser.add_subparsers (dest='command',
                                    title='Возможные команды',
                                    description='Команды, которые должны быть в качестве первого параметра %(prog)s')

'''Создаем парсер для команды hello ''' 
hello_parser = subparsers.add_parser ('hello', add_help = False,
                                      help = 'Запуск в режиме "Hello, world!"',
                                      description = '''Запуск в режиме "Hello, world!".
В этом режиме программа приветствует список людей, переданных в качестве параметра.'''
                                      )
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
hello_group.add_argument ('--help', '-h', action='help', help='Справка')

	 
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
     parser.print_help()

'''
справка о прграмме:
arg_cmd_10b.py --help

справка о подпарсерах:
arg_cmd_10b.py hello --help

arg_cmd_10b.py goodbye --help

вывод версии
arg_cmd_10b.py --version

запуск без параметров (должна отобразиться справка) 
arg_cmd_10b.py
'''
