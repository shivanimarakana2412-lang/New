l = []

def crli():
    num = int(input("Enter how many elements you want to add: "))
    
    for i in range(num):
        el = int(input(f"Enter the num f{i + 1}: "))
        l.append(el)
    return l
    
def sumLi(l):
    return sum(l)

def fMax(l):
    return max(l)

def fMin(l):
    return min(l)

def fAvg(l):
    return sum(l) / len(l)

def fact(num):
    if num <= 1:
        return 1
    return num * fact(num-1)


while True:
    print("\nEnter 1 to create a list")
    print("Enter 2 to sum the list")
    print("Enter 3 to find max in the list")
    print("Enter 4 to find min in the list")
    print("Enter 5 to find average of the list")
    print("Enter 6 to find fact of a number")
    print("Enter 7 to exit \n")

    choice = int(input("Enter your choice: "))
        
    if choice == 1:
        l = crli()    
        print("List created:" , l)
    
    elif choice == 2:
        print("sum of the list:" , sumLi(l))
        
    elif choice == 3:
        print("Maximum element:" ,fMax(l))
            
    elif choice == 4 :
        print("Minimum element:" , fMin(l))
            
    elif choice == 5:
        print("Average of list:", fAvg(l))
            
    elif choice == 6:
        num = int(input("Enter a number to find factorial: "))
        result = fact(num)
        print(f"Factorial of {num} is {result}")

    elif choice == 7:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice, try again.")



