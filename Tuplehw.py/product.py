def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
numbers_tuple = (1, 2, 3, 4) 
result = calculate_product(numbers_tuple)
print("The product of the numbers in the tuple is:", result)