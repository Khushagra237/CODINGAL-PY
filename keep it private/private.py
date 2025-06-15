class myClass:

    #private variable
    __privateVar = 0
    #private method
    def __privateMethod(self):
        print("I am inside class myClass")
        #function to print value of private variable
    def hello(self):
        print("Private variable value : ", myClass.__privateVar)
            # Object creation and meathod call
           
           
foo = myClass()
foo.hello()
foo.__privateMethod

