country_code = {'India': '0091',
                    'Australia': '0061',
                    'Nepal': '00977'}

country=input("enter coumtry name to get code: ")
if country in country_code:
    print(f"Country code for {country} is {country_code[country]}")
else:
    print("Country not found in the list")
    exit()
    