class India():
    def __init__(self):
        self.name = "India"
        self.capital = "New Delhi"
        self.population = 1393409038  # As of 2021
        self.area = 3287263  # in square kilometers
        self.currency = "Indian Rupee (INR)"
        self.languages = ["Hindi", "English"]
        self.independence_day = "15 August 1947"

    def get_info(self):
        return f"{self.name} - Capital: {self.capital}, Population: {self.population}, Area: {self.area} sq km, Currency: {self.currency}, Languages: {', '.join(self.languages)}, Independence Day: {self.independence_day}"
class USA1():
    def __init__(self):
        self.name = "United States of America"
        self.capital = "Washington, D.C."
        self.population = 331002651  # As of 2021
        self.area = 9833517  # in square kilometers
        self.currency = "United States Dollar (USD)"
        self.languages = ["English"]
        self.independence_day = "4 July 1776"

        def get_info(self):
            return f"{self.name} - Capital: {self.capital}, Population: {self.population}, Area: {self.area} sq km, Currency: {self.currency}, Languages: {', '.join(self.languages)}, Independence Day: {self.independence_day}"
    
    obj_ind = India()
    obj_usa = USA1()
    for country in (obj_ind, obj_usa):
        print(country.get_info())
