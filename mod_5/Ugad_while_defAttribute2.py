from random import randint
#n = 0               # Счетчик числа попыток

n_comp = randint(1, 100)
print(n_comp)
print('Компьютер "загадал" число в интервале от 1 до 100. Какое?')

def check_numder(numder, n_comp):
    #if not hasattr(check_numder, "n"):
    #   check_numder.n = 0 
    #check_numder.n += 1
    check_numder.n = getattr(check_numder, 'n', 0) + 1
    if numder > n_comp:
        return 'Загаданное число меньше'
    elif otvet < n_comp:
        return 'Загаданное число больше.'
    else:
        return f'Правильно! Число попыток отгадывания - {check_numder.n}'


while True: 
    otvet = int(input('Введите Ваше число '))
    answer = check_numder(otvet, n_comp)
    print(answer)
    if otvet == n_comp:
        break 


'''
Замечания по реализации:
главный цикл организует логику повторения попыток,
а функция считает их количество, добавляя себе атрибут и
использует как статическую переменную
'''
