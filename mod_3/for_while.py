﻿# применение циклов для подсчета суммы элементов последовательности
lst = [1, 3, 5, 7, 9]
sum1 = 0
for _ in lst: # типичная итерация
   sum1 += _

print(sum1)


sum2 = 0
while lst:
    sum2 += lst[0]  # похоже на рекурсивный вызов
    lst = lst[1:]

print(sum2)



