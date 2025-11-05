#CRUD --> CREAT , READ , UPDATE , DELETE

#COLLECTION DATATYPE ---> List , Tuple , Set , Dict

# list --> []  ---> mutable , ordered
# tuple --> () ---> imutable , ordered
# set --> {}   ---> mutable , unordered 
# dict --> {}  ---> mutable , unordered --> key : value

# when we write empty{} that was a dict data type



# single line comment

string1 = "Hello" , "World"   
string2 = 'Python is fun.'

print(string1)
print(string2)


# multi line comment
'''
This is a multi-line comment.
'''

greeting = "Hello World"
print(greeting)


# f string

name = "shivi"
print(f"Hello {name}")


name = "shivi"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

for i in name:
    print(i)
    

# String slicing
# String[start : end : step]

l = input("Enter the number of list: ")

print(l[::2])  # step
print(l[1:4])  # start : end
print(l[::-1]) # reverse
print(l[-1])   # negative indexing
print(l[-3:-1])# negative indexing with slicing
print(l[::])   # full list
print(l[:])    # full list
print(l[2:])   # from index 2 to end
print(l[:3])   # from start to index 3 (excluding index 3)
print(l[1:5:2])# start : end : step


# len function

txt = "Hello World"
print(len(txt))

















