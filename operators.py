# Arithmetic operators
# + - * / // ** %

print("Arithmetic operators")
a=2-1
print(a)
b=8%3 #modulus-- %
print(b)
c=8//3 #floor divison-- //
print(c)
d=2**5 #exponential-- **
print(d,"\n")

# Comparison operators
# < > == <= >= !=
print("Comparison operators")
e= 3>6 #greater than
print(e)
f= 3!=4 #not equal to
print(f)
g= 3==3 #equal to
print(g)
h= 5<=7 #less than equal to
print(h,"\n")

# Logical operators
# and or not
print("Logical operators")
i= 5>2 and 7<9 #and operator
print(i)
j= 5>2 or  7>9 #or operator
print(j)
k= not 5>2 #or operator
print(k,"\n")

# Assignment operator
# = += -= *= /= ....
print("Assignment operator")
l=1
l += 5
print(l)
l -= 5
print(l)
l *= 10
print(l,'\n')

# Identity operator
# is 'is not'
print("Identity operator")
m=1234
n='1234'
print(m is n)
print(m is not n ,'\n')

# Bitwise operator
# & | ^ << >> (compare binary numbers)
print("Bitwise operator")
print(bin(10)) #binary no. syntax
o=10
p=8
print(o & p) #bitwise and
print(o | p) #bitwise or
print(o ^ p) #bitwise xor
print(o >> 2) #zero fill left shift
print(o << 2,'\n') #zero fill right shift

# Membership operators
# in 'not in'
print("Membership operator")
q="hello"
print("p" in q)
print("l" in q)
print("a" not in q,'\n')

print("Operators Explained")