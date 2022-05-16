'''
a = int(input("Enter the first number of the series 0: "))
b = int(input("Enter the second number of the series 1: "))
n = int(input("Enter the number of terms needed: "))
print(a, b, end=" ")
while(n-2):
    c = a+b
    a = b
    b = c
    print(c, end=" ")
    n = n-1
'''
a = 0
b = 1
n = int(input("Enter the number of terms needed: "))
print(a, b, end=" ")
while(n-2):
    c = a+b
    a = b
    b = c
    print(c, end=" ")
    n = n-1
