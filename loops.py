# for loop
# eg :-  for(variable) in range(1,6):
from email.contentmanager import raw_data_manager

for i in range (1,6,2):
    print(i)

n=7
for i in range (1,11):
    print(n,'x',i,'=',n*i)


#while loop
#while condition:
#    body of while
#      increment
n=0
while n<=5:
    print(n)
    n=n+1

n=1
a=7
while n<=10:
    print(n*a)
    n+=1

while True:
    print("hello")
    break


for i in range(1,4):
    for j in range(1,11):
        print(j,end="")
    print()

for i in range (1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()


for i in range (1,101):
    if i%8==0 and i%12==0:
     print(i)
n=1
while n<=10:
    if n==3:
        print("fav no.")
    else:
        print(n)
    n+=1


# break and continue
for i in range (1,11):
    if i==5:
        continue
    else:
        print(i)


for i in range(1,11):
    if i==7:
        break
    else:
        print(i)
print("\n")


# Problem Solving
sum=0
for i in range (0,51):
    if i%2==0:
        sum=sum+i
print(sum)


for i in range(1,21):
    print(i,i**2)


while True:
    name=input("customer name:")
    total=0

    while True:
        amount=float(input("enter amount:"))
        quantity=float(input("enter quantity:"))
        total+=amount*quantity
        repeat=input('do you want to add more items? (yes/no):')
        if repeat=='no' or repeat=='No':
            break
    print("-"*40)
    print("name:",name)
    print("amount to be paid:",total)
    print("thank you")
    print("-"*40)

    repeat1 = input('do you want to move to next customer? (yes/no):')
    if repeat1 == 'no' or repeat == 'No':
        break


a="Why fit in, When you are Born to Stand Out!"
len(a)


for i in range(1,6):
    for j in range(1,6):
        print(j,end="")
    print()