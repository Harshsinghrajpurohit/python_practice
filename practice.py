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