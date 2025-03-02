#unique and mutable
#unordered means no indexing
a={"ironman","hulk","thor","captain america"}
print(a)
print(type(a))
for x in a:
    print(x)

#functions
#add
a.add("spiderman")
print(a)
#pop
a.pop()
print(a)
#remove
# a.remove("hulk")
# print(a)
#discard
a.discard("thor")
print(a)
#copy
b=a.copy()
print(b)

a={"ironman","hulk","thor","captain america"}
b={"superman","batman","wonder-woman"}
c={"hulk","thor"}
#isdisjoint
print(a.isdisjoint(b))
print(a.isdisjoint(c))
#issubset
print(b.issubset(a))
print(c.issubset(a))
#issuperset
print(a.issuperset(b))
print(a.issuperset(c))
#update
a.update(b)
print(a)
#clear
# a.clear()
# print(a)


#union
print(a.union(c))
#difference
print(a.difference(c))
#difference update
a.difference_update(b)
print(a)
#intersection
print(a.intersection(c))
#intersection update
# a.intersection_update(c)
# print(a)
#symmetric difference
print(a.symmetric_difference(c))
#symmetric difference update
a.symmetric_difference_update(c)
print(a)



#problems
A={12,56,34,8,90,1,57}
print(max(A))
print(min(A))

B=[1,5,6,8,2]
C=[4,5,6,7]
D=[1,9,6,2,5]
print(set(B)&set(C)&set(D))

print(set(B).difference(set(C)))
A.discard(56)
print(A)

e={1,2,3,4,5,6}
f={2,4,5}
print(f.issubset(e))