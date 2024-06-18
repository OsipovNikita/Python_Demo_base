def out(str):
    count = len(str)
    print(count)
    def nestout():
        count = len(str)
        count +=1
        print(str, count)
    nestout()

out("dfcz")

def out(str):
    count = len(str)
    print(count)
    def nestout():
        nonlocal count
        #count = len(str)
        count +=1
        print(str, count)
    nestout()

out("dfcz")


