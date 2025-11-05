# #nested if / else

a = int(input("Enter a num:"))

if a >10:
    if a % 2 == 0:
        print("A is graterthan 10 and an even number")
    else:
        print("A is grater than 10 and an odd number")
else:
    print("A is less than 10 and an odd number")
    

# Max number

a = int(input("Enter num one:"))

b = int(input("Enter num two:"))

c = int(input("Enter num three:"))

if a > b:
    if a > c:
        print("A")
    else:
        print("C")
else:
    if b > c:
        print("B")
    else:
        print("c")
        

# Left hand / Ternery statment

num = 44

result = "Even" if num * 2 == 0 else "Odd"

print(result)


# Match cases --> replacemant of leader statment 

day = 1

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Invalid!")    
        
