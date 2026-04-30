'''def convert_temperature(temp,unit):
    if unit=='C':
        return temp*9/5+32
    elif unit=='F':
        return (temp-32)*5/9
    else:
        return None
print(convert_temperature(25,'C'))
print(convert_temperature(77,'F'))'''

#password checker.
'''def is_strong_password(password):
    if len(password)<8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True
print(is_strong_password('Harsh@2005'))'''

'''def calculate_total_cost(items):
    total=0
    for item in items:
        total+=item['price']*item['quantity']
        return total
items=[
    {'name':'apple','price':15,'quantity':4000},]
print(calculate_total_cost(items))'''

'''def is_palindrome(string):
    
    if string==string[::-1]:
       return True
    else:
        return False
string=input("Enter the string:")
print(is_palindrome(string))'''

'''def valdate_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False
email=input("Enter the email:")
print(valdate_email(email))'''


'''import json
data={'name':'Harsh','age':22}
json_str=json.dumps(data)
print(json_str)
print(type(json_str))

parsed_data=json.loads(json_str)
print(parsed_data)
print(type(parsed_data))'''

'''from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class Email(Notification):
    def send(self, message):
        print("Email sent  {}".format(message))

class SMS(Notification):
    def send(self, message):
        print("SMS sent  {}".format(message))

e=Email()
print(e.send("Your order is confirmed!"))

s=SMS()
print(s.send("OTP: 4521"))

Email().send("Your order is confirmed!")
SMS().send("OTP: 4521")'''

'''n=int(input("enter the rows:"))
for i in range(1,n+1):
    print('*',end='')'''

'''n=int(input("enter the rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end=' ')
    print()  '''

'''n=int(input("enter the rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()  '''  
'''n=int(input("enter the rows:"))
for i in range(n,0,-1):
    
    print('*'*i)'''

'''n=int(input("enter the rows:"))
for i in range(1,6):
    for j in range(1,i+1):
    
      print(i,end=' ')

    print()'''
'''n = int(input("Enter the rows: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()'''

'''n=1
for row in range(3):
    for col in range(4):
        print(n,end='')
        n+=1
    print()'''

'''n=int(input("enter the rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(j+64),end='')
    print()'''

'''n = int(input("Enter the rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    
    for k in range(2 * i - 1):
        print("*", end="")
    
    print()'''


'''from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


class TextFileHandler(FileHandler):
    def read(self):
        print("Reading Text File")

    def write(self):
        print("Writing Text File")


class JSONFileHandler(FileHandler):
    def read(self):
        print("Reading JSON File")

    def write(self):
        print("Writing JSON File")


class CSVFileHandler(FileHandler):
    def read(self):
        print("Reading CSV File")

    def write(self):
        print("Writing CSV File")


TextFileHandler().read()
TextFileHandler().write()


JSONFileHandler().read()
JSONFileHandler().write()

CSVFileHandler().read()

CSVFileHandler().write()'''
'''l=[int(x) for x in input("enter the elements:").split()]
print(l)
print(type(l))'''

'''list=[x*x for x in range(1,21) if x%3==0 or x%4==0]
print(list)'''

'''l=[int(x) for x in input("enter the elements:").split()]
print(l)
print(type(l))   
t=tuple(l)
    
print(type(t))'''

'''d={100:"apple",101:'mango',102:'orange'}
print(d)

print(d.setdefault(200))
print(d)
print(d.setdefault(300))
print(d)
print(d.setdefault(301,'banana'))
print(d)'''

#Mini application---
'''n=int(input("Enter the number of students:"))
d={}
for x in range(n):
    name=input("Enter the name of student:")
    marks=int(input("Enter the marks of student:"))
    d[name]=marks
print("All student data is inserted successfully")
print(" Student Details")
print("-------------------")
for key,value in d.items():
    print(key,'------>',value)

while True:
    name=input("Enter the name of student to get the marks:")
    if name in d:
        print("Marks of {} ={}".format(name,d[name]))
    else:
        print("Student details not found")
    choice=input("Do you want to continue? (Yes/No):")
    while choice.lower() not in ['yes','no']:
        choice=input("Invalid choice ... Pleaase try again with valid options (Yes/No):")
    if choice.lower() =='no':
      break
print("Thanks for using our application... Visit Again")'''

'''class Restaurant:
    def prepare_order(self):
        print("Preparing generic order")

class PizzaPlace(Restaurant):
    def prepare_order(self):
        print("Baking a fresh Pizza 🍕")

class BiryaniHouse(Restaurant):
    def prepare_order(self):
        print("Cooking Biryani 🍛")

class SushiBar(Restaurant):
    def prepare_order(self):
        print("Rolling Sushi 🍣")

orders = [PizzaPlace(), BiryaniHouse(), SushiBar()]
for r in orders:
    r.prepare_order() '''  # Polymorphic call

