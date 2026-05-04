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



#12 
'''n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for outerk in range(1,n-i+1):
        print(' ',end='')
    if i==1:
        print(i)
    else:
        print(i,end='')
        for innerk in range(2*i-3):
            print(' ',end='')
        print(i)'''


'''n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for outerk in range(1,n-i+1):
        print(' ',end='')
    if i==1:
        print(chr(i+64))
    else:
        print(chr(i+64),end='')
        for innerk in range(2*i-3):
            print(' ',end='')
        print(chr(i+64))'''

'''n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for outerk in range(i-1):
        print(' ',end='')
    if i==n:
        print(chr(i+64))
    else:
        print(chr(i+64),end='')
        for innerk in range(2*(n-i)-1):
            print(' ',end='')
        print(chr(i+64))'''

'''for i in range(1,5):
    for outerk in range(1,5-i+1):
        print(' ',end='')
    if i==1:
        print(i)
    else:
        print(i,end='')
        for innerk in range(2*i-3):
            print(' ',end='')
        print(i)

for i in range(1,6):
    for outerk in range(i-1):
        print(' ',end='')
    if i==5:
        print(i)
    else:
        print(i,end='')
        for innerk in range(2*(5-i)-1):
            print(' ',end='')
        print(i)'''

'''for i in range(1,5):
    for outerk in range(1,5-i+1):
        print(' ',end='')
    if i==1:
        print(chr(i+64))
    else:
        print(chr(i+64),end='')
        for innerk in range(2*i-3):
            print(' ',end='')
        print(chr(i+64))

for i in range(1,6):
    for outerk in range(6-1):
        print(' ',end='')
    if i==5:
        print(chr(64+i),end='')
    else:
        print(chr(64+i),end='')
        for innerk in range(2*(5-i)-1):
            print(' ',end='')
        print(chr(64+i))'''

'''n=5
for i in range(1,n+1):
    for k in range(n-i+1):
        print(' ',end='')
    for j in range(1,i+1):
        print(i,end='')
    print()


for i in range(n-1,0,-1):
    for k in range(n-i):
        print(' ',end='')
    for j in range(i):
        print(i,end='')
    print()'''

'''n=5
for i in range(1,n+1):
    for k in range(n-i+1):
        print(' ',end='')
    for j in range(1,i+1):
        print(chr(i+64),end='')
    print()


for i in range(n-1,0,-1):
    for k in range(n-i):
        print(' ',end='')
    for j in range(i):
        print(chr(i+64),end='')
    print()'''

'''n = 5
for i in range(1, n + 1):
    for k in range(n - i):
        print('  ', end='')
    for j in range(2 * i - 1):
        print(j + 1, end=' ')
    print()'''


'''n = 5
for i in range(1, n + 1):
    for k in range(n - i):
        print('  ', end='')
    for j in range(2 * i - 1):
        print(chr(65 + j), end=' ')
    print()'''

'''n = 5
for i in range(1, n + 1):
    for k in range(n - i):
        print('  ', end='')
    for j in range(2 * i - 1):
        print(chr(64 + i), end=' ')
    print()'''
'''n = 5
for i in range(1, n + 1):
    for k in range(i - 1):
        print(' ', end='')
    for j in range(2 * (n - i) + 1):
        print(i, end=' ')
    print()'''

'''n = 5

# Upper half
for i in range(1, n + 1):
    for k in range(n - i):
        print('  ', end='')
    for j in range(2 * i - 1):
        print(j + 1, end=' ')
    print()

# Lower half
for i in range(n - 1, 0, -1):
    for k in range(n - i):
        print('  ', end='')
    for j in range(2 * i - 1):
        print(j + 1, end=' ')
    print()'''

'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or  j==0  or j==n-1 or i==n//2:
            print('*',end='')
        else:
            print(' ',end='') 
    print()'''
'''n = 5

for i in range(n):
    for j in range(n):
        if (
            i == 0 or i == n-1 or      # top & bottom row
            j == 0 or                 # left column
            j == n//2 or              # middle column
            j == n-1                  # right column
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''



'''n = 5

for i in range(n):
    for j in range(n):
        if (
            i == 0 or i == n-1 or        # top & bottom
            j == 0 or j == n-1 or        # left & right
            i == j              # anti-diagonal
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

'''n = 9

for i in range(n):
    for j in range(n):
        if (
            i == 0 or i == n-1 or      # top & bottom
            i == j or                  # main diagonal
            i + j == n - 1             # anti-diagonal
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()'''

'''n = 9

for i in range(n):
    for j in range(n):
        if i==0 or i==j or i+j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()'''

'''n = 5
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if i == 1 or j == i or j == 2 * n - i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()'''

n = int(input("Enter number of rows: "))

num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()