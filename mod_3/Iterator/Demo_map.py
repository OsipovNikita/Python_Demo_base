lst = ['qwerty', 'polo', 'molo', 'doom']
lenlst = map(len, lst)
print(lenlst)   # <map object at 0x000002BE75127670>
print(list(lenlst))   # [6, 4, 4, 4]

values = map(int, input().split())
dataTemo = list(values)
