# If statement
print("If statement")
marks=93
if marks>=90:
    print("you will get A grade")
print("thank you \n")


# If-else statement
print("If else statement")
marks_1=87
if marks_1>=90:
    print("you will get A grade")
else:
    print("you will get B grade")
print("thank you \n")


# If elif else statement
print("If elif else statement")
marks_2=int(input("enter the marks :"))
if marks_2>=90:
    print("you will get A grade")
elif marks_2>=80 and marks_2<90:
    print("you will get B grade")
elif marks_2>=70 and marks_2<80:
    print("you will get C grade")
else:
    print("Fail")
print("thank you \n")


# Nested If statement
print("Nested If statement")
marks_3=int(input("enter your marks here:"))
if marks_3>=90:
    print("you will get A grade")
    if marks_3>=99:
        print("you are 1st in the school")
        if marks_3==100:
            print("you will get a holiday trip")
    if marks_3>=95 and marks_3<99:
        print("you are 1st in class")
else:
    print("try again")
print("thank you \n")


# Short hand If statement
#used when only one statement is there
print("Short hand If statement")
marks_4=90
if marks_4>=90: print("you will get A grade")
print("\n")


# Short hand If else statement
print("Short hand If else statement")
marks_5=95
print("you will get A grade") if marks_5>=90 else print("you will get B grade")
print("thank you \n")