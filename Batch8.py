                                                                 #Pattern Programming
#1 Write a python program to create a Right-Angled Triangle Pattern.
'''n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()'''

#2 Write a python program to create a Inverted Triangle pattern.
'''n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(n-i+1):
        print('*',end='')
    print()'''

#3 Write a  python program to create a Number Triangle pattern.
'''n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()'''

#4 Write a python program to create a Square Pattern pattern.

'''n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end='')
    print()'''

#5 Write a python program to create a Pyramid Pattern pattern.
'''n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(' ',end='')
    for j in range(2*i-1):
        print('*',end='')
    print()'''

#6 Write a python program to create a Diamond Pattern pattern.
'''for i in range(1,5):
    for k in range(5-i+1):
        print(' ',end='')
    for j in range(2*i-1):
        print('*',end='')
    print()

for i in range(1,6):
    for k in range(i):
        print(' ',end='')
    for j in range(2*(5-i)+1):
        print('*',end='')
    print()'''

#7  Write a python program to create a Hollow Square pattern.
'''n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
       
   for j in range(1,n+1):
        if i==1 or i==5 or j==1 or j==5:
             print('*',end='')
        else:
            print(' ',end='')
   print()'''

#8  Write a python program to create a Zigzag / Number Pyramid.
'''n=int(input("Enter the number of rows:"))
count=1
for i in range(1,n+1):
    for j in range(1,i+1):

       print(count,end='')
       count=count+1
    print()'''

#9 Write a python program to create a Inverted Right-Angled Triangle.
'''for i in range(1,5):
    for j in range(1,i+1):
        print('*',end='')
    print()

for i in range(1,6):
    for j in range(5-i+1):
        print('*',end='')
    print()'''

#10 Write a python program to create a parallelogram.

'''n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for k in range(1,i+1):
        print(' ',end='')
    for j in range(1,n+1):
        print('*',end='')
    print()'''

#11 Write a python program to create a inverse parallelogram.
'''n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(' ',end='')
    for j in range(1,n+1):
        print('*',end='')
    print()'''