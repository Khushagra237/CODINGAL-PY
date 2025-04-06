rows = int(input("Enter the number of rows: "))
number = 1
print("Floyd's Triangle")
for i in range(0, rows):
    for j in range(0, i + 1):
        print(number, end=" ")
        number += 1
    print()