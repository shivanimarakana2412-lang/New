# An exeption is an error that occurs during the executing of program , disrupting the normal flow.

"thpes of error"

#1. zerodivision error
#2. index error
#3. name error 
#4. type error
#5. value error
#6. key error
#7. filenot found error

"TRY AND EXCEPT"

# try:
#     print(5/2) # jo divide thay to ans otherwise not divide
# except ZeroDivisionError:
#     print("Not divide")
    
    
    
# try:
#     print(5/0)
# except Exception: # when we didn't know the type of error
#     print("Not divide")
   
    
# "TRY EXCEPT ELSE"
 
 
# try:
#     print(5/2)
# except Exception: # when we didn't know the type of error
#     print("Not divide")
# else:
#     ("No error")    


# "TRY EXCEPT ELSE"

 
# try:
#     print(5/2)
# except Exception: # when we didn't know the type of error
#     print("Not divide")
# else:
#     ("No error")  
# finally:
#     print("All run")
   
   
    
""" 
✔ try-except → Catches errors

✔ try-except-else → Runs else if no error

✔ try-except-finally → Runs finally no matter what

✔ try-except-else-finally → Combines all
"""



#1️⃣ raise Keyword
#👉 raise is used to manually trigger exceptions in Python.

#👉 It is useful for custom error messages and validations.
    
#raise ExceptionType("Custom error message")


# a = 19
# if a < 18:
#     raise Exception("Age is not valid for voting")
# else:
#     print("You can vote")
    
    
class custom (Exception):
    pass

a = 17
if a < 2:
    raise custom("This is custom error")
    