"""Encaptulation example"""

# 3 methods 
#     1. setData ----> access and modify private variable
#     2. getData ----> access and modify private variable
#     3.private variable ----> "__" variable ke aage lage do underscores 
#

class Car:
    name = None
    brand = None
    
    def setData(self , name , brand):
        self.name = name
        self.brand = brand
        
    def getData(self):
        print(f"The name of car is {self.name} and the brand is {self.brand}")
        
obj = Car()
obj2 = Car()
    
obj.setData("XUV" , "Mahindra")
obj2.setData("Mustang" , "Ford" )
    
obj.getData()
obj2.getData() 
    
