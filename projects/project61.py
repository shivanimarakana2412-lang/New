import datetime
now = datetime.datetime.now()

class AllData:
    def __init__(self, filename):
        self.filename = filename

    def AddEntry(self, text):
        try:
            with open(self.filename, "a") as file:
                file.write(text + "\n")
                print("\nEntry Added Successfully")
        except FileNotFoundError:
            print("File not found")
            
    def ViewEntry(self):
        try:
            with open(self.filename, "r") as file:
                read = file.read()
                print("\n-----Your Journal entries-----\n")
                print(now)
                print(read)
                print(now)
                print("Had a great session on OOP")
                
        except FileNotFoundError:
            print("File not found")

    def SearchEntry(self):
        keyword=input("Enter a keyword for search:")
        with open("journal.txt","r")as file:
            line = file.readlines()
            for  linenum,line in enumerate(line):
               if keyword in line:
                   print(linenum,"          " , line)
    def DeleteEntry(self):
        with open(self.filename,"w")as file:
             file.write("")
 

Adata = AllData("journal.txt")

while True:
    print("\nWelcome to the Journal Manager!\n")
    print("1. Add new entry")
    print("2. View entries")
    print("3. Search entry")
    print("4. Delete entries")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        entry = input("\nEnter your journal entry: ")
        Adata.AddEntry(entry)
    
    elif choice == 2:
        Adata.ViewEntry()
    
    elif choice == 3:
        print("Show Matching Entries:\n")
        print(now)
        Adata.SearchEntry()
    
    elif choice == 4:
        sure = str(input("Are you sure you want to delete(yes/no): "))
        if sure == "yes":
            print("All journal has been deleted!!")
        elif sure == "no":
            print("Ok")
        else:
            print("No journal entries to delete.") 
       
        Adata.DeleteEntry()
   
    elif choice == 5:
        print("Thank you for using personal journal manager . Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select between 1-5.")