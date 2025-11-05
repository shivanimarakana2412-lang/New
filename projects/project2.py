
print("Welcome to the Pattern Generator and Number Analyzer!")

print()

while True:
    print("Select an option: ")
    print()
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        
        choice =  int(input("Enter the number of rows for the pattern: "))
        
        print("Pattern:")
        
        for i in range(1 , choice+1):
            print(" * " * i)
            
    elif choice==2: 
        
        start=int(input("Enter the start of the range : "))
        end=int(input("Enter the end of the range : "))
        sum=0
        
        for i in range(start,end+1): 
            if i%2==0:
                print("Number", i ,"is Even")
            else:
                print("Number", i ,"is Odd")
            sum=sum+i
            
        print("sum of all numbers from",start,"to",end,"is:", sum)
    
    elif choice == 3:
        print("Exiting the programe. Goodbye!")
        break
    
    else:
        print("Your choice is invalid!!!")
        break
        
    print()