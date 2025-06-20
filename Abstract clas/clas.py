# Import necessary Modules
from abc import ABC, abstractmethod
#Create base class
class AbstractClass(ABC):
#Function to print a value
 def print(self, x):
    print("Passed value :" , x)

 #Abstract Method
 @abstractmethod
 def task(self):
   print("We are inside Abstract class")

#create sub class
class test_class(AbstractClass):
    def task(self):
        print("We are inside test_class")
#obj of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)