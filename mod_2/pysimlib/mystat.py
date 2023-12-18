import math
import random
import pysimlib

n = random.randint(0, 99)

def mydiv(a):
    if pysimlib.is_log(n)==True:
        return a / n, n
    else:
        return 0


