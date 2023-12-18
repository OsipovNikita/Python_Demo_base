from functools import lru_cache
'''Пример эффективного вычисления чисел Фибоначчи с использованием кэша для реализации техники динамического 
программирования '''

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

k = 36
print([fib(n) for n in range(k)])

'''Функция суммирования (рекурсия)'''
@lru_cache(maxsize=50)
def mysum(n):
    if n == 1:
        return n
    print(f"'{n}'", end=" ")
    return n + mysum(n - 1)

s1 = mysum(7)
s2 = mysum(9)
s3 = mysum(5)

print((mysum.cache_info()))