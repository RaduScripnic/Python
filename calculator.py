def menu():
    print('''
    Main menu
    1.Multiply
    2.Power
    3.Factorial
    0.Exit
    ''')
    ch = int(input("Enter your choise: "))
    return ch

def multiply(a, b):
    a = int(input("enter first integer "))
    b = int(input("enter second integer"))
    c = 0
        if abs(a) >= abs(b):
            max = abs(a)
            min = abs(b)
        else:
            max = abs(b)
            min = abs(a)
        for i in range(min):
            c = c + max
        if a < 0: c = -c
        if b < 0: c = -c
        return c
    # def power(a,b):
    # def factorial(a,b):



#-------------main program -------------
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