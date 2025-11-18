import datetime
now = datetime.datetime.now()

class AllData:
    def __init__(self, filename):
        self.filename = filename

    def AddEntry(self, text):
        with open(self.filename, "a") as file:
            file.write(text + "\n")
            print("\nEntry Added Successfully!\n")

    def ViewEntry(self):
        try:
            with open(self.filename, "r") as file:
                read = file.read()
                print("\nYour Journal entries\n------------------------------------\n")
                print(now ,"\n")
                print(read)
                print(now)
                print("Had a great session on OOP\n")
                
        except FileNotFoundError:
            print("File not found")

    def SearchEntry(self):
        with open("journal.txt","r")as file:
            line = file.readlines()
            for  linenum,line in enumerate(line):
               if keyword in line:
                   print(linenum,"          " , line)
                   
    def DeleteEntry(self):
        with open(self.filename,"w")as file:
             file.write("")
 

Adata = AllData("journal.txt")
print("\nWelcome to the Journal Manager!")
print("Please select an option:\n")
while True:
    print("1. Add new entry")
    print("2. View entries")
    print("3. Search entry")
    print("4. Delete entries")
    print("5. Exit\n")

    try:
        choice = int(input("User Input:\n"))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        entry = input("\nEnter your journal entry: \n")
        Adata.AddEntry(entry)
    
    elif choice == 2:
        Adata.ViewEntry()
    
    elif choice == 3:
        keyword=input("Enter a keyword for search: ")
        print("Show Matching Entries:\n ------------------------------------\n")
        print(now , "\n")
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