#import pysimlib.mymath as myoper
'''
если в __init__ добавлено from pysimlib.mymath import *
то можно имя модуля не указывать - импортировать пакет
'''
import pysimlib
import pysimlib as myoper

sm = pysimlib.mysub(3,69)
print(sm)

sm = myoper.myadd(3,69)
print(sm)

sm = myoper.mymul(3,69)
print(sm)

su = myoper.myqrt3(69)
print(su)

su = myoper.mydiv(6,0)
print(su)



from pysimlib import mymath as oper

sm = oper.mymul(3,69)
print(sm)

from pysimlib import mystat as op

su = op.mydiv(50)

print("{:.2f} ; {}".format(*su))


print(pysimlib.fibonacci(8))
