import random,string,time
'''если сравнить время работы этих двух методов, то выясниться, что
1-ый (который работает со строкой) почти в 1.3 раза быстрее 2-го
(который работает с числами)'''
def solution1(s): 
    a = [int(i) for i in s]
    return sum(a[:3]) == sum(a[3:]) 

def solution2(s):  
    a = int(s)  
    sum_left = 0
    sum_right = 0 
    for i in range(6):
        if i<3:
            sum_right += a // 10**i % 10
        else:
            sum_left  += a // 10**i % 10  
    return sum_left == sum_right 


def random_string(ln=6):  
    return ''.join(random.choice(string.digits) for i in range(ln))

for N in range(3,10):
    print(' --- launch with data size 10^%s --- ' % N)
    sample = [random_string() for i in range(10**N)]

    start_time = time.time()
    for i in sample:
        solution1(i)
    time_of_sol1 = (time.time() - start_time)*1000
    print("solution #1: %s milliseconds" % time_of_sol1)

    start_time = time.time()
    for i in sample:
        solution2(i)
    time_of_sol2 = (time.time() - start_time)*1000
    print("solution #2: %s milliseconds" % time_of_sol2)

    if time_of_sol1<time_of_sol2:
        print('solution #1 is %s times faster than solution #2' % (time_of_sol2/time_of_sol1))
    else:
        print('solution #2 is %s times faster than solution #1' % (time_of_sol1/time_of_sol2))
    print('\n\n')
