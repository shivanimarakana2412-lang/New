# file handiling allows us to read , write , and modify files in python 
# python provide buit in function like open() , close() , read() , and write() for file handling

# syntax ---> file = open("filename.txt" , "mode")

# modes : 1. "r" - read , 2. "w" - write , 3. "a" - append , 4. "x" - create




# read

file = open("demo.txt","r")

content = file.read()

print(content)

file.close()



with open("demo.txt", "r") as file:  # Open file in read mode using context manager

	content = file.read()  # Read entire file content
	
print(content)

# write

file = open ("demo.txt" , "w")

file.write("\n\n\tThis is python")

file.close()



# append

file = open("demo.txt" , "a")

file.write("\n\tMy name is Shivani marakana\n") # \t  --> it means space of one tab 

file.write ("\tMy father name is Rameshbhai Marakana and also my mother is Induben Marakana")

file.close()



#Readlines

file = open("demo.txt" , "r")

firstline = file.readline() # for 1 line readibality

firstlines = file.readlines() # for all lines readibality , it gives list for any lines

print(firstline)

print(firstlines)

for line in firstlines:
    print(line)

file.close()


# with statment automatic file close

with open("demo.txt") as file:
    content = file.readline()
    print(content)



           # filehandling operation



 
