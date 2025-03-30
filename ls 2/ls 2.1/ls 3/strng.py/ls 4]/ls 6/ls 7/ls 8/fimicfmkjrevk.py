n = int(input( "enter the num of terms:"))
a , b = 0,1
count= 0
print("Fibonacci series:")
while count < n:
    print(a, end="")
    temp = a + b
    a = b
    b = temp
    count += 1




