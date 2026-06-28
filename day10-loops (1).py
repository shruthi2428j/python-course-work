'''
for var in seq:
    stmsts
seq: str,list,tuple,set,dict,range()
'''
'''
s = 'python programming'
for ch in s:
    print(ch)
'''

'''
products = ['laptop', 'mouse' , 'keyboard','charger']
for product in products:
    print(product)
'''

'''
names = ('veena','shruthi','pravalika','kavya')
for name in names:
    print(name)
'''

'''
s ={'python','c','mysql','c++','java'}
for i in s:
    print(i)
'''
'''
d = {'pen':10, 'book':50 , 'bag':2000,'pencil':5}
for i in d:
    print(i)
'''
'''
#syntax for range
range(start,stop+1,step) = (0,n,1)
'''

'''
for i in range(20,51):
    print(i)
'''

'''
for i in range(2,41,2):
    print(i)
'''

'''
for i in range (1,40,2):
    print(i)
'''
'''
for i in range(10,0,-1):
    print(i)
'''

'''
for i in range(19,0,-2):
    print(i)
'''
'''
for i in range(5,101,5):
    print(i)
'''
'''
s = 'python programming'
for ind in range(len(s)):
    print(ind,s[ind])
'''
'''
products = ['laptop', 'mouse' , 'keyboard','charger']
for i in range(len(products)):
    print(i,products[i])
'''
'''
s = 'python programming'
for i in enumerate(s):
    print(i[0],i[1])
'''
'''
products = {'laptop', 'mouse' , 'keyboard','charger'}
for i in enumerate(products):
    print(i[0],i[1])
'''
'''
d = {'pen':10,'book':50,'bag':2000 ,'pencil':5}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])
'''
'''
for i in range(20):
    if i==15:
        break
    print(i)
'''
'''
for i in range(10):
    if i==5:
        break
    print(i)
'''
'''
for i in range(20):
    if i==15:
        continue
    print(i)
'''
'''
for i in range(1,11):
    pass
'''
'''
#for with else, both else and break are inversely proportional
when there is break inside else will not execute.
'''



pin=1234
for i in range(5):
    epin = int(input("Enter the pin:  "))
    if pin == epin:
        print("Unlock the phone")
        break
    else:
        print("Incorrect pin, try again")
else:
    print("Try again after 60 seconds")



