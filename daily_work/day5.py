# patterns

# 1. simple

for i in range (5):
    #print("* * * * *")  
    print(" * " * 5)
    
    
# 2. Right angle

for i in range(1,6):
    print(" * " * i)


# 3.string loop -  Number row square

for i in range(1,6):
    print(str(i)*5)


# 4.number tringle

for i in range(1 , 6):
    print(str( i ) * i)
    
    
# 5. right number / nested loop

for i in range(1,7):
    for j in range(1,i):
        print(j , end=" ")
    print("\n")


# 6.reverse tringle

for i in range(5,0,-1):
    print("*" * i)
    
    
#pizza in while true

while True:
    print("Enter 1 to order pizza")
    print("Enter 2 to order burger")
    print("Enter 0 to exit !")
    
    print()
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        while True:
                print("Enter 1 to order cheese pizza")
                print("Enter 2 to order corn pizza")
                print("Enter 0 to exit !")
                
                print()
                
                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                    print("cheese pizza")
                elif choice == 2:
                    print("corn pizza")
                elif choice == 0:
                    print("bye")
                    break
                else:
                    print("invalid")            
    if choice == 2:
        while True:
                print("Enter 1 to order vegetable burger")
                print("Enter 2 to order paneer makhani")
                print("Enter 0 to exit !")
                
                print()
                
                choice = int(input("Enter your choice: "))
                
                                
                if choice == 1:
                    print("vegetable burger")
                elif choice == 2:
                    print("paneer makhani")
                elif choice == 0:
                    print("bye")
                    break
                else:
                    print("invalid")      
    if choice == 0:
        print("Exiting!!")
    else:
        print("Invalid!!")       
        
        
        
       