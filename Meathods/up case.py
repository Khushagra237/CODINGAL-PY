class IOstring():
    def __init__(self):
        self.string = ""
    def get_String(self):
        self.str1 = input("Enter a string: ")
    def print_String(self):
        print("The string is: ", self.str1.upper())

str1 = IOstring()
str1.get_String()
str1.print_String() 