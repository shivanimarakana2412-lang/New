students =[]

while True:
    print("\n welcome to our programme! \n")
    
    print("1.Add")
    print("2.Read")
    print("3.Delete")
    print("4.Update")
    print("0.Exit \n")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        st = {
        "stId" : int(input("Enter student Id: ")),
        "name" : input("Enter student name: "),
        "city" : input("Enter student city: ")          
        }
        
        students.append(st)
        
        print("\n student added successfully ! \n")
        
    elif choice == 2 :
        for st in students:
            print(f"student Id : {st["stId"]} , student Name : {st["name"]} , student city : {st["city"]} \n")
            
    
    elif choice == 3 :
        stId = int(input("Enter student id to remove: "))
        for st in students:
            if st in students:
                students.remove(st)  
                print("Student removed \n")  
            else:
                print("Student not found \n")
                
                
    elif choice == 4:
        stId = int(input("Enter student id to Update: "))
        for st in students:
            if st ["stId"] == stId:
                st["name"] = input ("Enter student new name: ") 
                st["city"] = input ("Enter student new city: ")  
                
                print("Student Updated \n")  
            else:
                print("Student not found \n")
                
                
    elif choice == 0:
        print("Exiting")
        break
    
    else:
        print("Invalid!!")
        
    