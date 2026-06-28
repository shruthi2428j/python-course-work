'''
#for N
n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j == 0 or j == n - 1 or i == j:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
#for O
n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (i == 0 and j > 0 and j < n - 1) or (i == n - 1 and j > 0 and j < n - 1) or (j == 0 and i > 0 and i < n - 1) or (j == n - 1 and i > 0 and i < n - 1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
for P
n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j == 0 or (i == 0 and j < n - 1) or (i == m and j < n - 1) or (j == n - 1 and i > 0 and i < m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
for Q
n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (i == 0 and j > 0 and j < n - 1) or (i == n - 2 and j > 0 and j < n - 1) or (j == 0 and i > 0 and i < n - 2) or (j == n - 1 and i > 0 and i < n - 2) or (i == j and i >= m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
for R
n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if j == 0 or (i == 0 and j < n - 1) or (i == m and j < n - 1) or (j == n - 1 and i > 0 and i < m) or (i - j == m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
for S
n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if (i == 0) or (i == m) or (i == n-1) or (j == 0 and i < m) or (j == n-1 and i > m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
for T
n = int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
for U
n = int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
for V
n = int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if (j==0 and i<=m) or (j==n-1 and i<=m) or (i-j==m and i>=m) or (i+j==n+m-1 and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
for W
n = int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or(i==j and j>=m) or (i+j==n-1 and j<=m) or ( i==m and j<=m)or (j==m and i==m) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
for Y
n = int(input("Enter the size:"))
m=n//2
for i in range(n):
    for j in range(n):
        if (i==j and j<=m) or (i+j==n-1 and j>=m) or (j==m and i>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
for Z
n = int(input("Enter the size: "))
m=n//2
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or i + j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
'''
for X
n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
