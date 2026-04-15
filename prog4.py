#131 Write a pyhton program to chek if a character is an alphabet.
'''ch=input("Enter a character:")
if ('a'<=ch<='z') or ('A'<=ch<='Z'):
    print("Character is an alphabet")
else:
    print("Character is not an alphabet")'''

#132 Write a python program to check if a character is a special symbol.
'''ch=input("enter a character:")
if not (('a'<=ch<='z')or('A'<=ch<='z')or('0'<=ch<='9')):
    print("Character is a special symbol:")
else:
    print("Character is not a special symbol")'''

#133 Write a python program to count uppercase letters in a string.
'''s=input("enter the string:")
count=0
for i in s:
    if'A'<=i<='Z':
        count+=1
print("Number of uppercase letters in the string:",count)'''

#134 Write a python program to count lowercase letters in a string.
'''s=input("enter the string:")
count=0
for i in s:
    if'a'<=i<='z':
        count+=1
print("Number of lowercase letters in the string:",count)'''

#135 Write a python program to counts digits in a string.
'''s=input("Enter the String:")
count=0
for i in s:
    if '0'<=i<='9':
        count+=1
print("Number of digits in the string:",count)'''

#136 Write a python program to count special characcters in a string.
'''s=input("Enter the string:")
count=0
for i in s:
    if not(('a'<=i<='z')or('A'<=i<='z')or('0'<=i<='9')):
        count+=1
print("Number of special characters in the string:",count)'''

#137 Write a python progrma to remove punctuation from a string.
'''import string
s=input("Enter the string:")
result=""
for i in s:
    if i not in string.punctuation:
        result+=i
print("String after removing punctuation:",result)'''

#138 Write a python program to replace spaces with hyphens in a string.
'''s=input("Enter the string:")
result=""
for i in s:
    if i==' ':
        result+='-'
    else:
        result+=i
print("Strings after replacing spaces with hyphens:",result)'''

#139 Write a python program to split a  string into words.
'''s=input("Enter the string:")
words=s.split()
print("Words in string",words)'''

#140 Write a python program to join words into a senrence.
'''words=input("Enter the words seperated by spaces:")
sentence=' '.join(words.split())
print("Sentences after joining words",sentence)'''

#151 Write a python program to simulate tossing a coin.
'''import random
toss=random.choice(['Heads','Tails'])
print("coin toss result:",toss)'''

#152 Write a python program to generate a ranndom password
'''import random
import string
def password(length):
    ch=string.ascii_letters+string.digits
    result=''.join(random.choice(ch) for i in range(length))
    return result
length=int(input("Enter the length of password:"))
print("Generated passsword:",password(length))'''

#153  Write a python program to generate a random otp.
'''import random
def otp(length):
    digits='0123456789'
    result=''.join(random.choice(digits) for i in range(length))
    return result
length=int(input("Enter the length of otp:"))
print("Generated otp:",otp(length))'''

#154 Write a python program to generate a random prime number
'''import random

primes = []

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print("Random prime number:", random.choice(primes))'''

#155 Wrtie a python program to generate a random even number.
'''import random

def even_number():
    k = random.randint(1, 1000)   # internal range
    return 2 * k

print("Random even number:", even_number())'''

#156 Write a python program to generate a random odd number.
'''import random
def odd_number():
    k=random.randint(1,1000)
    return 2*k+1
print("Random odd number:",odd_number())'''

#157 Write a python program to generate a random string of a given length.
'''import random
import string 
def random_string(length):
    letters=string.ascii_letters
    result=' '.join(random.choice(letters) for i in range(length))
    return result
length=int(input("Enter the length of a random string:"))
print("Generated random string is:",random_string(length))'''

#158 Write a python program to generate a alphanumeric string of a given length.
'''import random
import string
def alpha_numeric(length):
    ch=string.ascii_letters+string.digits
    result=''.join(random.choice(ch) for i in range(length))
    return result
length=int(input("Enter the length of alphanumeric string:"))
print("Generated alphanumeric string is:",alpha_numeric(length))'''


#159 write a python program to generate a random floating point numbers.
'''import random
def random_float():
    return random.uniform(0.0, 1.0)
print("Random floating point number:", random_float())'''

#160 Write a python progrma to generate random numbers within a specific range.
'''import random
print("Random number between 1 and 100:", random.randint(1, 101))'''



#181 Write a python program to check if a number is prime using function.
'''def is_prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num=int(input("Enter the number:"))
if is_prime(num):
    print("The number is prime")
else:
    print("The number is not prime")'''

#182 Write a python program to check if a string is palindrome using function.
'''def is_palindrome(s):
    return s[::-1]==s
s=input("Enter the string:")
if is_palindrome(s):
    print("The string is palindrome")
else:
    print("The String is not palindrome")'''


