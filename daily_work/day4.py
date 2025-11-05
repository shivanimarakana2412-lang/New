# for loop : A for loop is used to iterate over a squence (such as a list , tuple , string , or range) and execute a block of code for each element in that sequence.

# Range : In range function we can create a range between two numbers.

# Range always starts from zero if we passing single digit in function and the given number is execlusive

for i in range(0 , 11):
    print(i)
    
for i in range (15):
    print(i * 2)
    
for i in range (1 , 10 , 3):
    print(i)
    
for i in range (1 , 20 , -1):
    print(i)

# Table

num = int(input("Enter a number to print table: "))

for i in range(1 , 11):
    print(num , "x" , i , "=" , num*i)    

# Even or odd

start = int(input("Enter the start: "))
end = int(input("Enter the end: "))

for i in range (start , end+1):
    if i % 2 == 0:
        print(i , "Even")
    else:
        print(i , "Odd")
        
        
        

# while loop : A while loop repeatedly executes a block of code as long as the specified condition is true

# Different between two loop --> in for loop we know itretion count --> In while loop we don't know

i = 1

while i <= 10:
    print(i)
    i+= 1   # increment must be used otherwise it's infinity
    

while True:
    print("Enter 0 to stop!")
    choice = int(input("Enter num between (0 - 10)"))
    if choice == 0:
     break

