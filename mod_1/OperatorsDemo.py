a = 1
b = 2
a = a + b
print(a, type(a))
c = "start"
d = 'end'
# a = a + c # TypeError: unsupported operand type(s) for +: 'int' and 'str'
a = d
a = a + c
print(a, type(a))

age = 20
print(18 < age < 35)    # (18 < age) and (age < 35)
x, y, z = 2, 1, 2
print(x!=y!=z)           # (a != b) and (b != c)
'''лучше полностью избегать сцепленных операторов != '''

x = 25
y = 25.0
print(x is y)