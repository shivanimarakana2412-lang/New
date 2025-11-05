student = []

print("Welcome to the Student Data Organizer \n")

while True:
    print("Select an option: ")
    print("1.Add Students")
    print("2.Display All Students")
    print("3.Update Student Information")
    print("4.Delete Student")
    print("5.Display Subject Offered")
    print("6.Exit \n")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print("Enter student detail: \n")
        dt = {
           "StudentID" : int(input("Enter student id: ")),
           "Name" : input("Enter student name: "),
           "Age" : int(input("Enter student age: ")),
           "Grade" : input("Enter student grade: "),
           "Date of birth (YYYY-MM-DD)" : tuple(input("Enter students birthdate: ")),
           "Subjects" : set(input("Enter subjects: "))
        }
        
        student.append(dt)
        
        print("\n student added successfully ! \n")
        
    elif choice == 2 :
        for dt in student:
            print("---Display All Students---\n")
            print(f"studentId : {dt["StudentID"]} | Name : {dt["Name"]} | Age : {dt["Age"]} | Grade : {dt["Grade"]} | Subjects : {dt["Subjects"]} \n")

    elif choice == 3:
        StudentID = int(input("Enter student id to Update: "))
        for dt in student:
            if dt["StudentID"] == StudentID :
               dt["Name"] = input ("Enter student new Name: ") 
               dt["Age"] = input ("Enter student new Age: ") 
               dt["Grade"] = input ("Enter student new Grade: ") 
               dt["Date of birth (YYYY-MM-DD)"] = tuple(input("Enter student new  Date of birth (YYYY-MM-DD): ")) 
               dt["Subjects"] = set(input ("Enter student new Subjects: ")) 
               
               print("Student Updated \n")
         
    elif choice == 4:
        StudentID = int(input("Enter student id to remove: "))
    
        if StudentID in student:
                del student [StudentID] 
                print("Student removed \n")  
                break
        else:
            print("Student ID not found.\n")
    
    elif choice == 5:
        StudentID = int(input("Enter student id to print students subject: "))
        for dt in student:
           if dt["StudentID"]== StudentID:
               print(f"display all subjects = {dt['Subjects']}")
               print(f"All subjects offered: {' , '.join(dt['Subjects'])}\n")
               break
           else:
               print("Student not found.\n")
            
    elif choice == 6:
        print("Exiting")
        break
    
    else:
        print("Thank you for using the Personal Data Collector. Goodbye! \n")               
               
           
           
               
           
               
        
        
        
        

        