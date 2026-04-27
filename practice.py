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

from abc import ABC, abstractmethod

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
    print(f"{exam.subject} | Format: {exam.question_format()} | Eval: {exam.evaluate()}")