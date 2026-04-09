#31. write a pythion program to check if a number is armstrong number.
'''n = input("Enter a number: ")

digits = len(n)
total = 0

for i in n:
    total += int(i) ** digits

if total == int(n):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")'''

#32. write a program to check if a number is a perfect number or not.
'''n=int(input("enter the number:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("the number is perfect")
else:
    print("the number is not perfect")'''

#33. write a program to check if a number is a palindrome
'''n=int(input("enter the number:"))
rev=0
temp=n
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
        print("the number is palindrome")
else:
        print("the number is not palindrome")'''

#34. write a python program to gcd of two numbers.
'''a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
gcd=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print("the gcd of {} and {} is {}".format(a,b,gcd))'''

#35. write a program to find lcm of two numbers.

'''a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
gcd=1
for i in range(1, min(a,b)+1):
    if a%i ==0 and b%i==0:
        gcd=i
lcm=(a*b)//gcd
print("the lcm of {} and {} is {}".format(a,b,lcm))'''

#36. write a python progrma to convert decimal to binary.
'''n=int(input("enter the decimal number:"))
binary=""
while n>0:
    remainder=n%2
    binary=str(remainder)+binary
    n=n//2
print("the binary representation is:",binary)'''

#37. write a python program to convert binary to decimal.
'''n=int(input("enter the binary number:"))
decimal=0
power=0
while n>0:
    digit=n%10
    decimal=decimal+digit*(2**power)
    power+=1
    n=n//10
print("the decimal representation is:",decimal)'''

#38. write a python program to generate prime numbers up to n.
'''n=int(input("enter the number:"))

for i in range(2,n+1):
    is_prime=True
   
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        print(i,end=" ")'''

#39. write a python program to find sum of natural numbers up to n.
'''n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print("the sum of natural numbers up to {} is {}".format(n,sum))'''

#40.  write a python program to calcuate the power of a number without usign ** operator.
'''a=int(input("enter the base number:"))
b=int(input("enter the exponent:"))
result=1
for i in range(b):
    result=result*a
print("the result of {} raised to the power of {} is {}".format(a,b,result))'''



#81 write a python program to find the maximum elemrnt in a tuple.
'''t=(3, 5, 1, 8, 2)
max_element = max(t)
print("the maximum element in the tuple is:", max_element)'''


#82. write a python program to find the minimum element in a tuple.
'''t=(3, 5, 1, 8, 2)
min_element = min(t)
print("the minimum element in the tuple is:", min_element)'''

#83. write a python program to convert a list tuple.
'''l=(int(x) for x in input("enter the number of elements in the list:").split())
   print("the list is:",l) 
my_tuple=tuple(l)
print("the tuple is:",my_tuple)'''

#84. write a python program to convert a tuple to a list.
'''t=tuple(int(x) for x in input("enter the number of elements:").split())
print("the tuple is:",t)
list=list(t)
print("the list is:",list)'''

#85 write a python program to find union of two sets.
'''s1=set(int(x) for x in input("enter the elements of the first set:").split())
s2=set(int(x) for x in input("enter the elements of the second set:").split())
union=s1 | s2
print("the union of the two sets is:",union)'''

#86. write a python program to find intersection of two sets.
'''s1=set(int(x) for x in input("enter the elements of the first set:").split())
s2=set(int(x) for x in input("enter the elements of the second set:").split())
intersection=s1&s2
print("the intersewction of s1 & s2 is:",intersection)'''

#87. write a python program to find difference of two sets.
'''s1=set(int(x) for x in input("entrer the elments of the first set:").split())
s2=set(int(x) for x in input("enter the elements of the second set:").split())
diff1=s1-s2
diff2=s2-s1
print("the difference of s1 and s2 is:",diff1)
print("the difference of s2 and s1 is:",diff2)'''

