print("\nWelcome to file handling\n")

while True:
    print("Enter 1 to creat file ")
    print("Enter 2 to read file ")
    print("Enter 3 to write file ")
    print("Enter 4 to append file ")
    print("Enter 5 to exit file \n")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        file_name = str(input("\nEnter your File Name: "))

        with open(file_name , "x") as file:
            print(f"File {file_name} Created Successfully !")
  
    elif choice == 2:
        file_name = str(input("\nEnter File Name To Read: "))

        with open(file_name,"r") as file :
            print(file.read())

    elif choice == 3:
        file_name = str(input("\nEnter File Name to write somthings: "))
        
        with open(file_name , "w") as file:
            data1 = input("Enter data to write: ")
            file.write(data1)
            print("data Created Successfully !")
                      
    elif choice == 4:
        file_name = str(input("Enter file name to append: "))
        
        with open (file_name , "a") as file:
            data2 = str("Enter data to append: ") # for append we need to write in text file
            
            file.write("\n "+ data2)
  
    elif choice == 5:
        print("Exiting To filehandling !")
        break

    else:
        print("Invalid choice❌")
            