# syntax : [expression for item in iterable if condition]

my_sum = [x**2 for x in range(5)]
print(my_sum)

even_number =[ i for i in range(15) if i % 2 == 0]
print(even_number)



#Python primitive datatypes are:

"""1.
int (integer)

2.
float (floating-point number)

3.
str (string)

4.
bool (boolean - True/False)"""

num1 = 10        # int
num2 = 3.14      # float
val = "Hello"    # str
flag = True      # bool
num3 = (3 + 5j)  # complex

print(num1)
print(num1)
print(val)
print(flag)
print(num3)



#Python collection datatypes are:

"""
1.
str(String)

2.
list 

3.
tuple

4.
set 

5.
dict (dictionary)
"""

name = "Python"      # str
array = [4, 7, 1, 9]     # list
values = (3, 6, 9, 1, 4)    # tuple
fruits = {"apple", "banana", "cherry"}   # set
contacts = {"electrician": 458956, "plumber": 785623, "mechanic": 562378}  # dict 

