Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l =[]
l=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]
id(l)
2463376258880
l = [1,12.3 , 'str' , [1,2,3] , 3+7j , (1,2,3),{1:1, 2:2},False]
l
[1, 12.3, 'str', [1, 2, 3], (3+7j), (1, 2, 3), {1: 1, 2: 2}, False]
l=list()
l
[]
names= ['bharath' , 'sairam' , 'dheeraj' , 'madhav' , 'chaithanya']
names
['bharath', 'sairam', 'dheeraj', 'madhav', 'chaithanya']
girls = ['kavya','kavitha','anuhya','sarayu']
girls
['kavya', 'kavitha', 'anuhya', 'sarayu']
names + girls
['bharath', 'sairam', 'dheeraj', 'madhav', 'chaithanya', 'kavya', 'kavitha', 'anuhya', 'sarayu']
girls * 4
['kavya', 'kavitha', 'anuhya', 'sarayu', 'kavya', 'kavitha', 'anuhya', 'sarayu', 'kavya', 'kavitha', 'anuhya', 'sarayu', 'kavya', 'kavitha', 'anuhya', 'sarayu']
names[0]
'bharath'
names[2]
'dheeraj'
names[5]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    names[5]
IndexError: list index out of range
names[-1]
'chaithanya'
names[-2]
'madhav'
names[-3]
'dheeraj'
names[1:4]
['sairam', 'dheeraj', 'madhav']
names[-1::4]
['chaithanya']
names[-2:-5:-1]
['madhav', 'dheeraj', 'sairam']
'madhav'in names
True
'chaithanya' not in names
False
sorted(names)
['bharath', 'chaithanya', 'dheeraj', 'madhav', 'sairam']
sorted(names , reverse=True)
['sairam', 'madhav', 'dheeraj', 'chaithanya', 'bharath']
names
['bharath', 'sairam', 'dheeraj', 'madhav', 'chaithanya']
max(names)
'sairam'
len(names)
5
min(names)
'bharath'
names.append()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    names.append()
TypeError: list.append() takes exactly one argument (0 given)
names.append(sairam)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    names.append(sairam)
NameError: name 'sairam' is not defined
names
['bharath', 'sairam', 'dheeraj', 'madhav', 'chaithanya']
names.append('sairam')
names
['bharath', 'sairam', 'dheeraj', 'madhav', 'chaithanya', 'sairam']
names.insert(1,'madhav')
names
['bharath', 'madhav', 'sairam', 'dheeraj', 'madhav', 'chaithanya', 'sairam']
names.pop('bharath')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    names.pop('bharath')
TypeError: 'str' object cannot be interpreted as an integer
names.exiend(['sarayu','anuhya','kavya','sowmya'])
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    names.exiend(['sarayu','anuhya','kavya','sowmya'])
AttributeError: 'list' object has no attribute 'exiend'. Did you mean: 'extend'?
names.extend(['sarayu','anuhya','kavya','sowmya'])
names
['bharath', 'madhav', 'sairam', 'dheeraj', 'madhav', 'chaithanya', 'sairam', 'sarayu', 'anuhya', 'kavya', 'sowmya']
names.pop()
'sowmya'
names.pop()
'kavya'
names.remove('chaithanya')
names
['bharath', 'madhav', 'sairam', 'dheeraj', 'madhav', 'sairam', 'sarayu', 'anuhya']
del names[1]
names
['bharath', 'sairam', 'dheeraj', 'madhav', 'sairam', 'sarayu', 'anuhya']
names.clear()
names
[]
l=[1,2,3,4,5,6,6,7,8,9]
l
[1, 2, 3, 4, 5, 6, 6, 7, 8, 9]
l.index(3)
2
l.count(1)
1
>>> l.index(10)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    l.index(10)
ValueError: 10 is not in list
>>> l.index(4)
3
>>> l=[1,2,3]
>>> m=1
>>> m
1
>>> m.append(4)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    m.append(4)
AttributeError: 'int' object has no attribute 'append'
>>> 
>>> m.append(3)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    m.append(3)
AttributeError: 'int' object has no attribute 'append'
>>> n =l.copy()
>>> n.append(10)
>>> n
[1, 2, 3, 10]
>>> n =[10,4,3,2,1]
>>> n
[10, 4, 3, 2, 1]
>>> sum(n)
20
>>> #0 0.0 '' [] () set() {} False
>>> any([1,2,3,0,0,0,0])
True
>>> any([1,0,0,0,])
True
>>> all([1,2,3])
True
>>> any(() , [],0,0,0,0,0})
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> any((),[],0,0,0,0,0)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    any((),[],0,0,0,0,0)
TypeError: any() takes exactly one argument (7 given)
