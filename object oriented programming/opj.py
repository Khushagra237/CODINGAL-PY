class RomanConverter:
    def __init__(self, number):
        if not (0 < number < 4000):
            raise ValueError("Number must be between 1 and 3999")
        self.number = number
        self.roman_numeral = ""

    def convert_to_roman(self):
        roman_map = [
            (1000, "M"), (900, "CM"),
            (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"),
            (1, "I")
        ]

        num = self.number
        result = ""

        for value, symbol in roman_map:
            while num >= value:
                result += symbol
                num -= value

        self.roman_numeral = result
        return result

    def __str__(self):
        return f"{self.number} in Roman numerals is {self.roman_numeral or self.convert_to_roman()}"

