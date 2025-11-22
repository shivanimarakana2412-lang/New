from datetime import datetime     
now = datetime.now()
import uuid
import math
import random

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = datetime.now()
    input("Press Enter to stop the stopwatch...")
    end_time = datetime.now()       # current datetime
    total_time = end_time - start_time
    seconds = total_time.total_seconds()
    print(f"\nElapsed time: {round(seconds, 2)} seconds")

def countdown_timer():
    sec = int(input("Enter seconds for countdown: "))
    while sec > 0:
        mins, secs = divmod(sec, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        sec -= 1
    print("Time's up!")

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

print("\n================================")
print("Welcome to Multi-utility Toolkit")
print("================================\n")
while True:
    print("choose an option:")
    print("1. Datetime and Time operations")
    print("2. Mathematical operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Indentifiers")
    print("5. File operations (custom Modules)")
    print("6. Explore Module Attribute")
    print("7. Exit")
    print("\n================================\n")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        while True:
            print("\nDatetime and Time operations\n")
            print("1. Display current Date and Time")
            print("2. Calcuate difference between Two Date/Time")
            print("3. Formate date into custom formate")
            print("4. Stopwatch")
            print("5. Countdown")
            print("6. Back to Main Menu\n")
            
            ch = int(input("Enter a number: "))
            
            if ch == 1:
                print(f"Current Date and Time: {now.strftime("%d-%m-%Y %H:%M:%S")}")
            
            elif ch == 2 :

                fdate_str = input("Enter the first date (YYYY-MM-DD): ")
                sdate_str = input("Enter the second date (YYYY-MM-DD): ")

                # String → datetime conversion 
                fdate = datetime.strptime(fdate_str, "%Y-%m-%d")
                sdate = datetime.strptime(sdate_str, "%Y-%m-%d")

                difference = sdate - fdate

                print("Difference:", difference.days, "days")
                
            elif ch == 3:
                
                formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
                print("Formatted Date:", formatted_date)

                date_string = formatted_date
                converted_date = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
                print("Converted Datetime Object:", converted_date)
                
            elif ch == 4 :
                
                stopwatch()
            
            elif ch == 5 :
                
                countdown_timer()        
                    
            elif ch == 6:
                print("Back to main menu")
                break

    elif choice == 2:
        while True:
            print("\nMathematical operations\n")
            print("1. Calculate Factorial")
            print("2. Solve Compound Intrest")
            print("3. Trigonometric Calculation")
            print("4. Back to Main Menu\n ")
            
            ch = int(input("Enter a number: "))
            
            if ch == 1 :
                fact = int(input("Enter a number to get factorial: "))
                print(math.factorial(fact))
                print("\n================================\n")
                
            elif ch == 2 :
                amount = int(input("Enter principal amount: "))
                intrest = int(input("Enter rate of intrest(in %): "))
                time = int(input("Enter a time (in year): "))
                
                compond_interst = amount * intrest * time / 100
                
                print(compond_interst)                
           
            elif ch == 3 :
                #sine = int(input("Enter the number (30 , 45 , 60 , 90):"))
                print(math.sin(math.radians(30)))  # Output: 0.5
                print(math.cos(math.radians(60)))  # Output: 0.5
                print(math.tan(math.radians(45)))  # Output: 1.0
            
            else:
                print("Back to main menu")
                break
            
    elif choice == 3:
        while True:
            print("\nRandom Data Generation\n")
            print("1. Generate random number")
            print("2. Generate random list")
            print("3. Creat random OTP")
            print("4. Generate random password")
            print("5. Back to Main Menu\n ")
            
            ch = int(input("Enter a number: "))
            
            if ch == 1 :
                print(random.randint(1,100))
                
            elif ch == 2 :
                items = ["apple", "kiwi", "mango", "banana"]
                random_list = random.sample(items, k=3)
                print(random_list)
            
            elif ch == 3 :
                otp = " "
                for i in range(6):
                    otp += str(random.randint(0, 9))
                print("Your OTP:", otp) 
            
            elif ch == 4 :
                letters = "abcdefghijklmnopqrstuvwxyz"
                numbers = "0123456789"
                symbols = "!@#$%^&*"

                all_chars = letters + letters.upper() + numbers + symbols

                password = ""
                for i in range(8):
                    password += random.choice(all_chars)

                print("Your Password:", password)
    
            else :
                print("Back to main menu")
                break               
      
    elif choice == 4:
        while True:
            print("\nGenerate Unique Indentifiers\n") 
            print("1. Generate UUID")
            print("2. Back to Main Menu\n ")
            
            ch = int(input("Enter a number: "))
            
            if ch == 1 :
                Id = uuid.uuid4() 
                print(f"Generated UUID: {Id}") 
                print("\n================================\n")
                
            else: 
                print("Back to main menu")
                break
                    
    elif choice == 5:
        
        print("\nFile operations (custom Modules)\n")
        
        Adata = AllData("journal.txt")
        
        print("\nWelcome to the Journal Manager!")
        print("Please select an option:\n")
        while True:
            print("1. Add new entry")
            print("2. View entries")
            print("3. Search entry")
            print("4. Delete entries")
            print("5. Back to Main Menu\n \n")

            try:
                ch = int(input("User Input:\n"))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if ch == 1:
                entry = input("\nEnter your journal entry: \n")
                Adata.AddEntry(entry)
    
            elif ch == 2:
                Adata.ViewEntry()
    
            elif ch == 3:
                keyword=input("Enter a keyword for search: ")
                print("Show Matching Entries:\n ------------------------------------\n")
                print(now , "\n")
                Adata.SearchEntry()
    
            elif ch == 4:
                sure = str(input("Are you sure you want to delete(yes/no): "))
                if sure == "yes":
                    print("All journal has been deleted!!")
                elif sure == "no":
                    print("Ok")
                else:
                    print("No journal entries to delete.") 
       
                Adata.DeleteEntry()
          
            else:
                print("Back to main menu")
                break
            
        
    elif choice == 6:
        print("Explore Module Attributes:")
        module_name = input("Enter module name to explore: ")

        try:
            module = __import__(module_name)
            attrs = [a for a in dir(module) if not a.startswith("_")]  # clean list

            print(f"Available Attributes in {module_name} module:")
            print(attrs)
            print("===========================")

        except ModuleNotFoundError:
            print("Module not found. Try a valid module name.")
        
    elif choice == 7 :
        
        print("\n==============================================\n")
        print("Thank you for using the Multi - Utility Toolkit!")    
        print("\n===============================================\n")
       
        break
    
    else :
        print("Invalid choice !! Try Again .")

        
            
            
    
           
           
           
           
           
           
           
           
           
           
            
            
            
            
            
                      




