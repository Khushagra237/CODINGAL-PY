base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result_operator = base ** exponent
result_loop =1
result_loop *=base
if exponent < 0:
    result_loop = 1 / result_loop
    print(f"{base}^{exponent} using ** operator: {result_operator}")
    print(f"{base}^{exponent} using loop: {result_loop}")
