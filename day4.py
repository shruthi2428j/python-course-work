name=input()
shruthi
name
'shruthi'
name=input("enter your name:")``````````````````````````````````````````````
SyntaxError: invalid syntax
name=input("enter your name")
enter your name shruthi
name
' shruthi'
age=int(input("enter your age:"))
enter your age:22
age
22
gpa=float(input("enter your gpa"))
enter your gpa 8.9
'shruthi veena sai sharath'

names=input("enter the names").split()
enter the namesshruthi veena sai sharath
names
['shruthi', 'veena', 'sai', 'sharath']
names=input("enter the names").split(",")
enter the namesshruthi veena sai sharath
names
['shruthi veena sai sharath']
names=input("enter the names").split(',')
enter the namesshruthi veena sai sharath
names
['shruthi veena sai sharath']
marks=input("enter marks:").split()
enter marks:23 34 45 67
marks
['23', '34', '45', '67']
#map func is used to convert list of strings to ints
marks=list(map(int,input("enter marks:").split()))
enter marks:2 3 4 5 6
marks
[2, 3, 4, 5, 6]
#same for set and tuple
#same for set and tuple
gpa=tuple(map(float,input("enter gpa:").split()))
enter gpa:24 3 2 3 2
gpa
(24.0, 3.0, 2.0, 3.0, 2.0)
a=eval(input("enter the value:"))
enter the value:65432
a
65432
type(a)
<class 'int'>
  a=eval(input("enter the value:"))
a=eval(input("enter the value:"))
enter the value:34.56
a
34.56
a=eval(input("enter name"))
enter nameshruthi
a=eval(input("enter name"))
enter name "shruthi"
a
'shruthi'
type(a)
<class 'str'>
username,password=input("enter username & password:").split()
a=eval(input("enter name"))
enter name "shruthi"
a
'shruthi'
type(a)
<class 'str'>
<class 'str'>
SyntaxError: invalid syntax
username,password=input("enter username&password:").split()
enter username&password:abc ab@q2
username
'abc'
password
'ab@q2'
a,b,c=list(map(int,input().split())
2 3 4
a,b,c=list(map(int,input().split()))
           
2 3 4
a
           
2
b
           
3
c
           
4
a="python"
           
b=12
           
c=78.89
           
print(a,b,c)
           
python 12 78.89
print('a=','b=',b,'c=',c)
print('a=',a,'b=',b,'c=',c,sep='')
a=pythonb=12c=78.89
print('a=',a,'b=',b,'c=',c,end='@@@')
a= python b= 12 c= 78.89@@@
print('a=',a,'b=',b,'c=',c,end='\n')
a= python b= 12 c= 78.89
print(f'a={a} b={b} c={c} ')
           
a=python b=12 c=78.89 


