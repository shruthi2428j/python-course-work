'''
while condition:
    print()
    update()

i = 1
while i<=10:
    print(i)
    i += 1

i = 30
while i <=50:
    print(i)
    i += 2

i=6
while i<100:
    print(i)
    i += 6

i=10
while i>=1:
    print(i)
    i-=1

i =29
while i>=1:
    print(i)
    i-=2
s='python'
i=0
while i <len(s):
    print(i,s[i])
    i += 1
    
s=[1,2,3,45,788,908]
i=0
while i <len(s):
    print(i,s[i])

s=(1,2,3,45,788,908)
i=0
while i <len(s):
    print(i,s[i])
    i += 1

i = 1
while i<=10:
    if i==5:
        break
    print(i)
    i += 1

    
i = 0
while i<=10:
    i += 1
    if i==5:
        continue
    print(i)


#pass is used to define empty block of code
i=0
while i<=10:
    pass


x=10
y=10
z=None
assert x!= None and y!= None and z!=None, "You need to update the xyz values"
print(name,phone,age)


api = ''
assert api != '',


#bill generation
l=[]
while True:
    product = input("Enter the product:   ")
    price = int(input("Enter the price:  "))
    quantity = float(input("Enter the quantity:  "))
    l.append([product,price,quantity])
    status = input('[D]one or [N]ext: ').upper()
    if status == 'D':
       bill =0
       for i in l:
            print(f'{i[0]} : {i[1]} * {i[2]} = {i[1] * i[2]}')
            bill += i[1]*i[2]
       print(f"Total Bill: ${bill}")
       print("Thanks for shopping!!!")
       break


#guess the number
number = 5
while True:
    n = int(input("Guess the number:"))
    if number == n:
        print("Your guess is correct!!!")
        break
    else:
        print("Incorrect, Try Again")

'''


l=[9,0,0,6,0,5,0,2,45,87,12,4,90,23,0,0,0,0,0,0,3,5]
while 0 in l:
    l.remove(0)
print(l)
    
