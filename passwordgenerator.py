import random

print("welcome to your pasword generator")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNOPQRSTVXYZ!@£$%^&*().,?0123456789"
number = input("amount of passwords to generate: ")
number = int(number)

length = input("your password length")
length = int(length)

print("\nhere are your passwords: ")
for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)