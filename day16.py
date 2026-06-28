'''def display():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("inner function",n)
    inner()
    print("outsider function:",n)
display()'''
'''def display():
    course="java"
    print("strating:",course)
    def change():
        nonlocal course
        course="python"
        print("updated:",course)
    change()
    print("final course:",course)
display()'''
'''s="python"
print(len(s))
len=10#here len is built-in function we cant take as variable
print(len)'''
'''s="python"
len=10
print(len)'''
#pass by value and pass by reference
'''int,float,complex,str,tuple,bool=pass by values displays different outputs inside and outside functions
list,set,dict=pass by reference they display same output for in and outside function'''
'''def update(n):
    n=True
    print("inside:",n)
n=False
update(n)
print("outside",n)'''
'''def update(s):
    s=s.upper()
    print("inside:",s)
s="python"
update(s)
print("outside:",s)'''
'''def update(n):
    n.append(10)
    print("inside:",n)
n=[12,23,45]
update(n)
print("outside",n)'''
'''def update(n):
    n.add(10)
    print("inside:",n)
n={12,23,45}
update(n)
print("outside",n)
print(type(n))'''
#recursion
'''def display(num):
    if num>10:
        return
    print(num)
    display(num+1)
display(1)'''
'''def display(num):
    if num>10:
        return
    display(num+1)
    print(num)
display(1)'''
def display(s,ind):
    if ind==len(s):
     return
    display(s,ind+1)
    print(s[ind],end="")
display("enter the string:")



        
        

