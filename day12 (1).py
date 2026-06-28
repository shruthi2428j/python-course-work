'''
prices = list(map(int,input("Enter the prices: ").split()))
bill = 0
for i in prices:
    bill+=i
print("Bill",bill)
'''
'''
pwd = input("Enter the string:")
uc=lc=dc=sc=0
for i in pwd:
    if i.isalpha():
        if i.isupper():
             uc+=1
        else:
            lc+=1
    elif i.isdigit():
            dc+=1
    else:
            sc+=1
print("Uppercase:",uc)
print("lowercase:",lc)
print("Digits:",dc)
print("Special Characters:",sc)
'''
'''
movies = input("Enter the movies:").split()
for i in range(len(movies)):
    print(i+1,'.',movies[i])
'''
'''
records = eval(input())
print("Highest Salary:", max(records.values()))
print("Lowest Salary:", min(records.values()))
print("Average Salary:", sum(records.values())/len(records))
'''
'''
scores = list(map(int, input("Entet the scores: ")))
tr=bd=db=0
for i in scores:
    if i ==4 or i==6:
        bd+=1
    elif i==0:
        bd+=1
    tr+=i
print("Total Runs:",tr)
print("Boundaries:",bd)
print("Dot Balls:",db)
'''
'''
emails = input("Enter the email:").split()
for i in emails:
    print(i.split('@')[1])
'''
'''
attempts=0
pin=1234
while attempts<3:
    epin = int(input("Enter the pin: "))
    if epin == pin:
        print("Access Granted")
        break
    attempts+=1
else:
    print("Card Blocked")
'''
'''
c=0
while True:
    items = input("Enter the item or exit: ")
    if items == "exit":
        print("Total no of items:",c)
        break
    c+=1
'''
'''
at = 3
correct = 'python'
while at > 0:
    ans = input("Enter the answer: ")
    if ans == correct:
        print("You Win")
        print("Lives Remaining:",at)
        break
    at-=1
else:
    print("Game Over\nLives Remaining: 0")
'''
'''
s = 'looping statements'
i = 0
j = len(s) - 1
while i <= j:
        print(s[i] + s[j])
        i += 1
        j -= 1
'''

amount = int(input("Enter the amount: "))
notes = [2000,500,100,50,10]
for i in notes:
    req = amount//i
    amount = amount%i
    print(req,i )
    if req!=0:
        print(req,i)
        
