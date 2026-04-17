#121 Write a python program to calculate the perimeter of a circlr:
'''import math

from networkx import radius
def perimeter_of_circle(radius):
    return 2*math.pi*radius
radius=float(input("enter the radius of the circle:"))
print("The perimeter of the circle is:",perimeter_of_circle(radius))'''

#122 Write  a python program to calculate volume of cube:
'''def cube_volume(a):
    return a**3
a=float(input("Enter the side length of the cube:"))
print("The volume of the cube is:",cube_volume(a))'''

#123 Write a python program to calculate volume of cylinder.
'''import math
def cylinder_volume(radius,height):
    return math.pi*radius**2*height
radius=float(input("Enter the radius of the cylinder:"))
height=float(input("Enter the height of the cylinder:"))
print("The volume of cylinder is:",cylinder_volume(radius,height))'''

#124 Write a python program to calculate volume of sphere.
'''import math
def sphere_voume(radius):
    return (4/3)*math.pi*radius**3
radius=float(input("Enter the radius of the sphere:"))
print("The volume of the sphere is:",sphere_voume(radius))'''

#125  Write a python program to calculate surface area of a cube.
'''def cube_surface(a):
    return 6*a**2
a=float(input("Enter the side length of the cube:"))
print("The surface area of the cube is:",cube_surface(a))'''

#126 Write a python program to calculate surface area of a cylinder.
'''import math
def cylinder_surface_area(r,h):
    return 2*math.pi*r*(r+h)
r=float(input("Enter the radius of the cylinder:"))
h=float(input("Enter the height of the cylinder:"))
print("The surface area of the cylinder is:",cylinder_surface_area(r,h))'''

#127 Write a python program to calculate surface area of a sphere.
'''import math 
def sphere_surface(r):
    return 4*math.pi*r**2
r=float(input("Enter the radius of the sphere:"))
print("The surface area of the sphere is:",sphere_surface(r))'''


#128 Write a python program to check if a character is a uppercase.
'''def is_upper(char):
    if char.isupper():
        print("the character is uppercase")
    else:
        print("The character is not a uppercase")
char=input("Enter a character:")
is_upper(char)'''

#129 Write a python program to check if a character is a lowercase.
'''def is_lower(char):
    if char.islower():
        print("the character is lowercase")
    else:
        print("The character is not a lowercase")
char=input("Enter a character:")
is_lower(char)'''

#130 Write a python program to check if a character is a digit.
'''def is_digit(char):
    if char.isdigit():
        print("the character is a digit")
    else:
        print("The character is not a digit")
char=input("Enter a digit:")
is_digit(char)'''

#71 Write a python program to calculate factorial using recursion.
'''def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
num=int(input("Enter a number:"))
print("The factorial of {} is {}".format(num,factorial(num)))'''


#72 Write a python program to calculate the fibonacci series using recursion.
'''def fibonacci(n):
    if (n==0 or n==1):
        return n
    else:
      return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the number of terms:"))
for i in range(n):
    print(fibonacci(i), end=" ")'''

#73 Write a python program to find the sum of natural numbers using recursion.
'''def sum(n):
    if n==0:
        return 0
    else: 
        return n+sum(n-1)
n=int(input("Enter the number:"))
print("The sum of natural numbers up to {} is {}".format(n,sum(n)))'''

#74 Write a python program to reverse a string using recursion.
'''def reverse(s):
    if len(s)==0:
        return s
    else:
        return s[-1]+reverse(s[:-1])
string=input("Enter the string:")
print("The reverse of the string is:",reverse(string))'''

#75 Write a python program to check if a string is palindrome using recursion.
'''def is_palindrome(s):
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and is_palindrome(s[1:-1])
string=input("Enter the string:")
print("The string is palindrome:",is_palindrome(string))'''

#76  Write a python program to find the gcd of two numbers using recursion.
'''def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
print("The GCD of {} and {} is {}".format(num1,num2,gcd(num1,num2)))'''

#77 Write a python program to find the lcm of two numbers using recursion.

'''def lcm(a, b, candidate=None):
    if candidate is None:
        candidate = max(a, b)

    if candidate % a == 0 and candidate % b == 0:
        return candidate

    return lcm(a, b, candidate + 1)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("LCM is:", lcm(a, b))'''

#78 Write a python program to calculate the sum of digits using recursuin.
'''def sum(n):
    if n==0:
      return 0
    else:
       return n%10+sum(n//10)
num=int(input("Enter the number:"))
print("The sum of digits is:",sum(num))'''


#79 Write a python program to find the length of a string using recursion.
'''def length(s):
    if s=='':
        return 0
    else:
        return 1+length(s[1::])
string=input("Enter the string:")
print("The length of the string is:",length(string))'''

#80 Write a python program to print numbers from 1 to n using recursion.
'''def print_number(n):
    if n>0:
        print_number(n-1)
        print(n,end=' ')
n=int(input("Enter the number:"))
print_number(n)'''
 
