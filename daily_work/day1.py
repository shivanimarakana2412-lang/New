# 2 type of function --> 1.output   2.Input

# 1.output

print(12)
print("shivi")
print(20.58)
print(True)
print(False)
           
# # 2. Input

input("Enter your name :")

# #variable --> 

a = 46
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)

name = input("Enter your name: ")
lastName = input("Enter your lastName: ")

print("The student full name is",name, lastName)
print("The student full name is",name+" "+lastName)

# Datatypes  --> 1.Primitive   2. Collection

# 1. Primitive --> 1.String   2.Float   3.Boolean   4.Integer

#  1.String   --> text
#  2.Float    --> number with points
#  3.Boolean  --> True , False
#  4.Integer  --> number


# type

num = 34
text = "shivi"
point = 34.9
choice = False
num3 = None

print(type(num))
print(type(text))
print(type(point))
print(type(choice))
print(type(num3))

# #type casting constructor

num = int(input("Enter the number :"))
num2 = int(input("Enter the number :"))

print(num + num2)


num = 34
text = "shivi"
point = 34.9
choice = False
blank = " "

                                    # Truthy value / Falsy value
                                    
# Integer    

print(int(num))      
# print(int(text))  
print(int(point))  
print(int(choice))        
                     
# Float                     

print(float(num))      
#print(float(text))  
print(float(point))  
print(float(choice))

# string

print(str(num))      
print(str(text))  
print(str(point))  
print(str(choice))

# Boolean


print(bool(num))      
print(bool(text))  
print(bool(point))  
print(bool(choice))
print(bool(blank))