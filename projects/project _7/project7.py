from datetime_tools import *
from math_ops import *
from random_ops import *
from uuid_tools import *
from file_manager import AllData
from explorer import explore_module

if __name__ == "__main__":

    print("\n================================")
    print("Welcome to Multi-Utility Toolkit")
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

        # ==== DATETIME SECTION ====
        if choice == 1:
            while True:
                print("\nDatetime and Time operations\n")
                print("1. Display current Date and Time")
                print("2. Calcuate difference between Two Date/Time")
                print("3. Formate date into custom formate")
                print("4. Stopwatch")
                print("5. Countdown")
                print("6. Back to Main Menu\n")

                ch = int(input("Enter: "))

                if ch == 1:
                   print(current_datetime())

                elif ch == 2:
                    f = input("First date (YYYY-MM-DD): ")
                    s = input("Second date (YYYY-MM-DD): ")
                    print("Difference:", date_difference(f, s), "days")

                elif ch == 3:
                    f, c = format_date()
                    print("Formatted:", f)
                    print("Converted:", c)

                elif ch == 4:
                    print("Elapsed:", stopwatch(), "seconds")

                elif ch == 5:
                    sec = int(input("Enter seconds: "))
                    print(countdown(sec))
                else:
                    break

        # ==== MATH SECTION ====
        elif choice == 2:
            while True:
                print("\nMathematical operations\n")
                print("1. Calculate Factorial")
                print("2. Solve Compound Intrest")
                print("3. Trigonometric Calculation")
                print("4. Back to Main Menu\n ")

                ch = int(input("Enter: "))

                if ch == 1:
                    n = int(input("Enter number: "))
                    print(factorial(n))

                elif ch == 2:
                    p = int(input("Enter principal amount: "))
                    r =  int(input("Enter rate of intrest(in %): "))
                    t = int(input("Enter a time (in year): "))
                    print(compound_interest(p, r, t))

                elif ch == 3:
                    print(trig_values())
                else:
                    break
                
        # ==== RANDOM SECTION ====
        elif choice == 3:
            while True:
                print("\nRandom Data Generation\n")
                print("1. Generate random number")
                print("2. Generate random list")
                print("3. Creat random OTP")
                print("4. Generate random password")
                print("5. Back to Main Menu\n ")
               
                ch = int(input("Enter: "))

                if ch == 1:
                    print(random_number())

                elif ch == 2:
                    print(random_list())

                elif ch == 3:
                    print(generate_otp())

                elif ch == 4:
                    print(random_password())
                else:
                    break

        # ==== UUID ====
        elif choice == 4:
            print("Generated UUID:", generate_uuid())

        # ==== FILE MANAGER ====
        elif choice == 5:
            mgr = AllData("journal.txt")
            while True:
                print("\n1. Add Entry")
                print("2. View Entries")
                print("3. Search Entry")
                print("4. Delete Entries")
                print("5. Back")

                ch = int(input("Enter: "))

                if ch == 1:
                    text = input("Write: ")
                    mgr.AddEntry(text)

                elif ch == 2:
                        mgr.ViewEntry()

                elif ch == 3:
                    keyword = input("Search: ")
                    mgr.SearchEntry(keyword)

                elif ch == 4:
                    mgr.DeleteEntry()
                else:
                    break           
                    

        # ==== EXPLORER ====
        elif choice == 6:
            module = input("Enter module name: ")
            attrs = explore_module(module)
            print(attrs)

        elif choice == 7:
            print("Thank you for using the toolkit!")
            break
