'''
wish=lamda name: f'welcome to the course,{name}'
print(wish('shruthi'))
print(wish('sarayu'))'''

'''greater=lambda a,b:a if a>b else b
print(greater(10,3))
print(greater(1,34))
print(greater(2,6))'''
'''avg=lambda a,b,c:(a+b+c)/3
print(avg(10,20,30))
print(avg(20,30,40))'''
'''gst=lambda p: p+p*0.18
print(gst(1000))
print(gst(2000))
print(gst(4000))'''
'''from functools import reduce
l=(1,2,3,4,5)
res1=list(map(lambda i:i+10,l))
print(res1)'''
'''s=[12,23,45,56,67,78]
res2=list(filter(lambda i:i%3==0,s))
print(res2)'''
'''from functools import reduce
k=[12,34,56,78]
res3=reduce(lambda sum,i:sum+i,k)
print(res3)'''

'''l={'laptop':50000,'phone':100000,'charger':1000,'mouse':800}
res1=dict(map(lambda i:(i[0],i[1]+i[1]*0.18),l.items()))
print(res1)
'''
'''l={'laptop':0,'phone':10,'charger':2,'mouse':0}
res1=list(filter(lambda i:l[i]!=0,l))
print(res1)'''
'''def reels():
    l=['1..50','51..100','101..200','201..300']
    for i in range(len(l)):
       yield l[i]
r = reels()
print(next(r))
print(next(r))
print(next(r))'''
'''def reels():
    l=['1..50','51..100','101..200','201..300']
    for i in range(len(l)):
       yield l[i]
r = reels()

while True:
    try:
        print(next(r))
    except StopIteration:
        break'''
'''def factors(n):
    return [i for i in range(1,n+1) if n%i==0]
def generators(res):
    for i in res:
        yield i
res=factors(30)
f=generators(res)
for i in range(len(res)):
    print(next(f))'''
'''def fib(n):
    if n==1:
        return [0]
    elif n==2:
        return[0,1]
    elif n>2:
        res=[0,1]
        a,b=0,1
        for i in range(n-2):
            c=a+b
            res.append(c)
            a,b=b,c
        return res
def generators(res):
    for i in res:
        yield i
res=fib(13)
f=generators(res)
for i in range(len(res)):
    print(next(f))'''
#using generators
'''def primenumber(num):
    res=[]
    for n in range(2,num+1):
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            res.append(n)
    return res
def generators(res):
    for i in res:
        yield i
res=primenumber(10)
gen=generators(res)
for i in range(len(res)):
    print(next(gen))'''
#without generators
def primenumber(num):
    res=[]
    for n in range(2,num+1):
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            res.append(n)
    return res
res=primenumber(10)
print(res)
    
         