'''from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, base):
        self.name = name
        self.base = base

    @abstractmethod
    def salary(self):
        pass

    def display(self):
        print(f"{self.name}: ₹{self.salary()}")

class FullTime(Employee):
    def salary(self):
        return self.base + 5000   # HRA bonus

class PartTime(Employee):
    def salary(self):
        return self.base * 0.5    # Half pay

class Contractor(Employee):
    def salary(self):
        return self.base + 2000   # Project bonus

employees = [FullTime("Alice", 40000),
             PartTime("Bob", 30000),
             Contractor("Carol", 35000)]

for e in employees:
    e.display()'''

'''from abc import ABC, abstractmethod

class Exam(ABC):
    def __init__(self, subject):
        self.subject = subject

    @abstractmethod
    def question_format(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

class MCQExam(Exam):
    def question_format(self):
        return "Multiple Choice Questions"
    def evaluate(self):
        return "Auto-graded by system"

class DescriptiveExam(Exam):
    def question_format(self):
        return "Long Answer Questions"
    def evaluate(self):
        return "Manually graded by teacher"

class CodingExam(Exam):
    def question_format(self):
        return "Programming Problems"
    def evaluate(self):
        return "Evaluated by test cases"

exams = [MCQExam("Math"), DescriptiveExam("History"), CodingExam("Python")]
for exam in exams:
    print(f"{exam.subject} | Format: {exam.question_format()} | Eval: {exam.evaluate()}")'''


# 
''''def is_prime(n):
    if n<=1:
        print("the number is not a prime")
    for i in range(2,n):
        if n%i==0:
            print("the number is not a prime ")
           
        else:
            print("the number is prime:")
            break
num=int(input("enter the number:"))
is_prime(num)'''

'''def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("enter the number:"))
print("the factorial of {} is {} ".format(num,factorial(num)))'''

'''l=lambda a:a**2
print("sq ={}".format(l(4)))'''

'''lst=[23,45,65,44,223,446,7788,99,778,990,554,59]
print("original list=",lst)
l1=list(filter(lambda n:n%2==1,lst))
print(l1)'''

'''from random import*
from math import*
for i in range(1,1000):
  print(floor(random()*10))'''

''''import random
num=random.randint(1,100)
print(num)'''

'''import random
a=int(input("enter the lower limit:"))
b=int(input("enter the higher limit:"))
num=random.randint(a,b)
print(num)'''

'''import random
dice=random.choice(['Heads','Tails'])
print(dice)'''

'''import random
import string
def password(length):
    ch=string.ascii_letters+string.digits
    result=''.join(random.choice(ch) for i in range(length))
    return result
length=int(input("enter the length of password:"))
print(password(length))'''

'''import random
import string
def otp(length):
    ch=string.digits
    result=''.join(random.choice(ch) for i in range(length))
    return result
length=int(input("enter the length:"))
print(otp(length))'''


'''import random
print(random.randint(1,100))''' 

'''for i in range(1,5):
    for j in range(1,i+1):
        print(chr(j+64),end='')
    print()

for i in range(1,6):
    for j in range(1,4-i+1):
        print(chr(j+64),end='')
    print()'''

'''class Student:
    """I am creating a student class"""
print(Student.__doc__)'''

'''class Student:
    school="Gqt"
    def __init__(self,name):
        self.name=name
s = Student("Harsh")
print(s.school)
print(s.name)'''
 
'''class Student:
    school = "GQT"        # class variable (shared by all)
    
    def __init__(self, name):
        self.name = name  # instance variable (unique to each object)

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school)  # GQT  (same for all)
print(s1.name)    # Alice (unique)
print(s2.name)'''    # Bob   (unique)

'''class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price
p=Product(10,"RAM",5000)

print('{}\t{}\t{}\t'.format(p.id,p.name,p.price))'''

'''class Student:
    count=0
    total_gpa=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
        Student.total_gpa+=gpa
    @classmethod
    def get_count(cls):
        return f"total students={cls.count}"
    @classmethod
    def get_gpa(cls):
        if cls.count==0:
            return 0
        else:
            return f"average_gpa={cls.total_gpa/cls.count:.2f}"
    
s1=Student("harry",4.1)
s2=Student("hemu",3.4)
s3=Student("haru",2.1)
s4=Student("harsh",3.1)
print(Student.get_count())
print(Student.get_gpa())'''