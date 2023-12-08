myfile = open("myfile3.txt")

print(myfile.__next__()) #  файл является итерируемым объектом
print(myfile.readline())
print(myfile.__next__())
myfile.seek(0)
for line in myfile:
    print((line.rstrip()))

myfile.close()


with open("myfile3.txt") as fm:
    print(fm.__next__())
    for line in fm:
        print((line.rstrip()))

print(fm.__next__())  # ValueError: I/O operation on closed file.