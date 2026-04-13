#61. write A python program to define a function that returns the square of a number.
'''def square(n):
    return n**2
num=int(input("enter the number:"))
print("the square of the number is:",square(num))'''


#62 Write a python program to define a function if a number is prime.
'''def is_prime(n):
    if n<=1:
        print("the number is not prime")
    for i in range(2,n):
        if n%i==0:
            print("the number is not prime")
            break  
    else:
        print("the number is prime")
   
num=int(input("enter the number:")) 
is_prime(num)'''

#63. Write a python program to define a function that calculates the factorial of a number using recursion.
'''def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("enter the number:"))
print("{}! is {}".format(num,factorial(num)))'''

#64.  write a python program tom define a function that finds the maximum of 3 number:
'''def max(a,b,c):
    if a>b and a>c:
        return a    
    elif b>a and b>c:
        return b
    else:
        return c
a=int(input("enter first number:"))
b=int(input("enter second number:"))    
c=int(input("enter third number:"))
print("the maximum number is:",max(a,b,c))'''

#65 write a python program to define a function that returns reverse of a string.
'''def reverse_string(s):
    return s[::-1]
string=input("enter the string:")
print("the reverse of the string is:",reverse_string(string))'''

#66. write a python program tp define a function that counts the number of vowels in a string.
'''def count_vowels(s):
    count=0
    for i in s:
        if i in"aeiouAEIOU":
            count+=1
    return count
s=input("Enter the string:")
print("the number of vowels in the string is:",count_vowels(s))'''


#67. write a  python program to define a function that check if a string is palindrome
'''def palindrome(s):
    if s==s[::-1]:
        print(" the string is a pallindrome")
    else:
        print("the string is not a palindrome")
s=input("enter the string:")
palindrome(s)''' 

#68. Write a python progrma to define a function that return sthe sum of the digits of the number
'''def sum(n):
  total=0
  while n>0:
    digit=n%10
    total+=digit
    n=n//10
  return total
  
n=int(input("Enter the number:"))
sum(n)
print("sum of digits is:",sum(n))'''

#69. write a pyrhon program to define a function that genrates fibonacci series upto 'n'

'''def fibonacci(n):
    fib=[0,1]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib
n=int(input("enter the number of terms:"))
print("the fibonacci seires is:",fibonacci(n))'''

#70 write a python program to define a function that calculates the power of a number.

'''def calculate(a,b):
    result=1
    for i in range(b):
     result=result*a
    return result
a=int(input("enter the base:"))
b=int(input("enter the power:"))
 
 
print("the power of a is:",calculate(a,b))'''


#51 write a python to print multiplication table of a number
'''n=int(input("Enter the number:"))
for i in range(1,11):
    result=n*i
    print("the table is:",result)'''

#52 write a python program to print all even numbers from 1 to 100.
'''for i in range(1,101):
    if i%2==0:
        print(i, end =' ,')'''

#53.write a python program to print all odd numbers from 1 to 100:
'''for i in range(1,101):
    if i%2==1:
        print(i,end=',')'''

#54. wrrite a python program to calculate the sum of first 'n' natural numbers 
'''n=int(input("Enter the n natural numbers:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("the sum of  natural numbers is {}".format(sum))'''

# 55 write a program to print pyramid patterns of stars
'''n=int(input("Enter the number of rows"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    for j in range(2*i-1):
        print('*',end='') 
    print()'''

#56. write a python program to print an inverted pyramids of stars.
'''n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for j in range(i-1):
        print(" ",end='')
    for j in range(2*(n-i)+1):
        print('*',end='')
    print()'''    

#57 write a python program to print Pascal's triangle.
'''n=int(input("enter the number of rows:"))

for i in range(n):
    for j in range(n-i):
        print(" ",end='')
    value=1
    for j in range(i+1):
        print(value,end='')
        value= value * (i-j)//(j+1)
        
    print()'''        
#58. write a python program to print Floyd's triangle.
'''n=int(input("Enter the number of rows:"))
num=1
for i in range(1,n+1):
    for j in range(i):
        print(num,end='')
        num+=1
    print()''' 
#59. write a pytjhon program to print prime numbers between 1 and 100.
'''for num in range(2, 101):
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")'''

