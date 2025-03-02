#type--show data type
name = "john"
print(type(name))

age = 232
print(type(age))

#implicit conversion
a=123
b=1.23
print(type(a))
print(type(b))
c=a+b
print(c)
print(type(c))

#explicit conversion
d='123'
e=13.44
print(type(d))
print(type(e))
d=int(d)
f=d+e
print(f)
print(type(f))
