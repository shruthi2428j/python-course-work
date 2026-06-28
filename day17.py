'''def sumofn(n):
    if n==0:
        return 0
    return n+sumofn(n-1)
n=int(input("enter the n:"))
print(sumofn(n))'''
'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input("enter the n:"))
print(fact(n))'''
'''def sumofdigits(n):
    if n==0:
        return 0
    return n%10+sumofdigits(n//10)
n=int(input("enter the n:"))
print(sumofdigits(n))'''
'''def isprime(n):
    if n==0:
        return 0
    return ((n**0.5)+1)
n=int(input("enter n value:"))
print(isprime(n))'''

'''def power(base,pow):
    if pow==0:
        return 1
    return base*power(base,pow-1)
print(power(2,5))
print(power(3,4))'''
'''def display(s,ind):
     if len(s)+1==ind:
         return
     print(s[:ind])
     display(s,ind+1)
display("python programming",1)'''
'''def display(s,ind,wid):
    if ind==len(s)-wid+1:
        return
    print(s[ind:ind+wid])
    display(s,ind+1,wid)
display("python programming",0,15)'''
'''l=[1,2,3,4,5]
res=[]
for i in l:
    res.append(i*i)

res2=[i*i for i in l]
print(res,res2)'''

'''s='python programming'
res =[i for i in s if i in 'aeiouAEIOU']
print(res)'''
'''s=[1,2,3,4,5]
res=[i if i%2==0 else 0 for i in s]
print(res)'''
'''res=[j for i in range(5) for j in range(1,4)]
print(res)'''
'''res=[[j for j in range(1,5)] for i in range(4)]
print(res)'''
res={i:i**2 for i in range(1,11)}
print(res)


        
     














    
