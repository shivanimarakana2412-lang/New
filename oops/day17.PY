class Animal:  
    def sound(self):
        return "Makes a sound"

class Dog(Animal):  
    def bark(self):
        return "Barks"

dog = Dog()
print(dog.sound())  # Output: Makes a sound
print(dog.bark())   # Output: Barks







class Car():
    def __init__(self,seat,tyre):
        self.seat = seat
        self.tyre = tyre
        
class Toyato(Car):
    def __init__(self,seat,tyre,ac):
        super().__init__(seat,tyre)
        self.ac = ac
        
    def getdata(self):
        print(f"The car has features: seat-{self.seat}, tyre-{self.tyre}, ac-{self.ac}")
        
class Mahindra(Car):
    def __init__(self, seat, tyre,supersuspension):
        super().__init__(seat, tyre)
        self.supersuspension =supersuspension
    def getdata(self):
        print(f"The car has features: seat-{self.seat}, tyre-{self.tyre}, ac-{self.supersuspension}")
        
inova = Toyato(5,4,"available")
xuv = Mahindra(7,4,"not available")

print(inova.getdata())
print(xuv.getdata())        
        