#60. Write a python program to print numbers divisible by 3 and 5 upto 100.
'''i=1
while i<=100:
    if i%3==0 and i%5==0:
        print(i , end=' ,')
    i+=1'''

#161 Write a python program to check if list is empty or not.
'''l=input("enter the list elements:").split()
if not l:
    print("list is empty")
else:
    print(l)
    print(len(l))'''

#162 write a python progrma to check if a string is empty.

'''s=input("Enter the string character:")
if not s:
    print("String is empty")
else:
    print("String is  not empty")
    print(len(s))'''

#163 Write a program to check if a tuplpe is empty.
'''t = tuple(input("Enter elements: ").split())

if not t:
    print("Tuple is empty")
else:
    print("Tuple is not empty")
    print(len(t))'''

#164 Write a python program to check if a dictionary is empty.

''''d={}
n=int(input("enter the elements:"))
for i in range(n):
    key=input("enter key:")
    value=input("enter value:")
    d[key]=value
print(d)
if not d:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")'''

#165 write a Python program to remove all elemnts from list

'''l=list(map(int,input("enter the list elemnts:").split()))
print(l)
print()
l.clear()
print(l)'''

#166 write a Python program to remove all elemnts from dictionary
'''d={}
n=int(input("enter the elements:"))
for i in range(n):
    key=input("enter key:")
    value=input("enter value:")
    d[key]=value
print(d)

print()

d.clear()
print(d)'''

#167  write a Python program to remove all elemnts from set.

'''s = set(map(int, input("Enter elements: ").split()))
print(s)

print()
s.clear()
print(s)'''

#168 write a Python program to copy a list.

'''l1=['harsh',123 ,178,'Virat']
print(l1)
print("id of l1=",id(l1))
print()
l2=l1.copy()
print(l2)
print("id of l2=",id(l2))'''

#169 write a Python program to copy a dictionary.
'''d1={'Name':'Harsh','Age':22}
print("d1=",d1)
print("id of d1=",id(d1))
print()
d2=d1.copy()
print("d2=",d2)
print("id of d2=",id(d2))'''

#170 write a Python program to copy a Set.
'''s1={'Harry',45,'True',389,35.5}
print("s1=",s1)
print("id of s1=",id(s1))
print()
s2=s1.copy()
print("s2=",s2)
print("id of s2=",id(s2))'''

#171 Write a python program to reverse a list.

'''l=list(map(int,input("Enter the elements").split()))
print("the original list is=",l)
print()
l.reverse()
print("the reverse list is =",l)'''

#172  Write a python program to reverse a tuple.
'''t=tuple(map(int,input("Enter the elements").split()))
print("the original tuple is=",t)
print()
rev=tuple(reversed(t))
print("the reverse tuple is =",rev)'''

#173 Write a python program to reverse a dictionary.
'''d={}
n=int(input("enter the elements:"))
for i in range(n):
    key=input("enter key:")
    value=input("enter value:")
    d[key]=value
print(d)

rev = dict(reversed(list(d.items())))
print(rev)'''

#174 Write a python program to reverse a dictionary.
'''s = set(map(int, input("Enter elements: ").split()))
print(s)

print()
l = list(s)
l.reverse()

rev = set(l)
print(rev)'''

#175 Write a Python program to words in sentence
'''s=input("Enter the sentence:")
words=s.split()
rev=words[::-1]
result=" ".join(rev)
print(result)'''

#176 Write a python program to characters in each word of sentence.
'''s=input("Enter the sentence:")
print(s)

s=s[::-1]
print(s)'''

#177 Write a python program to reverse digits of a number.
'''n=int(input("enter the numbers:" ))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("reversed number is:",rev)'''

#179 Write a program to reverse the elements of nested list
'''l = [[1, 2], [3, 4], [5, 6]]

print("Original:", l)

l = [sub[::-1] for sub in l[::-1]]

print("Reversed:", l)'''

#180. Write a python to reverse the elements in of a nested dictionary.
'''d = {
    'a': {'x': 1, 'y': 2},
    'b': {'z': 3}
}

rev = {}

for outer_k, inner_d in d.items():
    for inner_k, value in inner_d.items():
        rev[value] = outer_k

print(rev)'''

