import math
import pysimlib


def myadd(a,b):
    return a+b

def mysub(a,b):
    return a-b

def mymul(a, b):
   return a * b

def mydiv(a, b):
    if pysimlib.is_log(b)==True:
        return a / b
    else:
        return 0

def myqrt3(a):
    return math.pow(a, 1/3)
