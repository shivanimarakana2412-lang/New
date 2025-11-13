# print("Welcome to Personal Journal Manager!\n")
# print("Please select an option: \n")

# while True:
#     print("1. Add a New Entry")
#     print("2. View All Entry")
#     print("3. Search for an Entry")
#     print("4. Delete all Entry")
#     print("5. Exit\n")
    
#     choice = int(input("User Input:\n"))
    
#     if choice == 1:
#         file_name = str(input("Enter file name to append: "))

#         with open(file_name,"a") as file:
#             data2=input("Enter data to add in your file to append: ")
#             file.write("\n"+ data2)
            
            
#     elif choice == 2:
#         file_name = str(input("\nEnter File Name To Read: "))

#         with open(file_name,"r") as file :
#             print(file.read())
            

#     elif choice == 4:
#         file_name = str(input("\nEnter File Name to : "))
        
#         with open(file_name , "w") as file:
#             data1 = input("Enter data to write: ")
#             file.write(data1)
#             print("data Created Successfully !")
class FileData:
    def _init_(self, filename):   # ✅ અહીં બે underscores આગળ અને પાછળ
        self.filename = filename
       # print("File Name is:", filename)

    def AddEntry(self, text):
        with open(self.filename, "a") as file:
            file.write(text + "\n")
        print("Entry Added Successfully")

    def ViewEntry(self):
        try:
            with open(self.filename, "r") as file:
                a = file.read()
                print("\n----- Journal entries -----")
                print(a)
        except FileNotFoundError:
            print("File not found")

    def SearchEntry(self):
        c = input("Enter a keyword for search: ")
        with open("main.txt" , "r") as file:
            b = file.readlines()
            for line in b:
                if c in line:
                    print(line.strip())

    def DeleteEntry(self):
        with open(self.filename, "w") as file:
            file.write("")
        #print("All journal entries deleted")


fd = FileData("main.txt")  # ✅ હવે કોઇ error નહીં આવે

while True:
    print("\nWelcome to the journal manager!!!")
    print("1. Add new entry")
    print("2. View Entries")
    print("3. Search Entry")
    print("4. Delete Entries")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        entry = input("\nEnter your journal entry: ")
        fd.AddEntry(entry)
    elif choice == 2:
        print("Journal Entries:")
        fd.ViewEntry()
    elif choice == 3:
        print("Show Matching Entries:")
        fd.SearchEntry()
    elif choice == 4:
        fd.DeleteEntry()
    elif choice == 5:
        print("Exiting Program...")
        break
    else:
        print("Invalid choice! Please try again.")