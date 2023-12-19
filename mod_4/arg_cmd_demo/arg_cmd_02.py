# Модуль sys позволяет работать с аргументами скрипта с помощью argv

import sys
'''
требования:
имя приветствуемого человека передавалось после именованного параметра --name или -n,
причем нужно следить, что в командной строке передано только одно имя. 
'''
''' решение с помощью проверок if '''
if len (sys.argv) == 1:
    print ("Привет, мир!")
else:
    if len (sys.argv) < 3:
        print ("Ошибка. Слишком мало параметров.")
        sys.exit (1)

    if len (sys.argv) > 3:
        print ("Ошибка. Слишком много параметров.")
        sys.exit (1)

    param_name = sys.argv[1]
    param_value = sys.argv[2]

    if (param_name == "--name" or
            param_name == "-n"):
        print ("Привет, {}!".format (param_value) )
    else:
        print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
        sys.exit (1)

'''
arg_cmd_02.py --name вася
'''
