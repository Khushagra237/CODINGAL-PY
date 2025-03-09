print("Enter marks as input from user")
math = int(input("Enter the marks of math:"))
english = int(input("Enter the marks of english:"))
science = int(input("Enter the marks of science:"))
hindi = int(input("Enter the marks of hindi:"))
sum = math + english + science + hindi
print("sum of math, english , hindi, science is ", sum)
perc = (sum/400)*100
print(end= "Percentage Mark =" )
print(perc)