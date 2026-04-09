#1. write a python program to print "Hello, World".
'''print("Hello world")'''


#2. write a python program to take user input and display it.

'''age= int(input ("enter your age:"))
#print("you are ", age," years old")'''


#3. write a python program to swap two numbers.
'''a=int(input("Enter the first number:"))
b= int(input("Enter the second number:"))
temp =a
a=b
b=temp
print("After swapping a=",a,"and b=",b)'''

#4. Write a python program to check if a number is even or odd.
'''num=int(input("Enter a number:"))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")'''

'''print("Even" if int(input("Enter a number:"))%2==0 else "Odd")'''

#5. Write a python program to find the largest of three numbers.
'''a=int(input("Enter thre first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter third number:"))

if a>b and a>c:
    print("the largest number is:",a)
elif b>a and b>c:
    print("the largest number is:",b)
else:
    print("the largest number is:",c)'''

#6. wite a python program to calculate the factorial of a number.
'''num = int(input("enter a number: "))
factorial = 1
if num < 0:
    print("factorial does not exist for negative numbers")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
''    print("the factorial of", num, "is", factorial)'''


#7. Write a python program to generate Fibonacci series.

'''n=int(input("enter the number of terms:"))
fib=[0,1]
for i in range(2,n):
    fib.append(fib[i-1]+fib[i-2])
    print("fibonacci series:",fib)'''

#8. write a program to  reverse a number.
'''num=int(input("enter the number:"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("the reversed number is:",rev)'''

#9. write a python program to check if a number is prime or not.
'''num=int(input("enter the number:"))
if num<=1:                                            #if the number is less than or equal to 1, it is not prime
    print("the number is  not prime")
else:
    for i in range(2,num):                           #check if the number is divisible by any number from 2 to num-1
        if num%i==0:                                 #if the number is divisible by any number, it is not prime         
            print("the number is not prime")
            
    else:        
        print("the number is prime")'''

#10. write a python program to find the sum of digits of a number.
'''n=int(input("enter the number:"))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print("the sum of digits is:",sum)'''

#11. write a program to reverse a string.
'''s=input("enter the string:")
print("the reversed string is:",s[::-1])'''


#12. write a program to check if a string is palindrome or not.
'''s=input("enter the string:")

if s==s[::-1]:
    print("the string is palindrome")
    
else:
    print("the string is not palindrome")    
print("the reversed string is:",s[::-1])'''

#13. write a program to count the number of vowels  and consonants in a string.
'''s=input("enter the string:")
vowels='aeiouAEIOU'
v=0
c=0
for i in s:
    if i in vowels:
      v+=1
        
    else:
        c+=1
print("the number of vowels is:",v)
print("the number of consonants is:",c)'''

#14. write a program to find the length of a string without using built-in functions.
'''s=input("enter the string:")
length=0
for i in s:
    length+=1   
    
print("the length of the string is:",length)'''


#15. write a program to remove all spaces from a string.
'''s=input("enter the string:")
s=s.replace(" ","")
print("the string without spaces is:",s)'''


#16. write a  python program to count occurance of a substring
'''string = input("Enter string: ")
sub = input("Enter substring: ")

print(string.count(sub))

or'''

'''s=input("enter the string:")
sub=input("enter the substring:")
count=0
for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)]==sub:
         count+=1

print("The number of occurrences of the substring is:", count)'''

#17. write a python program to convert a string into uppercase.
'''s=input("enter the string:")
s=s.upper()
print("the string in uppercase is:",s)'''

#18. write a pyhton program to replace vowels with *.
'''s=input("enter a string:")
vowels='aeiouAEIOU'
for i in s:
    if i in vowels:
        s=s.replace(i,'*')

print("the string with vowels replaced is:",s)'''

#19.  write a python program to check if two strings are anagrams.

'''s1=input("enter the first string:").lower()
s2=input("Enter the second sstring:").lower()
if sorted(s1)==sorted(s2):
 print("the strings are anagrams")
else:
 print("the striongd are not anagrams")'''

#20. write a python program to find the forst non-repeating character in a string.
'''s=input("Enter the string:")
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for ch in s:
    if freq[ch]==1:
        print("the first non-repeating character is:",ch)
        break'''

#21. write a python program to find the largest element in a list.
'''l = input("Enter numbers: ").split()

lst = []

for num in l:
    lst.append(int(num))

max_val = lst[0]

for num in lst:
    if num > max_val:
        max_val = num

print("Largest element:", max_val)'''

#22. writte a python program to find the smallest element in a list.
'''s = input("Enter numbers: ").split()

lst = []

for num in s:
    lst.append(int(num))

min_val = lst[0]

for num in lst:
    if num < min_val:
        min_val = num

print("Smallest element:", min_val)'''


#23. write a python program to calculate the sum of all elements in a list.
'''s=input("Enter numbers:").split()
lst=[]
for num in s:
    lst.append(int(num ))
sum=0
for i in lst:
    sum+=i
print("the sum of all elements in the list is:",sum)'''

#24. write a ppython program to remove duplicates from a list.
'''lst = [int(x) for x in input("Enter numbers: ").split()]

seen = []
duplicates = []

for num in lst:
    if num in seen:
        if num not in duplicates:
            duplicates.append(num)
    else:
        seen.append(num)

print("Duplicates:", duplicates)'''

#25. write a python program to sort a list in ascending order.
'''list=[int(x) for x in input("Enter numbers: ").split()]
print(list)
list.sort()
print("the sorted list is:",list)'''


#26. write a python program to sort a list in descending order.
'''list=[int(x) for x in input("Enter numbers: ").split()]
print(list) 
list.sort(reverse=True)
print("the sorted list in descending order is:",list)'''

#27 write a python program to find the second largest element in a list.
'''list=[int(x) for x in input("enter numbers:").split()]
max_val = max(list)
second_max = None
for num in list:
    if num != max_val:
        if second_max is None or num > second_max:
            second_max = num
if second_max is not None:
    print("the second largest element is:",second_max)'''
  

#28 write a python priogram to merge two lists.
'''list1=[int(x) for x in input("enter the first list:").split()]
list2=[int(x) for x in input("enter the second list:").split()]
merged_list = list1 + list2
print("the merged list is:",merged_list)'''

#29. write a python program to find the common elements between two lists.
'''list1=[int(x) for x in input("enter the first list:").split()]
list2=[int(x) for x in input("enter the second list:").split()]
common_elements = []
for num in list1:
    if num in list2 and num not in common_elements:
        common_elements.append(num)
print("the common elements are:",common_elements)'''

#30. write a python program to rotate a list  by 'k' positions.
'''lst = [int(x) for x in input("Enter numbers: ").split()]
k = int(input("Enter k: "))

k = k % len(lst)

rotated = lst[k:] + lst[:k]

print("Left rotated list:", rotated)'''