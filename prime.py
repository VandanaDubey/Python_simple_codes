"""
def user_choice():
    choice = 'wrong'
    while choice.isdigit() == False:
        choice = input("Please enter a number(0-10): ")
    return int(choice)
"""

"""
"for given prime no code
def prime(num):

    for i in range(2, num):
        if num % i == 0:
            print("no is not prime number")
            break
    else:
        print("no is prime")


prime(int(input("Enter a no: ")))

"""
"""
number = int(input("Enter any number:"))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not prime number")
            break
    else:
        print(number, "is prime number")
"""

"""for a range of nos find prime no """

start = int(input("Enter a starting no: "))
end = int(input("Enter a ending no: "))
print("prime numbers between", start, "and", end, "are: ")
for i in range(start, end+1):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i, end=" ")
