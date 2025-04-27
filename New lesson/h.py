try:
    age= int(input("Enter your age:"))
    if age < 0:
        print("age can't be negtive")
    else:
        if age % 2 == 0:
            print("age is even")
        else:
            print("age is odd")
except ValueError:
    print("Invalid input, please enter a valid age.")