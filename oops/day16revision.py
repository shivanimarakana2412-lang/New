"""constructor and destructor example"""

class student:
    
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old.")
        
    def __del__(self):
        print(f"{self.name} object is being destroyed.")
        
st1 = student("Shivani" , 17)
st2 = student("Krish" , 18)

st1.greet()
st2.greet()












