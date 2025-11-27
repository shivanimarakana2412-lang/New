# import numpy as np

# def create_array():
#     print("\nArray Creation:")
#     print("Select the type of array to create:")
#     print("1. 1D Array")
#     print("2. 2D Array")
#     print("3. 3D Array")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         n = int(input("Enter number of elements: "))
#         elements = list(map(int, input("Enter elements separated by space: ").split()))
#         arr = np.array(elements)
#         print("Array created successfully:\n", arr)

#     elif choice == 2:
#         rows = int(input("Enter number of rows: "))
#         cols = int(input("Enter number of columns: "))
#         elements = list(map(int, input(f"Enter {rows*cols} elements separated by space: ").split()))
#         arr = np.array(elements).reshape(rows, cols)
#         print("Array created successfully:\n", arr)

#     elif choice == 3:
#         x = int(input("Enter dimension 1: "))
#         y = int(input("Enter dimension 2: "))
#         z = int(input("Enter dimension 3: "))
#         elements = list(map(int, input(f"Enter {x*y*z} elements separated by space: ").split()))
#         arr = np.array(elements).reshape(x, y, z)
#         print("Array created successfully:\n", arr)

#     else:
#         print("Invalid choice.")
#         return None
    
#     return arr


# def mathematical_operations(arr):
#     print("\nMathematical Operations:")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")

#     choice = int(input("Enter your choice: "))
#     elements = list(map(int, input("Enter the same-size array elements separated by space: ").split()))
#     arr2 = np.array(elements).reshape(arr.shape)

#     print("\nOriginal Array:\n", arr)
#     print("\nSecond Array:\n", arr2)

#     if choice == 1:
#         print("\nResult of Addition:\n", arr + arr2)
#     elif choice == 2:
#         print("\nResult of Subtraction:\n", arr - arr2)
#     elif choice == 3:
#         print("\nResult of Multiplication:\n", arr * arr2)
#     elif choice == 4:
#         print("\nResult of Division:\n", arr / arr2)
#     else:
#         print("Invalid choice.")


# def combine_or_split(arr):
#     print("\nChoose an option:")
#     print("1. Combine Arrays")
#     print("2. Split Array")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         elements = list(map(int, input(f"Enter {arr.size} elements for the second array: ").split()))
#         arr2 = np.array(elements).reshape(arr.shape)
#         combined = np.vstack([arr, arr2])
#         print("\nCombined Array (Vertical Stack):\n", combined)

#     elif choice == 2:
#         print("\nOriginal Array:\n", arr)
#         print("\nSplitting into two equal parts:")
#         try:
#             split_arrays = np.split(arr, 2)
#             for i, s in enumerate(split_arrays, 1):
#                 print(f"Part {i}:\n{s}")
#         except:
#             print("Array cannot be split equally.")

#     else:
#         print("Invalid choice.")


# def search_sort_filter(arr):
#     print("\nSearch, Sort, and Filter:")
#     print("1. Search a value")
#     print("2. Sort the array")
#     print("3. Filter values")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         val = int(input("Enter value to search: "))
#         result = np.where(arr == val)
#         print("Found at positions:", result)

#     elif choice == 2:
#         print("Original Array:\n", arr)
#         print("\nSorted Array:\n", np.sort(arr))

#     elif choice == 3:
#         threshold = int(input("Enter minimum value: "))
#         print("Filtered values:", arr[arr > threshold])

#     else:
#         print("Invalid choice.")


# def aggregates(arr):
#     print("\nChoose an aggregate/statistical operation:")
#     print("1. Sum")
#     print("2. Mean")
#     print("3. Median")
#     print("4. Standard Deviation")
#     print("5. Variance")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         print("Sum:", np.sum(arr))
#     elif choice == 2:
#         print("Mean:", np.mean(arr))
#     elif choice == 3:
#         print("Median:", np.median(arr))
#     elif choice == 4:
#         print("Standard Deviation:", np.std(arr))
#     elif choice == 5:
#         print("Variance:", np.var(arr))
#     else:
#         print("Invalid choice.")


# # ---------------- MAIN PROGRAM --------------------
# print("\nWelcome to the NumPy Analyzer!")
# print("===================================")

# arr = None

# while True:
#     print("\nChoose an option:")
#     print("1. Create a NumPy Array")
#     print("2. Perform Mathematical Operations")
#     print("3. Combine or Split Arrays")
#     print("4. Search, Sort, or Filter Arrays")
#     print("5. Compute Aggregates and Statistics")
#     print("6. Exit")

#     option = int(input("Enter your choice: "))

#     if option == 1:
#         arr = create_array()

#     elif option == 2:
#         if arr is None:
#             print("Create an array first.")
#         else:
#             mathematical_operations(arr)

#     elif option == 3:
#         if arr is None:
#             print("Create an array first.")
#         else:
#             combine_or_split(arr)

#     elif option == 4:
#         if arr is None:
#             print("Create an array first.")
#         else:
#             search_sort_filter(arr)

#     elif option == 5:
#         if arr is None:
#             print("Create an array first.")
#         else:
#             aggregates(arr)

#     elif option == 6:
#         print("Thank you for using the NumPy Analyzer! Goodbye!")
#         break

#     else:
#         print("Invalid option. Try again.")