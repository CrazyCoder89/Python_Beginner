# 1 program to check if no. is positive
number=int(input("enter the value: "))
if number >= 0:
    print("it is positive")
else:
    print("it is negative")
print("thank you \n")


# 2 check wheather odd or even
number_1=int(input("enter the number: "))
if number_1%2==0:
    print("it is even")
else:
    print("it is odd")
print("thank you \n")


# 3 create area calculator
print("""press 1 for area of square
press 2 for area of rectangle
press 3 for area of circle: """)
choice=int(input("enter the 1-3:"))
if choice==1:
    side=float(input("enter the side length:"))
    square=side*side
    print("area of square is ",square)
elif choice==2:
    length=float(input("enter the length:"))
    breadth=float(input("enter the breadth:"))
    rectangle=length*breadth
    print("area of rectangle is ",rectangle)
elif choice==3:
    pi=3.14
    radius=float(input("enter the radius:"))
    circle=pi*radius*radius
    print("area of rectangle is ",circle)
else:
    print("invalid input")
print("thank you \n")


# 4 check weather it is vowel or not
#method1
alphabet=input("enter the alphabet: ")
vowels='a','e','i','o','u'
if alphabet==vowels:
    print("it is vowel")
else:
    print("it is consonant")

#method2
letter= input("enter a letter: ")
if (letter in 'aeiou') or (letter in 'AEIOU'):
    print("it is vowel")
else:
    print("it is not a vowel")
print("thank you \n")


# 5 to check wheather no. is single digit,2-digit no. and so on upto 5 digits.
num=int(input("enter the no. upto 5 digits: "))
if num>=0 and num<9:
    print("it is single digit")
elif num>=10 and num<99:
    print("it is 2-digit")
elif num>=100 and num<999:
    print("it is 3-digit")
elif num>=1000 and num<9999:
    print("it is 4-digit")
elif num>=10000 and num<99999:
    print("it is 5-digit")
else:
    print("invalid input")
print("thank you \n")
