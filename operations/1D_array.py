
# 1D array means vactor 

arr = [10, 20, 30, 40, 50, 60, 70]

print(arr[1:4])   # Elements from index 1 to 3 
print(arr[:3])    # First 3 elements
print(arr[2:])    # From index 2 to end 
print(arr[::2])   # Every second element , it means gap of index
print(arr[::-1])  # Reverse the array


#CRUD operation

#creat
arr = []  # Empty list
arr.append(10)  # Add element
arr.append(20)
arr.append(30)
print(arr)  # Output: [10, 20, 30]

#update
arr.insert(1, 15)  # Insert 15 at index 1
print(arr)  # Output: [10, 15, 20, 30]
arr[1] = 25  # Change value at index 1
print(arr)

arr.extend([40, 50])  # Add multiple elements
print(arr)

#read
print(arr[2])  # Access element at index 2 → Output: 20
print(arr[0:3])  # Access elements from index 0 to index 2 → Output: [10, 15, 20]

#delete
arr.pop(2)  # Removes element at index 2
print(arr)  # Output: [10, 25, 30, 40, 50]

arr.remove(40)  # Removes first occurrence of 40
print(arr)  # Output: [10, 25, 30, 50]

del arr[1]  # Delete element at index 1
print(arr)  # Output: [10, 30, 50]

arr.clear()  # Removes all elements
print(arr)



# loop in 1D
arr = [10, 20, 30, 40, 50, 60, 70]
for elem in arr:
  print(elem)
  
  

#sorting

arr = [50, 10, 40, 30, 20]

arr.sort()  # Sort in ascending order
print(arr)

arr.sort(reverse=True) # Sort in decending order
print(arr)


arr = [50, 10, 40, 30, 20]

new_arr = sorted(arr)  # Ascending order
print(new_arr)  # Output: [10, 20, 30, 40, 50]
print(arr) 

desc_arr = sorted(arr, reverse=True)
print(desc_arr)  # Output: [50, 40, 30, 20, 10]    



arr = [53, 27, 81, 42, 19]

arr.sort(key=lambda x: x % 10)  # Sort by last digit
print(arr)  # Output: [81, 42, 53, 19, 27]



#sortin string

names = ["Zara", "Alice", "John", "Bob"]

names.sort()
print(names)  # Output: ['Alice', 'Bob', 'John', 'Zara']

names.sort(reverse=True)
print(names)



# Sorting a List of Tuples

students = [("Alice", 90), ("Bob", 75), ("Charlie", 85)]

students.sort(key=lambda x: x[0])  # Sort by names (1st element) # output: [("Alice", 90), ("Bob", 75), ("Charlie", 85)]
students.sort(key=lambda x: x[1])  # Sort by marks (2nd element) # Output: [('Bob', 75), ('Charlie', 85), ('Alice', 90)]
print(students)  




