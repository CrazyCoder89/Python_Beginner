a="Why fit in, When you are Born to Stand Out!"
print(len(a))

print(a.count("o"))

print(a.lower())

print(a.upper())

print(a.title())

print(a.find("fit in"))



#loops

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print("")
print("\n")

for i in range(1,6):
    for j in range(6,i,-1):
        print(i,end="")
    print()

for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()


for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end="")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(5,0,-1):
    for j in range(0,i-1):
        print("*",end="")
    print()


for i in range(1,11):
    for j in range(1,i+1):
        print(i*j,end="")
    print()

#fibonacci
a=0
b=1
n=int(input("enter a no.:"))
if n==1:
    print(1)
else:
    print(a)
    print(b)
    for i in range (2,n):
        c=a+b
        a=b
        b=c
        print(c)


#prime
num=int(input("enter a number:"))
if num <=1:
    print("not a prime")
else:
    for i in range(2,num):
        if num%i == 0:
            print("it is not prime")
            break
        else:
            print("it is prime")
            break


#palindrome
num_1=int(input("enter a number:"))
temp=num_1
rev=0
while num_1>0:
    dig=num_1%10
    rev=rev*10+dig
    num_1=num_1//10
if rev==temp:
    print("it is palindrome")
else:
    print("it is not palindrome")


#area calculator
while True:
    print("""press 1 for area of square
    press 2 for area of rectangle
    press 3 for area of circle: """)
    choice=int(input("enter the 1-3:"))
    if choice==1:
        while True:
            side=float(input("enter the side length:"))
            square=side*side
            print("area of square is ",square)
            repeat=input("do you want to square again?")
            if repeat=='no':
                break
    elif choice==2:
        while True:
            length=float(input("enter the length:"))
            breadth=float(input("enter the breadth:"))
            rectangle=length*breadth
            print("area of rectangle is ",rectangle)
            repeat = input("do you want to square again?")
            if repeat == 'no':
                break
    elif choice==3:
        while True:
            pi=3.14
            radius=float(input("enter the radius:"))
            circle=pi*radius*radius
            print("area of rectangle is ",circle)
            repeat = input("do you want to square again?")
            if repeat == 'no':
                break
    else:
        print("invalid input")
    print("thank you \n")
    repeat = input("do you want to square again?")
    if repeat == 'no':
        break
