def hello():
    print("hello world")
hello()

def add():
    x=56
    y=23
    print(x+y)
add()

def add(x,y):
    sum=x+y
    return sum
a=23
b=11
result=add(23,11)
print(result)


#parameters--parameters are variables written inside the parenthesis with name of function.

#arguents--arguments are the value passed to the parameters while calling the function.


def rect(length,width):
    print("the area of rectangle is",length*width)

rect(4,5)


def hello1(name):
    print("hello,my name is ",name)
hello1("krish")

def hello2(*name):   #arbitary values calls by index number
    print("hello,my name is ",name[1])
hello2("krish","Ram","Krishna")

#return--return keyword in # python is used to exit a function and return the value of a function

#recurson--recursion means a function can call itself,giving us a benefit of looping through data in order to get a result

"""def hello3():
    print("hello")
    return hello3()
print(hello3())"""

def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))
print(fact(5))

#lambda function--it is used when an anonymous function is required for a short period of time.

a=lambda b: b*5
print(a(5))

x=lambda c,d,e: (c+d)*e
print(x(5,4,6))

#local variables--restricted to only one block of code and cannot be changed throughout the program.

#global variable--not restricted to one block of code and can be changed throughout the program.


#function to find maximum of three numbers
def maximum_num(val1,val2,val3):
    if val1>val2 and val1>val3:
        print(val1,"is the greatest number")
    elif val2>val1 and val2>val3:
        print(val2,"is the greatest number")
    else:
        print(val3,"is the greatest number")

print(maximum_num(34,76,56))

#list where the values are square of numbers between 1 and 30
def create_list():
    l=[]
    for i in range(1,31):
        l.append(i**2)

    return l
print(create_list())

#takes a number as a parameter and check if the number if number is prime or not
def check_prime(num):
    if num==1:
        print("it is not a prime number")
    if num==2:
        print("it is a prime number")
    if num>2:
        for i in range (2,num):
            if num%i==0:
                print("it is not a prime number")
                break
            else:
                print("it is a prime number")

check_prime(11)

#function to sum all the numbers in a list
def add(numbers):
    total=0
    for i in numbers:
        total=total+i
    return(total)

print(add([12,4,5,67,45]))

#solution using recursion
def add1(no):
    if len(no)==1:
        return (no[0])
    else:
        return (number[0]+add1(no[1:]))
print(add([12,4,5,67,34]))

#fibonacci sequence using recursion
def fs(number):
    if number==1:
        return(0)
    elif number==2:
        return(1)
    else:
        return(fs(number-1)+fs(number-2))
print(fs(8))