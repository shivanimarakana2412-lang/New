print("Welcome to the Interactive Personal Data  Collector!")

print()

name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
number = int(input("Please enter your favourite number: "))

print()

print("Thank you! Here is the information we collected:")

print()

print("Name:",name,("Type:",type(name),"Memory Address:",id(name)))
print("Age:",age,("Type:",type(age),"Memory Address:",id(age)))
print("Height:",height,("Type:",type(height),"Memory Address:",id(height)))
print("Favourite Number:",number,("Type:",type(number),"Memory Address:",id(number)))

print()

print("Your birth year is approximately:",2025 - age,"(based on age of)",age)

print()

print("Thank you for using the Personal Data Collector. Goodbye!")