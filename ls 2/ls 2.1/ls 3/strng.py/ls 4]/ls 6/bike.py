print("Select your ride:")
print("1. Bike")
print("2. Car")
choice = int(input("Enter choice: "))

if choice == 1:
    print("What type of Bike?")
    print("1. Scooty")
    print("2. Scooter")
    choice2 = int(input("Enter choice2: "))
    
    if choice2 == 1:
        print("You have selected Scooty")
    elif choice2 == 2:
        print("You have selected Scooter")
    else:
        print("Invalid choice for Bike type")

elif choice == 2:
    print("What type of Car?")
    print("1. Sedan")
    print("2. XUV")
    choice3 = int(input("Enter choice3: "))
    
    if choice3 == 1:
        print("You have selected Sedan")
    elif choice3 == 2:
        print("You have selected XUV")
    else:
        print("Invalid choice for Car type")

else:
    print("Invalid choice for ride type")

    
   