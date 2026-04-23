# 141 Write a python program to check if a number is divisible by another number.
'''num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1%num2==0:
    print("{} is divisible by {}".format(num1,num2))
else:
    print("{} is not divisible by {}".format(num1,num2))'''

#142 Write a python program to calculate square root of a number.
'''from math import sqrt
n=int(input("Enter the number:"))
result=sqrt(n)
print("The square root of {} is {}".format(n,result))'''


#143 Write a python program to calculate cube root of a number.

'''n=int(input("Enter the number:"))
if n>=0:
    print(n**(1/3))
else:
    print((-n)**(1/3))'''

#144 Write a python program to calculate power using 'pow()' function.
'''import math
base=int(input("Enter the base number:"))
exponent=int(input("Enter the exponent:"))
print(math.pow(base,exponent))'''

#145 Write a python program to calculate absolute value of a number.
'''n=int(input("Enter the number:"))
absolute_value=abs(n)
print("The absolute value of {} is {}".format(n,absolute_value))'''

#146 Write a python program to generate a random number.
'''import random
num = random.randint(1, 1000)
print("Random number:", num)'''

#147 Write a python program to generate a random integer between two numbers
'''import random

a = int(input("Enter lower limit: "))
b = int(input("Enter upper limit: "))

num = random.randint(a, b)

print("Random number between", a, "and", b, "is:", num)'''

#148 Write a python program to shuffle elements of a list.
'''import random
lst=[10,44,34,56,23,556,775,8966,554]
print("the original list",lst)
random.shuffle(lst)
print("shuffled list is:",lst)'''

#149 Write a python program to pick a random element from a list.
'''import random
lst=[10,44,34,56,23,556,775,8966,554]
print("the random element from a list is:",random.choice(lst))'''

#150 Write a python program to stimulate rolling a dice.
'''import random
while True:
    input("press enter to roll the dice...")
    dice=random.randint(1,6)
    print("dice result =",dice)

    choice=input("Do you want to play again? (yes/no):")
    if choice.lower()!="yes":
        break'''