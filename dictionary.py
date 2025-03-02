#dictonary
#in form of key and values
# enclosed in{}
employee_data={"name":"John","age":24,"gender":"male"}
print(employee_data)
print(employee_data["gender"])

#iteration
student={"name":"John","class":"6th","roll_no.":23}
for x in student:
    print(x)

for x in student:
    print(student[x])

for x in student.values():
    print(x)

for x,y in student.items():
    print(x,":",y)

#functions
#get
x=student.get("name")
print(x)
#item
a=student.items()
print(a)
#keys
b=student.keys()
print(b)
#values
c=student.values()
print(c)
#copy
d=student.copy()
print(d)
#setdefault
e=student.setdefault("roll_no.",24)
print(e)
#update
#pop
#popitem
#clear


#nested dictionaries
employee={1:{"name":"John","age":24,"gender":"male"},
          2:{"name":"Lisa","age":23,"gender":"female"},
          3:{"name":"Peter","age":22,"gender":"male"}}
print(employee[2]["age"])
print(employee[1]["gender"])
print(employee[1])


#problems
#import json
#student_data={"name":"David","age":13,"marks":87}
#print(type(student_data))
#data=json.dumps(student_data)
#print(data)
#print(type(data))

#student_data1={"name":"David","age":13,"marks":87}
#data1=json.load(student_data1)
#print(data1)


#pretty print
import json
student={"name":"David","age":13,"marks":87}
data=json.dumps(student,indent=4,separators=(",","="))
print(data)

#sort json keys and write them into a file
#f=open("demo.json","w")
#json.dumps(student,indent=4,sort_keys=True)
#f.write(data)
#print(student)

student1="""{"student":{
        "grade":{
            "name" : "David",
                "marks":{
                    "math":87,}
            }
}"""

#data1=(json.loads(student1))
#print(data1["student"]["grade"]["name"]["marks"])


A={"a":12,"b":23,"c":6,"d":91,"e":45}
A=sorted(A.values())
print(A)

B={}
for i in range (1,15):
    B[i]=i**2
print(B)

C={"a":1,"b":2,"c":3,"d":4,"e":5}
prod=1
for i in C:
    prod*=C[i]
print(prod)

D={12:"a",23:"b",6:"c",91:"d",45:"e"}
D=sorted(D.keys())
print(D)