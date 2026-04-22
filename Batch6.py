#191 Write a python program to check if a string contains only uppercase letters.
'''def is_upper(s):
    return s.isupper()
s=input("Enter the string:")

if is_upper(s):
    print("the string only contains uppercase letters")
else:
    print("the stirng does not contains only uppercase letters")'''


#192 Write a python program to check if a string contains only lowercase letters.
'''def is_lower(s):
    return s.islower()
s=input("Enter the string:")

if is_lower(s):
    print("the string only contains lowercase letters")
else:
    print("the stirng does not contains only lowercase letters")'''

#193 Write a python program to check if string contains only whitespace.

'''def is_space(s):
    return s.isspace()
s=input("Enter the string:")
if is_space(s):
    print("the string only contains whitespaces")
else:
    print("the stirng doesn't contain whitespace only")'''

#194 Write a python program to check if a string contians only special characters.
'''def is_special(s):
    for ch in s:
        if ch.isalnum() or ch.isspace():
            return False
    return True

s = input("Enter the string: ")

if is_special(s):
    print("String contains only special characters")
else:
    print("String does not contain only special characters")'''

#195 Write a python program to check if string contsins both letters and digits.
'''def letters_digits(s):
    has_letter=False
    has_digit=False
    for ch in s:
        if ch.isalpha():
            has_letter=True
        if ch.isdigit():
            has_digit=True
    return has_letter and has_digit
s=input("Enter the stirng:")
if letters_digits(s):
    print("the stirng contains both letters and digits")
else:
    print("the stirng does contains both letters and digits")'''

#196 Write a python program to check if a string contains both uppercase and lowercase letters.
'''def lower_upper(s):
    has_upper=False
    has_lower=False
    for ch in s:
        if ch.isupper():
            has_upper=True
        if ch.islower():
            has_lower=True
    return has_upper and has_lower
s=input("Enter the stirng:")
if lower_upper(s):
    print("the stirng contains both uppercase and lowercase letters.")
else:
    print("the stirng does not contains both uppercase and lowercase letters.  ")'''

#197 Write a python program to check if a string contains both vowels and consonants.

'''def vowels_conso(s):
    vowels='aeiouAEIOU'
    has_vowel=False
    has_consonant=False
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                has_vowel=True
            else:
                has_consonant=True
    return has_vowel and has_consonant
s=input("Enter the stirng:")
if vowels_conso(s):
    print("the stirng contains both both vowels and consonants.")
else:
    print("tthe stirng doesn't contains both both vowels and consonants.  ")'''

#198 Write a python program to check if a string contains repeated characters.
'''s = input("Enter string: ")

freq = {}

for ch in s:
    if ch!='':
      if ch in freq:
        freq[ch] += 1
      else:
        freq[ch] = 1

for ch in freq:
    if freq[ch] > 1:
        print(ch, end=" ")'''

#199 Write a python program to check if a string contains unique characters.
'''s = input("Enter string: ")

freq = {}

for ch in s:
    if ch!='':
      if ch  in freq:
        freq[ch] += 1
      else:
        freq[ch] = 1

for ch in freq:
    if freq[ch] <= 1:
        print(ch, end=" ")'''

#200 Write a python program to check if a string contains all vowels.
'''s=input("Enter the stirng:")
vowels='aeiouAEIOU'
for v in vowels:
    if v in vowels:
        print("the string contians all vowels")
        break
    else:
        print("the does not contains all vowels")
        break'''


#311 Write a python program to implement object-oriented programming with a class and object.

'''class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Salary:", self.salary)
e=Employee(101,'Harsh',100000)
e.display()'''

#312 Write a python progrma to implement inheritance.

'''class Parent:
    def __init__(self):
        print("Parent class executed")
class Child(Parent):
    pass
c=Child()'''

#313 Write a python program to implement multiple inheritance.
'''class Personal:
    def show1(self,name,age):
        self.name=name
        self.age=age
class College:
    def show2(self,usn,branch):
        self.usn=usn
        self.branch=branch
class Details(Personal,College):
      def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("USN:", self.usn)
        print("Branch:", self.branch)
name=input("Enter the student name:")
age=int(input("Enter the age :"))
usn=int(input("Enter the usn :"))
branch =input("Enter the branch name:")

d=Details()
d.show1(name,age)
d.show2(usn,branch)
print(d.display())'''

#314 Write a python program to implement multilevel inheritance.
'''class Employee:
    def show1(self):
        print("I am an Employee at Google")
class Engineer(Employee):
    def show2(self):
        print("I am an Engineer at google")
class Software(Engineer):
   pass
s=Software()
s.show1()
s.show2()'''

