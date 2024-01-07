def sum(a, b) -> int:
    return (a + b)

if __name__ == "__main__":
    a = int(input('Enter 1nd number: '))
    b = int(input('Enter 2nd number: '))
    c= sum(a,b)
    print(f'Sum of {a} and {b} is {c}')
