rowSize = int(input("Enter the number of rows: "))
if rowSize%2 == 0:
    halfDiamond = rowSize//2
else:
    halfDiamond = rowSize//2 + 1
space = halfDiamond - 1
for i in range(halfDiamond):
    for j in range(1,space+1):
        print(" ", end="")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        num = num + 1
    print()
    space =  1
for i in range(1, halfDiamond):
    for j in range(1, space+1):
        print(" ", end="")
    space = space + 1
    num = 1
    for j in range(1,2*(halfDiamond-i)-1):
        print(end=str(num))
        num = num + 1
    print()