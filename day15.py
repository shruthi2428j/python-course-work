'''def iseven(num):
    
    if num%2==0:
        return "even numbers"
    else:
        return "odd numbers"
print(iseven(14))
print(iseven(13))
print(iseven(5))'''
'''def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return "not prime"
        
        else:
            return "prime"
for i in range(2,100):
    print(isprime(i))'''
'''def isprime(n):
    for num in range(2,n+1):
        for i in range(2,num):
         if num%i==0:
            break
        else:
            print(num,end=" ") 
isprime(32)'''
'''def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"factorial of {n}:{fact}")
factorial(5)
factorial(10)'''
'''def display(name,email):
    print('name:',name)
    print('email:',email)
display('shruthi','shruthi23i@gmai.com')
display('veena234@gmail.com',"venna")'''
def display(name,email=''):
    print('name:',name)
    print('email:',email)
display("siri")
display('shruthi','shruthi23i@gmai.com')
display('veena234@gmail.com',"venna")
    
