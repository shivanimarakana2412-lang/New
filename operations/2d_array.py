
# 2d array means matrix

matrix = [        
    [1, 2, 3],    
    [4, 5, 6],  
    [7, 8, 9],
]
                      
print(matrix)  

print(matrix[1][1]) # first 1 is raw's index and second 1 is for colum's index and output : 5
print(matrix[-1][1])


# CRUD in 2d array it means matrix

#Creat
matrix.append([10, 11, 12])  
print(matrix) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]


#Read
for row in matrix:
    print(row)  # Prints each row
   
    
#Delete
del matrix[1][2]  # Removes element at row 1, column 2
print(matrix) # Output: [[1, 2, 3], [4, 5], [7, 8, 9], [10, 11, 12]]

matrix.pop(1)  # Removes row at index 1
print(matrix)  # Output: [[1, 2, 3], [7, 8, 9], [10, 11, 12]]



for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
    
    
for col in range(len(matrix[0])):  
    for row in matrix:
        print(row[col], end=" ")
    print()
    

# sorting

matrix.sort(key=lambda x: x[0])
print(matrix)




# 3D array

thirdy_array =  [        
   [ [1, 2, 3],    
    [4, 5, 6],  
    [7, 8, 9]
   ]
[       
    [11, 12, 13],    
    [14, 15, 16],  
    [17, 18, 19],
]
]

print(matrix)
print(matrix[1][2])



   