# -*- coding: utf-8 -*-
'''парадокс Монти Холла
'''
import random

 
def monty_hall_without_change(choices):
# в начале каждой попытки случайно перемешаем массив
    random.shuffle(choices)
    return choices[random.randrange(len(choices))]
 
 
def monty_hall_with_change(choices):
    # в начале каждой попытки случайно перемешаем массив
    random.shuffle(choices)
    # первый выбор
    first_choice = random.randrange(len(choices))
    # ведущий открывает дверь с козлом
    for i in range(len(choices)):
        if i != first_choice and choices[i] == 'к':
            host_choice = i
            break
    # делаем второй выбор, меняя первое решение
    for i in range(len(choices)):
        if i != first_choice and i != host_choice:
            return choices[i]


# к - козел, а - автомобиль
choices = ['к', 'к', 'а']
# просто калое-либо большое число (количество опытов)
N = 100000

# проверяем вариант с неизменным выбором
win_count = 0
for _ in range(N):
    result = monty_hall_without_change(choices)
    if result == 'а':
        win_count += 1
# вероятность выиграть - частота выигранных опытов
print(win_count/N)
 
# проверяем вариант с изменением выбора
win_count = 0
for _ in range(N):
    result = monty_hall_with_change(choices)
    if result == 'а':
        win_count += 1
# вероятность выиграть - частота выигранных опытов
print(win_count/N)
