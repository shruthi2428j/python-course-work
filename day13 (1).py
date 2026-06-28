'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print('*',end=' ')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print(col%2 ,end=' ')
    print()
'''
'''
0's = 00 02 04 11 13 20
       0  2  4  2  4  2 same like this take 1's also
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print((row + col )%2 ,end=' ')
    print()
'''
'''
logic - 00 01 02 03 10 11 12 20 21 30 - 0's  , 1's = 04  13  14  22  23  24 31 32 33 34                                                   4   4   5   4   5   6  4  5  6  7
0   1  2  3  1  2  3  2  3  3
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n):
        print(int(row+col>n-1),end=' ')
    print()
'''
'''
n = int(input("Enter the size: "))
c=1
for row in range(n):
    for col in range(n):
        print(str(c).zfill(2),end=' ')
        c+=1
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(row+1):
        print('*',end=' ')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(n-i):
        print('*',end=' ')
    print()
'''
'''
c=65
n = int(input("Enter the size: "))
for row in range(n):
    for col in range(row+1):
        print(chr(c),end=' ')
        c+=1
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for sp in range(row):
        print(' ',end=' ')
    for col in range(n-row):
        print('*' ,end=' ')
    print()
'''
'''
n = int(input("Enter the size: "))
for row in range(n):
    for sp in range(n-row-1):
        print(' ',end=' ')
    for col in range(row+1):
        print('*',end=' ')
    print()
'''
n = int(input("Enter the size: "))
m = n//2
for row in range(n):
    if i<=m:
        for col in range(row+1):
             print('*',end=' ')
    else:
        for col in range(n-row):
            print('*',end=' ')
    print()
