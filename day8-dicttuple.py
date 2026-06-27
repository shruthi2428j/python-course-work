Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=()
t=tuple()
type(t)
<class 'tuple'>
t=(1,2,3,4)
(1,2,3,4)+(3,2,1,6)
(1, 2, 3, 4, 3, 2, 1, 6)
t=(1)
t
1
t=(0)
t=(1,)
t
(1,)
t=(1,2,3,4,5)
t(:4:1)
SyntaxError: invalid syntax
t[:3:]
(1, 2, 3)
t[::-1]
(5, 4, 3, 2, 1)
t[-1:-4:-1]
(5, 4, 3)
t[:-5:]
()
t[1:3:]
(2, 3)
6 in t
False
6 not in t
True
t
(1, 2, 3, 4, 5)
t*3
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
t+t
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
t[1]
2
sorted.t
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    sorted.t
AttributeError: 'builtin_function_or_method' object has no attribute 't'
sorted.(t)
SyntaxError: invalid syntax
t.count(2)
1
sorted(t)
[1, 2, 3, 4, 5]
max(t)
5
min(t)
1
any(1,2)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    any(1,2)
TypeError: any() takes exactly one argument (2 given)
any((1,2))
True
all((0,0))
False
all((1,0))
False
all(())
True
any(())
False
a,b,c=(1,2,3)
a
1
b
2
>>> c
3
>>> t=(1,2,3,[1,2,3],(1,2,3),"shruthi",False,True,(),[],None)
>>> t
(1, 2, 3, [1, 2, 3], (1, 2, 3), 'shruthi', False, True, (), [], None)
>>> t[0]
1
>>> t[2]
3
>>> t[4]
(1, 2, 3)
>>> t[5]
'shruthi'
>>> d={1:2,2:4,3:9,"name":"shruthi"}
>>> d
{1: 2, 2: 4, 3: 9, 'name': 'shruthi'}
>>> d.get(1)
2
>>> d.get(4)
>>> d
{1: 2, 2: 4, 3: 9, 'name': 'shruthi'}
>>> d.(1)
SyntaxError: invalid syntax
>>> d.1
SyntaxError: invalid syntax
>>> d.[1]
SyntaxError: invalid syntax
>>> d[1]
2
>>> d[1]=int'
SyntaxError: unterminated string literal (detected at line 1)
>>> d[1]='int'
>>> d
{1: 'int', 2: 4, 3: 9, 'name': 'shruthi'}
>>> d={}
>>> d
{}
>>> d=dict{}
SyntaxError: invalid syntax
>>> d=dict[]
SyntaxError: invalid syntax
>>> d = dict[]
SyntaxError: invalid syntax
>>> d.get(30,'key is not present')
'key is not present'
>>> 