#88. write a python program to check if a set is a subset of another set.
'''s1=set(int(x) for x in input("enter the elements of the first set:").split())
s2=set(int(x) for x in input("enter the elements of the second set:").split())
if s1.issubset(s2):
    print("s1 is a subset of s2")   
else:   
      print("s1 is not a subset of s2")'''

#89. write a python program to remove duplicates from a list  using sets.
'''l=[int(x) for x in input("enter the number of elements in the list:").split()]
print("the list is:",l)
unique_elements=set(l)
print("the unique elements in the list are:",unique_elements)'''

#90 write a python program to count unique elements in a list using sets.
'''l=[int(x) for x in input("enter the number of elements in a list:").split()]
print("the list is:",l)
unique_elements=set(l)
print("the number of unique elements in the list is:",len(unique_elements))'''


#91. write a python program to create a dictionary of student names and marks.
'''n=int(input("enter the number of students:"))
d={}
for i in range(n):
    name = input("enter the name of student:")
    marks=int(input("enter the marks of student:"))
    d[name]=marks
print("the dictionary of student and marks is:",d)'''

#92. Write a python program to access the value from a dictionary.
'''d={'Name':"Virat Kohli", 'Age': 35, 'Country': "India"}
print(d)
for value in d.values():
    print(value)'''

#93. Write a python program to update values in a dictionary.
'''d = {'Name': 'Virat', 'Age': 35}

key = input("Enter key: ")
value = input("Enter value: ")

# try converting to int
if value.isdigit():
    value = int(value)

d[key] = value

print("Updated dictionary:", d)'''

#94 write python program to delete a key from a dictionary.
'''d={100:'Apple',101:'Banana',102:'Orange'}
key=int(input("enter the key to delete:"))
if key in d:
    del d[key]
    print("the updated dictionary is:",d)'''

#95.Write Pyrhon program to merge two dictionaries.
'''d1={'Name':'Virat','Age':36,'sport':'Cricket','Country':'India'}
d2={'Matches':300,'Runs':15000,'Centuries':54}
d3={**d1,**d2}
print("the merged dictionary is:",d3)'''

#96 Write a Python program to count frequency of characters in a string using a dictionary.
'''s=input("enter the string:")
freq={}
for ch in s:
  if ch in freq:
    freq[ch]+=1
  else:
    freq[ch]=1
print("the frequency of characters in the string is:",freq)'''

#97. write a python program to count the frequency of words in a sentence using a dictionary.
'''s=input("enter the sentence:")
freq={}
for word in s.split():
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print("the frequency of words in the sentence is:",freq)'''

#98 Write a python program to find the key with the maximum value in a dictionary.
'''d={'a': 10, 'b': 20, 'c': 15}
max_key = max(d, key=d.get)
print("the key with the maximum value in the dictionary is:", max_key)'''

                  # or#

'''d={'a': 10, 'b': 20, 'c': 15}
max_key=None
max_value=float('-inf')
for key,value in d.items():
    if value>max_value:
        max_value=value
        max_key=key
print("the key with the maximum value in the dictionary is:",max_key)'''


#99 write a python program to sort a dictionary by values.

'''d={'a':100,'b':450,'c':200,'d':50,'e':300,'f':350,'g':40}
sorted_d=dict(sorted(d.items(),key=lambda item:item[1]))
print("the dictionary sorted by values is:",sorted_d)'''

#100. write a pyrhon program to check if a key exists in a dictionary.
'''d={'Name' :'Virat','Age':36,'sport':'Cricket','Country':'India'}
key=input("enter the key to check:")
if key in d:
    print("the key exists in the dictionary")
else:
    print("the key does not exist in the dictionary")'''


'''def largest(a,b,c):
    if a>b and a>c:
        print("the largest number is:",a)
    elif b>a and b>c:
        print("the largest number is:",b)       
    else:
        print("the largest number is:",c)
largest(10,20,15)'''

x='harry'
def func():
    x='rohan'
    print(x)
func()
print(x)


