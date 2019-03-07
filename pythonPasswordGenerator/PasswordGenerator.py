import random
print("Enter length for your password you want to generate\ns")
x = input("An integer number:")
password = ''
code='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?_-&!#$'

for c in range(int(x)):
    password += random.choice(code)
print(password)