try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma:"))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError :
    print("Error: Division by zero is not allowed.")
except SyntaxError:
    print("Comma is  missing , Enter Numbers seperated by a comma")
except:
    print("Wrong input:")
else:
    print("No exception occurred.")
finally:
    print("Execution completed.")
    