string = input("please enter your own word :")
char = input("please enter your own character :")
i = 0
count = 0
while i < len(string):
    if(string[i] == char):
        count += 1
        
    i = i + 1
print("The number of times the character appears in the string is : ", count)

