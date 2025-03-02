#ordered and unmutable

a=("mango","apple")
print(type(a))
print(a)
b=("ironman",)
print(type(b))

#slicing
a=("Oneplus","Vivo","Redmi","Samsung","Apple")
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[::2])
print(a[::-1])
print(a[2::-1])

#iteration
#for loop
for i in a:
    print(i)

#with range and length in for loop
for i in range(len(a)):
    print(a[i])

#while loop
i=0
while i<len(a):
    print(a[i])
    i+=1

#conversion of tuples
a=("Oneplus","Samsung","Apple")
print(type(a))

a=list(a)
print(type(a))
a.append("Vivo")
print(a)
a=tuple(a)
print(type(a))
print(a)


#functions
#1 count
print(a.count("Apple"))
#2 index
print(a.index(("Apple")))



#