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
