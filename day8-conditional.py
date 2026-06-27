Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=set()
s
set()
s={1,2,3,4,6}
s
{1, 2, 3, 4, 6}
s.add(8)
s
{1, 2, 3, 4, 6, 8}
s.add(1)
s
{1, 2, 3, 4, 6, 8}
girls={'shruthi','kavya','anuhya','veena','pravalika'}
girls
{'veena', 'pravalika', 'shruthi', 'anuhya', 'kavya'}
boys={'sairam','madhav','bharath','ravi','vamshi'}
toppers={'madhav','sairam','adarsh'}
girls|boys
{'bharath', 'vamshi', 'shruthi', 'ravi', 'madhav', 'veena', 'sairam', 'pravalika', 'anuhya', 'kavya'}
girls&boys
set()
toppers&boys
{'sairam', 'madhav'}
boys-toppers
{'ravi', 'bharath', 'vamshi'}
boys^toppers
{'bharath', 'vamshi', 'ravi', 'adarsh'}
#^removes common words and give remaining words in set
#^removes common words and give remaining words in set
{madhav}>=boys
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    {madhav}>=boys
NameError: name 'madhav' is not defined
>>> {'madhav'}>=boys
False
>>> {'sairam'}>=boys
False
>>> {'bharathi'}>=boys
False
>>> {'sairam','madhav','bharath','ravi','vamshi'}>=boys
True
>>> girls.isdisjoint(boys)
True
>>> boys.isdisjoint(toppers)
False
>>> False
False
>>> boys.pop()
'bharath'
>>> boys
{'vamshi', 'sairam', 'ravi', 'madhav'}
>>> boys.pop()
'vamshi'
>>> boys.remove('sairam')
>>> boys
{'ravi', 'madhav'}
>>> boys.discard('ravi')
>>> boys
{'madhav'}
>>> sorted(girls)
['anuhya', 'kavya', 'pravalika', 'shruthi', 'veena']
>>> max(girls)
'veena'
>>> min(girls)
'anuhya'
>>> girls.copy()
{'veena', 'pravalika', 'shruthi', 'anuhya', 'kavya'}
>>> f=frozenset({1,2,3,3,4,5,5})
>>> f
frozenset({1, 2, 3, 4, 5})
>>> len(f)
5
>>> max(f)
5
>>> min(f)
1
>>> sum(f)
15
>>> 
