def menu():
    print('''
    Fibonacci series
    1.Print n number of terms
    2.Print up to a value
    3.Print between start and end value
    0.Exite
    ''')
    ch = input("Enter your choise: ")
    return ch


def terms(a, b):
    n = int(input("enter number of terms to print: "))
    for i in range(n):
        c = a + b
        print(c, end="")
        a, b = b, c
    print()


def value(a,b):
    v = int(input("Enter valuer to print up to: "))
    c = a + b
    while c <= v:
        print(c, end="")
        a, b = b, c
        c = a + b
    print


def terms_value(x,y):
    s = int(input("Enter the starting point: "))
    t = int(input("Enter the end point: "))
    c = 0
    for i in range(s):
        c = c+t
        print(c)

    # s = int(input("Enter the starting point: "))
    # for i in range(s):
    #     c = a + b
    #     print(c, end="")
    #     a, b = b, c
    #
    # print()
    # t = int(input("Enter the end point: "))
    # c = a + b
    # while c <= t:
    #     print(c, end="")
    #     a, b = b, c
    #     c = a + b
    # print


# -----------Main program--------------
x, y = -1, 1
ch = menu()
while ch != "0":
    if ch == "1":
        terms(x, y)
    elif ch == "2":
        value(x, y)
    elif ch == "3":
        terms_value(x, y)
    else:
        print("Wrong calue entered.")
    ch = menu()
