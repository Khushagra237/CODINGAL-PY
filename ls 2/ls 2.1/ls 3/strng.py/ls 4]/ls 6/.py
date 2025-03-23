medical_cause=input("did you have a medical cause Y or N: ")
atten=int(input("enter the attendance of the student: "))
if medical_cause=="Y":
    print("student is allowed ")
else:
    if atten>=75:
        print("student is allowed")
    else:
        print("student is not allowed")