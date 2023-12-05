import random
c = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
l = int(input("Enter length of password: "))
p = ""

for a in range(l):
    p+=random.choice(c)
print(p)