#315 Write a python program to implement hierarchical inheritance.
'''class Parent:
    def show(self):
        print("Parent class Executed")

class Child1(Parent):
    def child1_method(self):
        print("Child1 specific method")

class Child2(Parent):
    def child2_method(self):
        print("Child2 specific method")

c1 = Child1()
c2 = Child2()

c1.show()
c1.child1_method()

c2.show()
c2.child2_method()'''

#316 Write a python program to implement hybrid inheritance.
'''class A:
    def method1(self):
        print("class A executed")
class B(A):
    def method2(self):
        print("class B executed")
class C(A):
    def method3(Self):
        print("class c executed")
class D(B,C):
    def method4(self):
        print("Class D executed")

d=D()
d.method1()
d.method2()
d.method3()
d.method4()'''

#317 Write a python program to implement polymorphism.
'''class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()'''

#318 Write a python program to implement method overloading.
'''class Test:
    def add(self, a, b, c ):
        return a + b + c

t = Test()
print(t.add(2, 3,5))       
print(t.add(2, 3, 4))'''

# 319 Write a python program to implement method overriding.
'''class Employee:
    def salary(self):
        print("Basic salary")

class Manager(Employee):
    def salary(self):
        print("Salary with bonus")

class Intern(Employee):
    def salary(self):
        print("Stipend")

e = Employee()
m = Manager()
i = Intern()

e.salary()
m.salary()
i.salary()'''

#320 Write a python progrma to implement operator overriding.
'''class Employee:
    def __init__(self,id):
        
        self.id=id
    def __eq__(self, other):
        return self.id==other.id
e1=Employee(101)
e2=Employee(101)
print(e1==e2)'''


#321 Write a python program to implement Encapsulation.
'''class Demo:
    def setAge(self,age):
        self.__age=age
    def getAge(self):
        return self.__age


d=Demo()
age=int(input("enter the age:"))
d.setAge(age)
print(d.getAge())'''

#322 Write a python program to implement abstraction.
'''from abc import *

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Area of circle")

class Rectangle(Shape):
    def area(self):
        print("Area of rectangle")

c = Circle()
r = Rectangle()

c.area()
r.area()'''

#323 Write a python program to implement constructor in class.

'''class Demo:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("Name="'{}'.format(self.name))
        print("Age="'{}'.format(self.age))
d=Demo("Harsh",21)
d.show()'''

# 324 Write a python program to implement destructor in class.
'''class Test:
    def __init__(self):
        print("Constructor is being created....")

    def __del__(self):
        print("Deconstructor is being executed")
t=Test()
del t'''

#325 Write a python program to implement class variables and instance variables.
'''class Employee:
    company = "TCS"   

    def __init__(self, eid, ename, salary):
        self.eid = eid          
        self.ename = ename      
        self.salary = salary    

e1 = Employee(101, "Harsh", 60000)
e2 = Employee(102, "Aman", 50000)


print(e1.eid, e1.ename, e1.salary)
print(e2.eid, e2.ename, e2.salary)

# class variable
print(e1.company)
print(e2.company)'''

#326 Write a python program to implement static method.
'''class Test:
    @staticmethod
    def add(a,b):
        print(a+b)
t=Test()
Test.add(34,45)'''

#327 Write a python program to implement class  method.
'''class Employee:
    company="Google"
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
    
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company

e1 = Employee(101,"Harsh", 60000)
e2 = Employee(102,"Aman", 50000)

print("Before:", e1.company, e2.company)

Employee.change_company("Meta")

print("After:", e1.company, e2.company)'''

#328 Write a python program to implement abstract base class.
'''from abc import *
class College(ABC):
    @abstractmethod
    def marks(self):
        pass
class Student(College):
    def marks(self):
        print("Marks of student is being evaluating...")
s=Student()
s.marks()'''


#329 Write a python program to implement interface using abstract  class.
'''from abc import *
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with key")

    def stop(self):
        print("Car stops with brake")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick")

    def stop(self):
        print("Bike stops with brake")


c = Car()
b = Bike()

c.start()
c.stop()

b.start()
b.stop()'''

#330 Write a python program to implement multiple constructors using @classmethod.
'''class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    @classmethod
    def from_name(cls, name):
        return cls(name, 0)

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


# normal constructor
a1 = BankAccount("Harsh", 5000)

# alternative constructor
a2 = BankAccount.from_name("Aman")

a1.display()
a2.display()'''


