def LinearSearch(lys, element):
    '''перебрать массив и вернуть индекс первого вхождения элемента, когда он найден'''
    for i in range (len(lys)):
        if lys[i] == element:
            return i
            return -1

print(LinearSearch([11,12,13,4,5,2,1], 2))

def BinarySearch(lys, val):
    '''Бинарный поиск работает по принципу «разделяй и властвуй».
    Он быстрее, чем линейный поиск, но требует,
    чтобы массив был отсортирован перед выполнением алгоритма
    Итеративная реализация бинарного поиска'''
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print(BinarySearch([10,20,31,40,10], 40))


def InterpolationSearch(lys, val):
    '''В отличие от бинарного поиска, он не всегда начинает поиск с середины.
    Интерполяционный поиск вычисляет вероятную позицию искомого элемента по формуле:
    index = low + [(val-lys[low])*(high-low) / (lys[high]-lys[low])]
'''
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
        if lys[index] == val:
            return index
            if lys[index] < val:
                low = index + 1;
            else:
                high = index - 1;
            return -1


print(InterpolationSearch([1,2,3,4,5,6,7,8], 6))
