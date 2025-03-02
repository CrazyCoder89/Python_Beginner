# ordered and mutable data
# inside square brackets[]
# mutable once created can be changed
# multiple datatypes

fruits=["apple","mango","banana",12,45.10    ]
print(fruits)
print(type(fruits))


#list slicing
a=["ironman","thor","captain america","hulk"]
print(a[2])
print(a[-3])
print(a[1:3])
print(a[:2])
print(a[1:])
print(a[::2])
print(a[-3:-1])
print(a[::-1])
print(a[-1:-4:-1])


#list iteration
#for loop
a=["ironman", "thor", "captain america", "hulk"]
for i in a:
    print(i)

#for loop with range and length function
for i in range(len(a)):
    print(a[i])

#while loop
i=0
while i<len(a):
    print(a[i])
    i=i+1
    i+=1

#shorthand for loop
[print(i) for i in a]


#list functions
a=["ironman","thor","captain america","hulk","hulk"]
print(len(a))
print(a.count("hulk"))
print(a.append("spiderman"))
print(a)
print(a.insert(1,"vision"))
print(a)
print(a.remove("hulk"))
print(a)
print(a.pop(1))
print(a)
b=a.copy()
print(b)
print(a.index("ironman"))
c=["vision","spiderman"]
a.extend(c)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.clear()
print(a)



#list comprehension
l1=[30,40,50,60]
l2=[]
for i in l1:
    if i>45:
        l2.append(i)
print(l2)

l3=[i for i in l1 if i>45]
print(l3)



A=["Ross","Rachel","Monica","Joe"]
A[0],A[3]=A[3],A[0]
print(A)
A.insert(1,"Phoebe")
print(A)
A.pop(2)
print(A)


B=[13,7,12,10]
mul=1
for i in B:
    mul*=i
print(mul)
B.sort()
print(B)
#B=B[-1]
print(B[-1])
print(B[0])
