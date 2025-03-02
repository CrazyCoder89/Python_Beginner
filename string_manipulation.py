a="Harry Porter and the Goblin of Fire"
print(len(a))
print(a.count("o"))
print(a.upper())
print(a.lower())
print(a.index("o",15,34))
print(a.capitalize())
print(a.casefold())  #to covert string into lower case
print(a.find("e",15,34))
name="john"
age=20
b="My name is {} and my age is {}"
print(b.format(name,age))  #to write variables inside a string
print(name.center(10,'*'))



# String Functions
#1 isalnum -- alpha numeric and does not allows space and symbols
#2 isalpha -- all characters are alphabets
#3 isdecimal -- all characters are decimal
#4 isdigit -- all characters are digits
#5 isnumeric -- all characters are numeric
#6 islower -- string is lower or not
#7 isupper -- string isupper or not
#8 isspace -- all characters in string has whitespace
#9 istitle -- follow title rule
#10 endswith -- string ends with specified value
#11 startswith -- string starts with specified value
#12 swapcase -- lower case becomes upper case and vice a versa
#13 strip -- trimmed version of string
#14 split -- splits the string at the specified seperator,and returns a list
#15 ljust -- returns a left justified version of string
#16 rjust -- returns a right justified version of a string
#17 replace -- returns a string where a specified value is replaced with a
#18 rindex -- searches the string for a specified value and return the last positon of where it was found
#19 rfind -- searches the string for a specified value and return the last positon of where it was found



#Slicing in Strings
a="Harry Potter and the Goblet of fire"
b="0123456789"
print(a)
print(a[0:5])
print(a[6:12])
print(a[:5])
print(a[-4:])
print(b[::2])
print(b[:7:2])
print(b[::-1])
print(b[6::-1])


A="OOTD.YOLO.ASP.BRB.GTG.OTW"
print(A.split("."))
a="krish"
print(sorted(a))
print(a.replace("k",""))
Z="F.R.I.E.N.D.S"
print(Z.replace(".",""))

f="she sells seashells on the sea shore"
print(f.count("sea"))



b=input("enter anything here:")
print(b[::-1])
print()

c=input("enter anything here:")
print(c.isdigit())

d=input("enter anything here:")
temp=d[::-1]
if d==temp:
    print("palindrome")
else:
    print("not a palindrome")

e=input("enter anything here:")
vowels=0
for i in e:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        vowels+=1
print(vowels)

f=input("enter anything here:")
print(f.istitle())