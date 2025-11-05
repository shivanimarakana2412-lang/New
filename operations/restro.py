while True:
    print("Enter 1 to order Breakfast")
    print("Enter 2 to order Lunch")
    print("Enter 3 to order Starter")
    print("Enter 4 to order Main course")
    print("Enter 5 to order Desert")
    print("Enter 0 to exit!!!")

    print()
    
    choice = int(input("Enter a number between 0 - 5 for order :"))

    if choice == 1:
        while True:
            print("Enter 1 to order Bread jam")
            print("Enter 2 to order Thepla")
            print("Enter 3 to oeder Bread butter")
            print("Enter 0 to Exit")
            
            print()
            
            choice = int(input("Enter a number between 0 - 3 for Breakfast :"))
            
            if choice == 1:
                print("Bread jam")
            elif choice == 2:
                print("Thepla")
            elif choice == 3 :
                print("Bread butter")
            elif choice == 0:
                print("Exit!!")
                break
            else:
                print("Invalid")
                
    if choice == 2:
        while True:
            print("Enter 1 to order Sabji Roti")
            print("Enter 2 to order Dal bhat")
            print("Enter 3 to oeder Sweets")
            print("Enter 0 to Exit")
            
            print()
            
            choice = int(input("Enter a number between 0 - 3 for Lunch :"))
            
            if choice == 1:
                print("Sabji Roti")
            elif choice == 2:
                print("Dal bhat")
            elif choice == 3 :
                print("Sweets")
            elif choice == 0:
                print("Exit!!")
                break
            else:
                print("Invalid")
                                
    if choice == 3:
        while True:
            print("Enter 1 to order Sizlar")                  
            print("Enter 2 to order Panipuri")
            print("Enter 3 to oeder Noodles")
            print("Enter 0 to Exit")
            
            print()
            
            choice = int(input("Enter a number between 0 - 3 for Starter :"))
            
            if choice == 1:
                print("Sizlar")
            elif choice == 2:
                print("Panipuri")
            elif choice == 3 :
                print("Noodles")
            elif choice == 0:
                print("Exit!!")
                break
            else:
                print("Invalid")
                

    if choice == 4:
        while True:
            print("Enter 1 to order Dal Makhani")                  
            print("Enter 2 to order Dhosa")
            print("Enter 3 to oeder Panir Bhurji")
            print("Enter 0 to Exit")
            
            print()
            
            choice = int(input("Enter a number between 0 - 3 for Main course :"))
            
            if choice == 1:
                print("Dal Makhani")
            elif choice == 2:
                print("Dhosa")
            elif choice == 3 :
                print("Panir Bhurji")
            elif choice == 0:
                print("Exit!!")
                break
            else:
                print("Invalid")
                
    if choice == 5:
        while True:
            print("Enter 1 to order Oreo Brownie ")                  
            print("Enter 2 to order Mava choco badam")
            print("Enter 3 to oeder Chocolate Brownie")
            print("Enter 0 to Exit")
            
            print()
            
            choice = int(input("Enter a number between 0 - 3 for Desert :"))
            
            if choice == 1:
                print("Oreo Brownie")
            elif choice == 2:
                print("Mava choco badam")
            elif choice == 3 :
                print("Chocolate Brownie")
            elif choice == 0:
                print("Exit!!")
                break
            else:
                print("Invalid")
                
    if choice == 0:
        print("exit")
            
            
            
            
            