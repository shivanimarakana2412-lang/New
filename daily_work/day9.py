# list of dict

students = [
    {"name" : "Shivani" , "age" : 17},
    {"name" : "Vishva" , "age" : 17},
    {"name" : "Khushi" , "age" : 17},
    {"name" : "Mahek" , "age" : 17},   
]
print(students[0]["name"])
print(students[1]["name"])
print(students[2]["name"])
print(students[3]["name"])

for st in students:
    print(st["name"] , "---" , st["age"])
    
    
# CRUD operations 