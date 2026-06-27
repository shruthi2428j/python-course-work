Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s="python programming"
s.startswith('py')
True
s.startswith('java')
False
s.endswith('ed')
False
'abc'.isalpha()
True
'abc1'.isalpha()
False
'abc def'.isalpha()
False
'abc@'.isalpha()
False
'1abc'.isalpha()
False
'abcsd'.isalnum()
True
'12abc'.isalnum()
True
'$%@'.isalnum()
False
'abc'.islower()
True
'Abc'.isupper()
False
'ABC'.isupper()
True
'shruthi  kummari'.isspace()
False
'shruthikummari'.isspace()
False
'    '.isspace()
True
'Abc Bced Cde'.istitle()
True
'my_var.isidentifier()
SyntaxError: unterminated string literal (detected at line 1)
'my_var'.isidentifier()
True
'234.isdecimal()
SyntaxError: unterminated string literal (detected at line 1)
'234'.isdecimal()
True
'abc'.isdecimal()
False
'12.3'.isdigit()
False
"shruti".isstr()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    "shruti".isstr()
AttributeError: 'str' object has no attribute 'isstr'
l=[]
l=list()
l=[1,2,3,4,5,5]
type(l)
<class 'list'>
id(l)
1797877506304
l.append(12)
l
[1, 2, 3, 4, 5, 5, 12]
l.remove(2)
l
[1, 3, 4, 5, 5, 12]
l=s="python programming"
s.startswith('py')
True
s.startswith('java')
False
s.endswith('ed')
False
'abc'.isalpha()
True
'abc1'.isalpha()
False
'abc def'.isalpha()
False
'abc@'.isalpha()
False
'1abc'.isalpha()
False
'abcsd'.isalnum()
True
'12abc'.isalnum()
True
'$%@'.isalnum()
False
'abc'.islower()
True
'Abc'.isupper()
False
'ABC'.isupper()
True
'shruthi  kummari'.isspace()
False
'shruthikummari'.isspace()
False
'    '.isspace()
True
'Abc Bced Cde'.istitle()
True
'my_var.isidentifier()
SyntaxError: unterminated string literal (detected at line 1)
'my_var'.isidentifier()
True
'234.isdecimal()
SyntaxError: unterminated string literal (detected at line 1)
'234'.isdecimal()
True
'abc'.isdecimal()
False
'12.3'.isdigit()
False
"shruti".isstr()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    "shruti".isstr()
AttributeError: 'str' object has no attribute 'isstr'
l=[1,2,3,4,[1,2,3],3+7j,(1,2,3),{1,2,3},{1:1,2:2}]
SyntaxError: multiple statements found while compiling a single statement
l=[1,2.3,4,[1,2,3],3+7j,(1,2,3),{1,2,3},{1:1,2:2},False]
l
[1, 2.3, 4, [1, 2, 3], (3+7j), (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, False]
names=['sharath','shashi','sai,'shruthi','siri']
       
SyntaxError: unterminated string literal (detected at line 1)
names=['sharath','shashi','sai','shruthi','siri']
       
names
       
['sharath', 'shashi', 'sai', 'shruthi', 'siri']
girls=['shru','siri','kavya','greesh']
       
names+girls
       
['sharath', 'shashi', 'sai', 'shruthi', 'siri', 'shru', 'siri', 'kavya', 'greesh']
names[0]
       
'sharath'
names[-1]
       
'siri'
girls[0]
       
'shru'
names[:4:]
       
['sharath', 'shashi', 'sai', 'shruthi']
names[0:4:]
       
['sharath', 'shashi', 'sai', 'shruthi']
names[1:3:]
       
['shashi', 'sai']
l[1:3:]
       
[2.3, 4]
sorted(names)
       
['sai', 'sharath', 'shashi', 'shruthi', 'siri']
min(names)
       
'sai'
max(names)
       
'siri'
len(names)
       
5
5
       
5
names.insert(1,'shruu')
       
names
       
['sharath', 'shruu', 'shashi', 'sai', 'shruthi', 'siri']
names.extend(['anu','soumya])
              
SyntaxError: unterminated string literal (detected at line 1)
names.extend(['anu','soumya'])
              
names
              
['sharath', 'shruu', 'shashi', 'sai', 'shruthi', 'siri', 'anu', 'soumya']
names.pop(0)
              
'sharath'
names
              
['shruu', 'shashi', 'sai', 'shruthi', 'siri', 'anu', 'soumya']
names.clear()
              
names.delete('sai')
              
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    names.delete('sai')
AttributeError: 'list' object has no attribute 'delete'
names.del('sai')
              
SyntaxError: invalid syntax
del names[1]
              
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    del names[1]
IndexError: list assignment index out of range
del names[l]
              
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    del names[l]
TypeError: list indices must be integers or slices, not list
>>> del names[2]
...               
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    del names[2]
IndexError: list assignment index out of range
>>> del names[0]
...               
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    del names[0]
IndexError: list assignment index out of range
>>> del l[1]
...               
>>> l
...               
[1, 4, [1, 2, 3], (3+7j), (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, False]
>>> del l[0]
...               
>>> l
...               
[4, [1, 2, 3], (3+7j), (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, False]
>>> l.index(2)
...               
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    l.index(2)
ValueError: 2 is not in list
>>> l.index(1)
...               
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    l.index(1)
ValueError: 1 is not in list
>>> l.index(0)
...               
6
>>> l.count(1)
...               
0
>>> l=[2,3,4]
...               
>>> m=1
              
m=l
              
m
              
[2, 3, 4]
m.append(2)
              
m
              
[2, 3, 4, 2]
l
              
[2, 3, 4, 2]
sum(l)
              
11
any([1,23,0])
              
True
any([00,0,(),{},[],' ')]
              
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
any([00,0,(),{},[],' '])
              
True
any([0,0,(),{},[],' '])
              
True
