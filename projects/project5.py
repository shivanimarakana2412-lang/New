class Employee():
    def __init__(self, name, age , emp_id , salary ):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.salary = salary

    def getdata(self):
        print("\nName: " ,self.name)
        print("Age: " ,self.age) 
        print("ID: " ,self.emp_id)
        print("Salary: ",self.salary)
        
class Manager(Employee):
    def __init__(self, name, age , emp_id , salary, department ):
        super().__init__(name, age , emp_id , salary )
        self.department = department
        
    def getdata(self):
        print("\nName: ", self.name)
        print("Age: ", self.age)
        print("ID: ", self.emp_id)
        print("Salary: ", self.salary)
        print("Department: ", self.department)


class Developer(Employee):
    def __init__(self, name, age, emp_id , salary , pro_language):
        super().__init__(name , age , emp_id , salary)     
        self.pro_language = pro_language
    def getdata(self):
        print("\nName: ", self.name)
        print("Age: ", self.age) 
        print("ID: ", self.emp_id)
        print("Salary: ", self.salary)  
        print("programing Lanhuage: ", self.pro_language)
     

Employee_list = []
Manager_list = []
Developer_list = []

print("\n--- Python OOP Project: Employee Management System ---\n")

while True:

    print("Choose an option:")
    print("1. Create an Employee")
    print("2. Create a Manager")
    print("3. Create a Developer ")
    print("4. Show Details")
    print("5. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        emp_id = int(input("Enter Employee ID: "))
        salary = int(input("Enter salary: $ "))
        eobj = Employee(name, age , emp_id , salary)
        Employee_list.append(eobj)
        print(f"\nEmployee created with name: {name} , age: {age} , ID: {emp_id} and salary:$ {salary} .\n")

        print("---choose another operation---\n")
    
    elif choice == "2":
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = int(input("Enter salary: $ "))
        dept = input("Enter Department: ")
        mobj = Manager(name, age, emp_id , salary , dept)
        Manager_list.append(mobj)
        print(f"\nManager created with name: {name} , age: {age} , ID: {emp_id} , salary:$ {salary}, and department: {dept} .\n")

        print("---choose another operation---\n")

    elif choice == "3":
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        emp_id = input("Enter Employee ID: ")
        salary = int(input("Enter salary: $ "))
        pro_language = input("Enter Programming Language: ")
        dobj = Developer(name, age, emp_id, salary , pro_language)
        Developer_list.append(dobj)
        print(f"\nDeveloper created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary} and known programing language is {pro_language } .\n")

        print("---choose another operation---\n")

    elif choice == "4":
        print("\nchoose Details to show:\n")
        print("1.Employee")
        print("2.Manager")
        print("3.Developer")
        
        ch = int(input("\nEnter your choice: "))
        
        if ch == 1:
            print("\nEmployee Details: ")
            for obj in Employee_list:
                obj.getdata()
                print()
        elif ch == 2:
            print("\nManager Details: ")
            for obj in Manager_list:
                obj.getdata()
                print()                
        elif ch == 3:
            print("\nDeveloper Details: ")
            for obj in Developer_list:
                obj.getdata()
                print()
        else:
            print("Invalid choice!❌\n")        
        
    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")
