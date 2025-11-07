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
  
toyatocars = []
mahindracars = []      
        
while True:
    
    print("\nWelcome to Car Management System")
    print("Enter 1 to add Toyato car")
    print("Enter 2 to add Mahindra car")
    print("Enter 3 to view Cars")
    print("Enter 0 to exit\n")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        seat = int(input("Enter the number of seats: "))
        tyre = int(input("Enter the number of tyre: "))
        ac = input("Enter the avaibility of ac (y/n): ")
        
        tobj = Toyato(seat,tyre,ac)
        toyatocars.append(tobj)
   
    elif choice == 2:
        seat = int(input("Enter the number of seats: "))
        tyre = int(input("Enter the number of tyre: "))
        ss = input("Enter the avaibility of supersuspension (y/n): ")        
       
        mobj = Mahindra(seat,tyre,ss) 
        mahindracars.append(mobj)
        
    elif choice == 3:
        print("Enter 1 to view Toyato cars")
        print("Enter 2 to view Mahindra cars")
        
        ch = int(input("Enter your choice: "))
        if ch == 1:
            for obj in toyatocars:
                tobj.getdata()
        elif ch == 2:
            for obj in mahindracars:
                mobj.getdata() 
                
        else:
            print("Invalid choice") 
            
    elif choice == 0:
        print("Exiting the program.")
        break   
    
    else:
        print("Invalid choice. Please try again.")      
        

