'''
Каждая итерация цикла создает новый объект строки,
а старый объект строки при этом пропадает
'''
finalString = ''
for i in range(100000):
    finalString += 'spam '

print(finalString)

'''Питонический способ построения строк основан на присоединении меньших строк к списку
и на последующем слиянии элементов списка в одну строку.
Этот способ также создает 100000 строковых объектов,
но с выполнением только одной конкатенации строк при вызове join().
'''

finalString = []
for i in range(100000):
    finalString.append('spam ')

finalString = ''.join(finalString)

print(finalString)