#183 Write a python program to check if a number is Armstrong  using function.
'''def is_armstrong(num):
    digits=len(str(num))
    sum=0
    for i in str(num):
        sum+=int(i)**digits
    return sum==num
num=int(input("Enter the number:"))
if is_armstrong(num):
    print("The number is armstrong")    
else:    
    print("The number is not armstrong")'''

#184 Write a python program to check if a number is perfect using function.
'''def is_perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum==n
n=int(input("Enter the number:"))
if is_perfect(n):
    print("The number is perfect")
else:
    print("The number is not perfect")'''

#185 Write a python program to check if a number is palindrome using function.
'''def is_palindrome(num):
    rev=0
    temp=num
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    return temp==rev
num=int(input("Enter the number:"))
if is_palindrome(num):
    print("The number is palindrome")   
else:
    print("The number is not palindrome")'''

#186 Write a python program to check if a string is anagram using function.
'''def is_anagram(s1,s2):
    return sorted(s1)==sorted(s2)
s1=input("Enter the first string:")
s2=input("Enter the second string:")
if is_anagram(s1,s2):
    print("The string is anagram")
else:
    print("The string is not anagram")'''

#187 Write a python program to check if a string is pangram using function.
'''def is_pangram(s):
    alphabet=set('abcdefghijklmnopqrstuvwxyz')
    return alphabet.issubset(set(s.lower()))
s=input("Enter the string:")
if is_pangram(s):
    print("The string is pangram")
else:
    print("The string is not pangram")'''

#188 Write  a python program to check idf a string contains only digits using function.
'''def is_digit(s):
    return s.isdigit()
s=input("Enter the string:")
if is_digit(s):
    print("The string contains only digits")
else:
    print("The string does not contain only digits")'''

#189 Write  a python program to check idf a string contains only alphabets using function.
'''def is_alpha(s):
    return s.isalpha()
s=input("Enter the string:")
if is_alpha(s):
    print("The string contains only alphabets")
else:
    print("The string does not contain only alphabets")'''

#190 Write  a python program to check idf a string contains only alphanumerics using function.
'''def is_alphanumeric(s):
    return s.isalnum()
s=input("Enter the string:")
if is_alphanumeric(s):
    print("The string contains only alphanumerics")
else:
    print("The string does not contain only alphanumerics")'''


#111  Write a python program to check if a year is a leap year
'''def is_leap(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
year=int(input("Enter the year:"))
is_leap(year)'''

#112 write a python program to calculate simple interest.
'''def simple_interest(p,r,t):
    return (p*r*t)/100
p=float(input("Enter the principal amount:"))
r=float(input("Enter the rate of interest:"))
t=float(input("Enter the time in years:"))
si=simple_interest(p,r,t)
print("The simple interest is:",si)'''

#113 write a python program to calculate compound interest.
'''def compound_interest(p,r,t):
    return p*(1+r/100)**t
p=float(input("Enter the principal amount:"))
r=float(input("Enter the rate of interest:"))
t=float(input("Enter the time in years:"))
ci=compound_interest(p,r,t)
print("The compound interest is:",ci)'''

#114 Write a python program to convert Celcius to fahrenhit.
'''def cel_to_fah(c):
    return (c*9/5+32)
c=float(input("Enter the temperature in Celcius:"))
f=cel_to_fah(c)
print("The temperature in fahrenhit is:",f)'''

#115 Write a python program to convert Celcius fahrenhit to Celcius.
'''def fah_to_cel(f):
    return(f-32)*5/9
f=float(input("Enter the temperature in Fahrenhit:"))
c=fah_to_cel(f)
print("The temperature in Celcius is:",c)'''

#116 Write a python progrma to calculater the area of a circle.
'''import math
def area_of_circle(r):
    return math.pi*r**2
r=float(input("Enter the radius of the circle:"))
area=area_of_circle(r)
print("The area of thr circle is:",area)'''

#117 Write a python program to calculate the area of a rectangle.
'''def area_of_rectangle(l,w):
    return l*w
l=float(input("Enter the length of the rectangle:"))
w=float(input("Enter the width of the rectangle:"))
area=area_of_rectangle(l,w)
print("The area of thr rectangle is:",area)'''

#118 Write a python program to calculate the area of a triangle.
'''def area_of_triangle(b,h):
    return 0.5*b*h
b=float(input("Enter the base of the triangle:"))
h=float(input("Enter the height of the triangle:"))
area=area_of_triangle(b,h)
print("The area of thr triangle is:",area)'''

#119 Write a python program to calculate perimeter of a square.
'''def perimeter_of_square(s):
    return(4*s)
a=float(input("Enter the side of the square:"))
perimeter=perimeter_of_square(a)
print("The perimeter of the square is:",perimeter)'''

#120 Write a python program to calculate perimeter of a rectangle.
'''def perimeter_of_rec(l,w):
    return 2*(l+w)
l=float(input("Enter the length of the rectangle:"))
w=float(input("Enter the width of the rectangle:"))
perimeter=perimeter_of_rec(l,w)
print("The perimeter of the square is:",perimeter)'''