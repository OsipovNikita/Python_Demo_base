import collections

"""
Класс collections.namedtuple позволяет создать тип данных,
ведущий себя как кортеж, с тем дополнением, что каждому элементу
присваивается имя, по которому можно в дальнейшем получать доступ
"""
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)     # instantiate with positional or keyword arguments
p[0] + p[1]             # indexable like the plain tuple (11, 22) - 33

x, y = p                # unpack like a regular tuple
print(x, y) 		# (11, 22)
p.x + p.y               # fields also accessible by name - 33

print(p)                # readable __str__ with a name=value style
                        #Point(x=11, y=22)
