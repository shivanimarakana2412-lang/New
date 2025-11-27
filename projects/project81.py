# 

# # # # import numpy as np



# # # # print("Welcom to NumPy Analyzer!")
# # # # print("============================================")
# # # # while True:
# # # #     print("Choose an option: ")
# # # #     print("1. create a Numpy Array")
# # # #     print("2. Perform Mathematical Operations")
# # # #     print("3. Combine or Split Arrays")
# # # #     print("4. Search, Sort, or Filter Arrays")
# # # #     print("5. Compute Aggregates and Statistics")
# # # #     print("6. Exit\n")
    
# # # #     choice = int(input("Enter your choice: "))
    
# # # #     if choice == 1:
# # # #             print("Select the type of array to create: ")
# # # #             print("1. 1D Array")
# # # #             print("2. 2D Array")
# # # #             print("3. 3D Array")
            
# # # #             ch = int(input("Enter your choice: "))
# # # #             if ch == 1 :
# # # #                 elements = input("Enter elements for the 1D array separated by space: ").split()
# # # #                 elements = [int(x) for x in elements]
# # # #                 array_1d = np.array(elements)

# # # #                 print("1D Array created successfully:")
# # # #                 print(array_1d)
            
# # # #             elif ch == 2:
# # # #                 rows = int(input("Enter the number of rows: "))
# # # #                 cols = int(input("Enter the number of columns: "))
# # # #                 elements = input(f"Enter {rows * cols} elements for the array separated by space: ").split()
# # # #                 elements = [int(x) for x in elements]
# # # #                 array_2d = np.array(elements).reshape(rows, cols)
# # # #                 print("Array created successfully:")
# # # #                 print(array_2d)
            
# # # #             elif ch == 3:
# # # #                 d1 = int(input("Enter the number of blocks (depth): "))
# # # #                 d2 = int(input("Enter the number of rows: "))
# # # #                 d3 = int(input("Enter the number of columns: "))

# # # #                 total = d1 * d2 * d3 
# # # #                 elements = input(f"Enter {total} elements separated by space: ").split()
# # # #                 elements = [int(x) for x in elements]

# # # #                 array_3d = np.array(elements).reshape(d1, d2, d3)

# # # #                 print("3D Array created successfully:")
# # # #                 print(array_3d)
    
# # # #             else:
# # # #                 print("Invalid choice.")
          
            
# # # #     elif choice == 2:












# # # import numpy as np

# # # """
# # # NumPy Analyzer Program
# # # ----------------------
# # # A simple interactive tool that lets users create NumPy arrays
# # # and perform various mathematical, statistical, and structural operations.
# # # """


# # # def create_array():
# # #     """
# # #     Create a NumPy array based on user input.

# # #     Options:
# # #     - 1D array
# # #     - 2D array
# # #     - 3D array

# # #     Returns:
# # #         numpy.ndarray: The created array.
# # #         None: If invalid choice is entered.
# # #     """
# # #     print("\nArray Creation:")
# # #     print("Select the type of array to create:")
# # #     print("1. 1D Array")
# # #     print("2. 2D Array")
# # #     print("3. 3D Array")

# # #     choice = int(input("Enter your choice: "))

# # #     if choice == 1:
# # #         n = int(input("Enter number of elements: "))
# # #         elements = list(map(int, input("Enter elements separated by space: ").split()))
# # #         arr = np.array(elements)
# # #         print("Array created successfully:\n", arr)

# # #     elif choice == 2:
# # #         rows = int(input("Enter number of rows: "))
# # #         cols = int(input("Enter number of columns: "))
# # #         elements = list(map(int, input(f"Enter {rows*cols} elements separated by space: ").split()))
# # #         arr = np.array(elements).reshape(rows, cols)
# # #         print("Array created successfully:\n", arr)

# # #     elif choice == 3:
# # #         x = int(input("Enter dimension 1: "))
# # #         y = int(input("Enter dimension 2: "))
# # #         z = int(input("Enter dimension 3: "))
# # #         elements = list(map(int, input(f"Enter {x*y*z} elements separated by space: ").split()))
# # #         arr = np.array(elements).reshape(x, y, z)
# # #         print("Array created successfully:\n", arr)

# # #     else:
# # #         print("Invalid choice.")
# # #         return None
    
# # #     return arr


# # # def mathematical_operations(arr):
# # #     """
# # #     Perform mathematical operations between the given array and another user-input array.



# # # def combine_or_split(arr):
# # #     """
# # #     Combine two arrays vertically or split an array into equal halves.

# # #     Args:
# # #     arr (numpy.ndarray): The original array.
# # #     """
# # #     print("\nChoose an option:")
# # #     print("1. Combine Arrays")
# # #     print("2. Split Array")

# # #     choice = int(input("Enter your choice: "))

# # #     if choice == 1:
# # #         elements = list(map(int, input(f"Enter {arr.size} elements for the second array: ").split()))
# # #         arr2 = np.array(elements).reshape(arr.shape)
# # #         combined = np.vstack([arr, arr2])
# # #         print("\nCombined Array (Vertical Stack):\n", combined)

# # #     elif choice == 2:
# # #         print("\nOriginal Array:\n", arr)
# # #         print("\nSplitting into two equal parts:")
# # #         try:
# # #             split_arrays = np.split(arr, 2)
# # #             for i, s in enumerate(split_arrays, 1):
# # #                 print(f"Part {i}:\n{s}")
# # #         except:
# # #             print("Array cannot be split equally.")

# # #     else:
# # #         print("Invalid choice.")


# # # def search_sort_filter(arr):
# # #     """
# # #     Perform search, sorting, or filtering operations on the array.

# # #     Supported features:
# # #     - Search for a value
# # #     - Sort the array
# # #     - Filter values above a threshold

# # #     Args:
# # #         arr (numpy.ndarray): The array to process.
# # #     """
# # #     print("\nSearch, Sort, and Filter:")
# # #     print("1. Search a value")
# # #     print("2. Sort the array")
# # #     print("3. Filter values")

# # #     choice = int(input("Enter your choice: "))

# # #     if choice == 1:
# # #         val = int(input("Enter value to search: "))
# # #         result = np.where(arr == val)
# # #         print("Found at positions:", result)

# # #     elif choice == 2:
# # #         print("Original Array:\n", arr)
# # #         print("\nSorted Array:\n", np.sort(arr))

# # #     elif choice == 3:
# # #         threshold = int(input("Enter minimum value: "))
# # #         print("Filtered values:", arr[arr > threshold])

# # #     else:
# # #         print("Invalid choice.")


# # # def aggregates(arr):
# # #     """
# # #     Compute aggregate/statistical measures of the array.

# # #     Supported metrics:
# # #     - Sum
# # #     - Mean
# # #     - Median
# # #     - Standard deviation
# # #     - Variance

# # # Args:
# # #     arr (numpy.ndarray): The input array.
# # #     """
# # #     print("\nChoose an aggregate/statistical operation:")
# # #     print("1. Sum")
# # #     print("2. Mean")
# # #     print("3. Median")
# # #     print("4. Standard Deviation")
# # #     print("5. Variance")

# # #     choice = int(input("Enter your choice: "))

# # #     if choice == 1:
# # #         print("Sum:", np.sum(arr))
# # #     elif choice == 2:
# # #         print("Mean:", np.mean(arr))
# # #     elif choice == 3:
# # #         print("Median:", np.median(arr))
# # #     elif choice == 4:
# # #         print("Standard Deviation:", np.std(arr))
# # #     elif choice == 5:
# # #         print("Variance:", np.var(arr))
# # #     else:
# # #         print("Invalid choice.")


# # # # ---------------- MAIN PROGRAM --------------------
# # # print("\nWelcome to the NumPy Analyzer!")
# # # print("===================================")

# # # arr = None

# # # while True:
# # #     print("\nChoose an option:")
# # #     print("1. Create a NumPy Array")
# # #     print("2. Perform Mathematical Operations")
# # #     print("3. Combine or Split Arrays")
# # #     print("4. Search, Sort, or Filter Arrays")
# # #     print("5. Compute Aggregates and Statistics")
# # #     print("6. Exit")

# # #     option = int(input("Enter your choice: "))

# # #     if option == 1:
# # #         arr = create_array()

# # #     elif option == 2:
# # #         if arr is None:
# # #             print("Create an array first.")
# # #         else:
# # #             mathematical_operations(arr)

# # #     elif option == 3:
# # #         if arr is None:
# # #             print("Create an array first.")
# # #         else:
# # #             combine_or_split(arr)

# # #     elif option == 4:
# # #         if arr is None:
# # #             print("Create an array first.")
# # #         else:
# # #             search_sort_filter(arr)

# # #     elif option == 5:
# # #         if arr is None:
# # #             print("Create an array first.")
# # #         else:
# # #             aggregates(arr)

# # #     elif option == 6:
# # #         print("Thank you for using the NumPy Analyzer! Goodbye!")
# # #         break

# # #     else:
# # #         print("Invalid option. Try again.")








# # # import numpy as np

# # # """
# # # Simple NumPy Analyzer Program
# # # """


# # # def create_array():
# # #     """Creates a NumPy array based on user input."""
# # #     print("\nArray Creation:")
# # #     print("Select the type of array to create:")
# # #     print("1. 1D Array")
# # #     print("2. 2D Array")
# # #     print("3. 3D Array")

# # #     choice = int(input("Enter your choice: "))

# # #     if choice == 1:
# # #         n = int(input("Enter number of elements: "))
# # #         elements = list(map(int, input("Enter elements separated by space: ").split()))
# # #         arr = np.array(elements)
# # #         print("Array created successfully:\n", arr)

# # #     elif choice == 2:
# # #         rows = int(input("Enter number of rows: "))
# # #         cols = int(input("Enter number of columns: "))
# # #         elements = list(map(int, input(f"Enter {rows*cols} elements separated by space: ").split()))
# # #         arr = np.array(elements).reshape(rows, cols)
# # #         print("Array created successfully:\n", arr)

# # #     elif choice == 3:
# # #         x = int(input("Enter dimension 1: "))
# # #         y = int(input("Enter dimension 2: "))
# # #         z = int(input("Enter dimension 3: "))
# # #         elements = list(map(int, input(f"Enter {x*y*z} elements separated by space: ").split()))
# # #         arr = np.array(elements).reshape(x, y, z)
# # #         print("Array created successfully:\n", arr)

# # #     else:
# # #         print("Invalid choice.")
# # #         return None
    
# # #     return arr


# # # def mathematical_operations(arr):
# # #     """Performs basic math operations on arrays."""
# # #     print("\nMathematical Operations:")
# # #     print("1. Addition")
# # #     print("2. Subtraction")
# # #     print("3. Multiplication")
# # #     print("4. Division")

# # #     choice = int(input("Enter your choice: "))
# # #     elements = list(map(int, input("Enter the same-size array elements separated by space: ").split()))
# # #     arr2 = np.array(elements).reshape(arr.shape)

# # #     print("\nOriginal Array:\n", arr)
# # #     print("\nSecond Array:\n", arr2)

# # #     if choice == 1:
# # #         print("\nResult of Addition:\n", arr + arr2)
# # #     elif choice == 2:
# # #         print("\nResult of Subtraction:\n", arr - arr2)
# # #     elif choice == 3:
# # #         print("\nResult of Multiplication:\n", arr * arr2)
# # #     elif choice == 4:
# # #         print("\nResult of Division:\n", arr / arr2)
# # #     else:
# # #         print("Invalid choice.")


# # # def combine_or_split(arr):
# # #     """Combines two arrays or splits one array."""
# # #     print("\nChoose an option:")
# # #     print("1. Combine Arrays")
# # #     print("2. Split Array")

# # #     choice = int(input("Enter your choice: "))

# # #     if choice == 1:
# # #         elements = list(map(int, input(f"Enter {arr.size} elements for the second array: ").split()))
# # #         arr2 = np.array(elements).reshape(arr.shape)
# # #         combined = np.vstack([arr, arr2])
# # #         print("\nCombined Array (Vertical Stack):\n", combined)

# # #     elif choice == 2:
# # #         print("\nOriginal Array:\n", arr)
# # #         print("\nSplitting into two equal parts:")
# # #         try:
# # #             split_arrays = np.split(arr, 2)
# # #             for i, s in enumerate(split_arrays, 1):
# # #                 print(f"Part {i}:\n{s}")
# # #         except:
# # #             print("Array cannot be split equally.")

# # #     else:
# # #         print("Invalid choice.")


# # # def search_sort_filter(arr):
# # #     """Searches, sorts, or filters the array."""
# # #     print("\nSearch, Sort, and Filter:")
# # #     print("1. Search a value")
# # #     print("2. Sort the array")
# # #     print("3. Filter values")

# # #     choice = int(input("Enter your choice: "))

# # #     if choice == 1:
# # #         val = int(input("Enter value to search: "))
# # #         result = np.where(arr == val)
# # #         print("Found at positions:", result)

# # #     elif choice == 2:
# # #         print("Original Array:\n", arr)
# # #         print("\nSorted Array:\n", np.sort(arr))

# # #     elif choice == 3:
# # #         threshold = int(input("Enter minimum value: "))
# # #         print("Filtered values:", arr[arr > threshold])

# # #     else:
# # #         print("Invalid choice.")


# # # def aggregates(arr):
# # #     """Calculates basic statistical values."""
# # #     print("\nChoose an aggregate/statistical operation:")
# # #     print("1. Sum")
# # #     print("2. Mean")
# # #     print("3. Median")
# # #     print("4. Standard Deviation")
# # #     print("5. Variance")

# # #     choice = int(input("Enter your choice: "))

# # #     if choice == 1:
# # #         print("Sum:", np.sum(arr))
# # #     elif choice == 2:
# # #         print("Mean:", np.mean(arr))
# # #     elif choice == 3:
# # #         print("Median:", np.median(arr))
# # #     elif choice == 4:
# # #         print("Standard Deviation:", np.std(arr))
# # #     elif choice == 5:
# # #         print("Variance:", np.var(arr))
# # #     else:
# # #         print("Invalid choice.")


# # # # ---------------- MAIN PROGRAM --------------------
# # # print("\nWelcome to the NumPy Analyzer!")
# # # print("===================================")

# # # arr = None

# # # while True:
# # #     print("\nChoose an option:")
# # #     print("1. Create a NumPy Array")
# # #     print("2. Perform Mathematical Operations")
# # #     print("3. Combine or Split Arrays")
# # #     print("4. Search, Sort, or Filter Arrays")
# # #     print("5. Compute Aggregates and Statistics")
# # #     print("6. Exit")

# # #     option = int(input("Enter your choice: "))

# # #     if option == 1:
# # #         arr = create_array()

# # #     elif option == 2:
# # #         if arr is None:
# # #             print("Create an array first.")
# # #         else:
# # #             mathematical_operations(arr)

# # #     elif option == 3:
# # #         if arr is None:
# # #             print("Create an array first.")
# # #         else:
# # #             combine_or_split(arr)

# # #     elif option == 4:
# # #         if arr is None:
# # #             print("Create an array first.")
# # #         else:
# # #             search_sort_filter(arr)

# # #     elif option == 5:
# # #         if arr is None:
# # #             print("Create an array first.")
# # #         else:
# # #             aggregates(arr)

# # #     elif option == 6:
# # #         print("Thank you for using the NumPy Analyzer! Goodbye!")
# # #         break

# # #     else:
# # #         print("Invalid option. Try again.")

















# # import numpy as np


# # class DataAnalytics:
# #     def __init__(self):
# #         self.array = None

# #     # ---------- Array Creation ----------
# #     def create_array(self):
# #         print("\nSelect the type of array to create:")
# #         print("1. 1D Array\n2. 2D Array\n3. 3D Array")
# #         choice = int(input("Enter your choice: "))

# #         if choice == 1:
# #             data = list(map(float, input("Enter elements separated by space: ").split()))
# #             self.array = np.array(data)

# #         elif choice == 2:
# #             rows = int(input("Enter number of rows: "))
# #             cols = int(input("Enter number of columns: "))
# #             values = list(map(float, input(f"Enter {rows * cols} elements separated by space: ").split()))
# #             self.array = np.array(values).reshape(rows, cols)

# #         elif choice == 3:
# #             x = int(input("Enter dimension x: "))
# #             y = int(input("Enter dimension y: "))
# #             z = int(input("Enter dimension z: "))
# #             values = list(map(float, input(f"Enter {x * y * z} elements separated by space: ").split()))
# #             self.array = np.array(values).reshape(x, y, z)

# #         print("\nArray created successfully:")
# #         print(self.array)

# #     # ---------- Indexing & Slicing ----------
# #     def indexing_slicing(self):
# #         if self.array is None:
# #             print("No array created yet!")
# #             return

# #         print("\nChoose an operation:")
# #         print("1. Indexing\n2. Slicing\n3. Go Back")
# #         choice = int(input("Enter your choice: "))

# #         if choice == 1:
# #             idx = tuple(map(int, input("Enter index (example: 1 2): ").split()))
# #             print("Indexed Value:", self.array[idx])

# #         elif choice == 2:
# #             r = input("Enter the row range (start:end) or leave blank for all: ")
# #             c = input("Enter the column range (start:end) or leave blank for all: ")

# #             r_slice = slice(*map(int, r.split(":"))) if r else slice(None)
# #             c_slice = slice(*map(int, c.split(":"))) if c else slice(None)

# #             print("\nSliced Array:")
# #             print(self.array[r_slice, c_slice])

# #     # ---------- Mathematical Operations ----------
# #     def math_operations(self):
# #         if self.array is None:
# #             print("No array created yet!")
# #             return

# #         print("\nChoose a mathematical operation:")
# #         print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
# #         op = int(input("Enter your choice: "))

# #         values = list(map(float, input("Enter new array elements separated by space: ").split()))
# #         second = np.array(values).reshape(self.array.shape)

# #         print("\nOriginal Array:\n", self.array)
# #         print("Second Array:\n", second)

# #         if op == 1:
# #             result = self.array + second
# #         elif op == 2:
# #             result = self.array - second
# #         elif op == 3:
# #             result = self.array * second
# #         elif op == 4:
# #             result = self.array / second
# #         else:
# #             print("Invalid choice!")
# #             return

# #         print("\nResult:\n", result)

# #     # ---------- Combine & Split ----------
# #     def combine_split(self):
# #         if self.array is None:
# #             print("No array created yet!")
# #             return

# #         print("\nChoose an option:")
# #         print("1. Combine Arrays\n2. Split Array")
# #         choice = int(input("Enter your choice: "))

# #         if choice == 1:
# #             values = list(map(float, input("Enter elements of another array separated by space: ").split()))
# #             arr = np.array(values).reshape(self.array.shape)
# #             result = np.vstack((self.array, arr))
# #             print("\nCombined Array (Vertical Stack):\n", result)

# #         elif choice == 2:
# #             parts = int(input("Enter number of parts to split into: "))
# #             result = np.array_split(self.array, parts)
# #             print("\nSplit Arrays:")
# #             for r in result:
# #                 print(r)

# #     # ---------- Search / Sort / Filter ----------
# #     def search_sort_filter(self):
# #         if self.array is None:
# #             print("No array created yet!")
# #             return

# #         print("\nChoose an option:")
# #         print("1. Search a value\n2. Sort the array\n3. Filter values")
# #         choice = int(input("Enter your choice: "))

# #         if choice == 1:
# #             value = float(input("Enter value to search: "))
# #             locations = np.where(self.array == value)
# #             print("Value found at indexes:", locations)

# #         elif choice == 2:
# #             result = np.sort(self.array, axis=-1)
# #             print("Sorted Array:\n", result)

# #         elif choice == 3:
# #             cond = float(input("Enter threshold to filter values greater than: "))
# #             result = self.array[self.array > cond]
# #             print("Filtered Values:", result)

# #     # ---------- Aggregating & Statistics ----------
# #     def statistics(self):
# #         if self.array is None:
# #             print("No array created yet!")
# #             return

# #         print("\nChoose an aggregate/statistical operation:")
# #         print("1. Sum\n2. Mean\n3. Median\n4. Standard Deviation\n5. Variance")
# #         choice = int(input("Enter your choice: "))

# #         if choice == 1:
# #             print("Sum:", np.sum(self.array))
# #         elif choice == 2:
# #             print("Mean:", np.mean(self.array))
# #         elif choice == 3:
# #             print("Median:", np.median(self.array))
# #         elif choice == 4:
# #             print("Standard Deviation:", np.std(self.array))
# #         elif choice == 5:
# #             print("Variance:", np.var(self.array))
# #         else:
# #             print("Invalid choice!")


# # # ---------------------- Main Program ----------------------
# # def menu():
# #     obj = DataAnalytics()

# #     while True:
# #         print("\nWelcome to the NumPy Analyzer!")
# #         print("=" * 40)
# #         print("1. Create a NumPy Array")
# #         print("2. Perform Mathematical Operations")
# #         print("3. Combine or Split Arrays")
# #         print("4. Search, Sort, or Filter Arrays")
# #         print("5. Compute Aggregates and Statistics")
# #         print("6. Exit")

# #         choice = int(input("Enter your choice: "))

# #         if choice == 1:
# #             obj.create_array()
# #         elif choice == 2:
# #             obj.math_operations()
# #         elif choice == 3:
# #             obj.combine_split()
# #         elif choice == 4:
# #             obj.search_sort_filter()
# #         elif choice == 5:
# #             obj.statistics()
# #         elif choice == 6:
# #             print("\nThank you for using the NumPy Analyzer! Goodbye!")
# #             break
# #         else:
# #             print("Invalid choice. Try again!")


# # if __name__ == "__main__":
# #     menu()



















# import numpy as np

# class DataAnalytics:
#     def __init__(self):
#         self.array = None

#     # ---------- Array Creation ----------
#     def create_array(self):
#         while True:
#             print("\nSelect the type of array to create:")
#             print("1. 1D Array\n2. 2D Array\n3. 3D Array\n4. Go Back")
#             choice = int(input("Enter your choice: "))

#             if choice == 1:
#                 data = list(map(float, input("Enter elements separated by space: ").split()))
#                 self.array = np.array(data)

#             elif choice == 2:
#                 rows = int(input("Enter number of rows: "))
#                 cols = int(input("Enter number of columns: "))
#                 values = list(map(float, input(f"Enter {rows * cols} elements separated by space: ").split()))
#                 self.array = np.array(values).reshape(rows, cols)

#             elif choice == 3:
#                 x = int(input("Enter dimension x: "))
#                 y = int(input("Enter dimension y: "))
#                 z = int(input("Enter dimension z: "))
#                 values = list(map(float, input(f"Enter {x * y * z} elements separated by space: ").split()))
#                 self.array = np.array(values).reshape(x, y, z)



#             else:
#                 print("Invalid choice!")
#                 continue

#             print("\nArray created successfully:")
#             print(self.array)

#     # ---------- Mathematical Operations ----------
#     def math_operations(self):
#         if self.array is None:
#             print("No array created yet!")
#             return

#         while True:
#             print("\nChoose a mathematical operation:")
#             print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Go Back")
#             op = int(input("Enter your choice: "))

#             if op == 5:
#                 return

#             values = list(map(float, input("Enter new array elements separated by space: ").split()))
#             second = np.array(values).reshape(self.array.shape)

#             if op == 1:
#                 result = self.array + second
#             elif op == 2:
#                 result = self.array - second
#             elif op == 3:
#                 result = self.array * second
#             elif op == 4:
#                 result = self.array / second
#             else:
#                 print("Invalid choice!")
#                 continue

#             print("\nResult:\n", result)

#     # ---------- Combine & Split ----------
#     def combine_split(self):
#         if self.array is None:
#             print("No array created yet!")
#             return

#         while True:
#             print("\nChoose an option:")
#             print("1. Combine Arrays\n2. Split Array\n3. Go Back")
#             choice = int(input("Enter your choice: "))

#             if choice == 1:
#                 values = list(map(float, input("Enter elements of another array separated by space: ").split()))
#                 arr = np.array(values).reshape(self.array.shape)
#                 result = np.vstack((self.array, arr))
#                 print("\nCombined Array (Vertical Stack):\n", result)

#             elif choice == 2:
#                 parts = int(input("Enter number of parts to split into: "))
#                 result = np.array_split(self.array, parts)
#                 print("\nSplit Arrays:")
#                 for r in result:
#                     print(r)

#             elif choice == 3:
#                 return
#             else:
#                 print("Invalid choice!")

#     # ---------- Search / Sort / Filter ----------
#     def search_sort_filter(self):
#         if self.array is None:
#             print("No array created yet!")
#             return

#         while True:
#             print("\nChoose an option:")
#             print("1. Search a value\n2. Sort the array\n3. Filter values\n4. Go Back")
#             choice = int(input("Enter your choice: "))

#             if choice == 1:
#                 value = float(input("Enter value to search: "))
#                 locations = np.where(self.array == value)
#                 print("Value found at indexes:", locations)

#             elif choice == 2:
#                 result = np.sort(self.array, axis=-1)
#                 print("Sorted Array:\n", result)

#             elif choice == 3:
#                 cond = float(input("Enter threshold to filter values greater than: "))
#                 result = self.array[self.array > cond]
#                 print("Filtered Values:", result)

#             elif choice == 4:
#                 return
#             else:
#                 print("Invalid choice!")

#     # ---------- Aggregating & Statistics ----------
#     def statistics(self):
#         if self.array is None:
#             print("No array created yet!")
#             return

#         while True:
#             print("\nChoose an aggregate/statistical operation:")
#             print("1. Sum\n2. Mean\n3. Median\n4. Standard Deviation\n5. Variance\n6. Go Back")
#             choice = int(input("Enter your choice: "))

#             if choice == 1:
#                 print("Sum:", np.sum(self.array))
#             elif choice == 2:
#                 print("Mean:", np.mean(self.array))
#             elif choice == 3:
#                 print("Median:", np.median(self.array))
#             elif choice == 4:
#                 print("Standard Deviation:", np.std(self.array))
#             elif choice == 5:
#                 print("Variance:", np.var(self.array))
#             elif choice == 6:
#                 return
#             else:
#                 print("Invalid choice!")


# # ---------------------- Main Program ----------------------
# def menu():
#     obj = DataAnalytics()

#     while True:
#         print("\nWelcome to the NumPy Analyzer!")
#         print("=" * 40)
#         print("1. Create a NumPy Array")
#         print("2. Perform Mathematical Operations")
#         print("3. Combine or Split Arrays")
#         print("4. Search, Sort, or Filter Arrays")
#         print("5. Compute Aggregates and Statistics")
#         print("6. Exit")

#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             obj.create_array()
#         elif choice == 2:
#             obj.math_operations()
#         elif choice == 3:
#             obj.combine_split()
#         elif choice == 4:
#             obj.search_sort_filter()
#         elif choice == 5:
#             obj.statistics()
#         elif choice == 6:
#             print("\nThank you for using the NumPy Analyzer! Goodbye!")
#             break
#         else:
#             print("Invalid choice. Try again!")


# if __name__ == "__main__":
#     menu()













# import numpy as np

# class DataAnalytics:
#     def __init__(self):
#         self.array = None

#     # ---------- Array Creation ----------
#     def create_array(self):
#         print("\nSelect the type of array to create:")
#         print("1. 1D Array\n2. 2D Array\n3. 3D Array")
#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             data = list(map(float, input("Enter elements separated by space: ").split()))
#             self.array = np.array(data)

#         elif choice == 2:
#             rows = int(input("Enter number of rows: "))
#             cols = int(input("Enter number of columns: "))
#             values = list(map(float, input(f"Enter {rows * cols} elements separated by space: ").split()))
#             self.array = np.array(values).reshape(rows, cols)

#         elif choice == 3:
#             x = int(input("Enter dimension x: "))
#             y = int(input("Enter dimension y: "))
#             z = int(input("Enter dimension z: "))
#             values = list(map(float, input(f"Enter {x * y * z} elements separated by space: ").split()))
#             self.array = np.array(values).reshape(x, y, z)

#         print("\nArray created successfully:")
#         print(self.array)

#     # ---------- Mathematical Operations ----------
#     def math_operations(self):
#         while True:
#             if self.array is None:
#                 print("No array created yet!")
#                 return

#             print("\nChoose a mathematical operation:")
#             print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Go Back")
#             op = int(input("Enter your choice: "))

#             if op == 5:
#                 return

#             values = list(map(float, input("Enter new array elements separated by space: ").split()))
#             second = np.array(values).reshape(self.array.shape)

#             if op == 1:
#                 result = self.array + second
#             elif op == 2:
#                 result = self.array - second
#             elif op == 3:
#                 result = self.array * second
#             elif op == 4:
#                 result = self.array / second
#             else:
#                 print("Invalid choice!")
#                 continue

#             print("\nResult:\n", result)

#     # ---------- Combine & Split ----------
#     def combine_split(self):
#         while True:
#             if self.array is None:
#                 print("No array created yet!")
#                 return

#             print("\nChoose an option:")
#             print("1. Combine Arrays\n2. Split Array\n3. Go Back")
#             choice = int(input("Enter your choice: "))

#             if choice == 1:
#                 values = list(map(float, input("Enter elements of another array separated by space: ").split()))
#                 arr = np.array(values).reshape(self.array.shape)
#                 result = np.vstack((self.array, arr))
#                 print("\nCombined Array:\n", result)

#             elif choice == 2:
#                 parts = int(input("Enter number of parts to split into: "))
#                 result = np.array_split(self.array, parts)
#                 print("\nSplit Arrays:")
#                 for r in result:
#                     print(r)

#             elif choice == 3:
#                 return
#             else:
#                 print("Invalid choice!")

#     # ---------- Search / Sort / Filter ----------
#     def search_sort_filter(self):
#         while True:
#             if self.array is None:
#                 print("No array created yet!")
#                 return

#             print("\nChoose an option:")
#             print("1. Search a value\n2. Sort the array\n3. Filter values\n4. Go Back")
#             choice = int(input("Enter your choice: "))

#             if choice == 1:
#                 value = float(input("Enter value to search: "))
#                 locations = np.where(self.array == value)
#                 print("Value found at:", locations)

#             elif choice == 2:
#                 result = np.sort(self.array, axis=-1)
#                 print("Sorted Array:\n", result)

#             elif choice == 3:
#                 cond = float(input("Enter threshold to filter values greater than: "))
#                 result = self.array[self.array > cond]
#                 print("Filtered Values:", result)

#             elif choice == 4:
#                 return
#             else:
#                 print("Invalid choice!")

#     # ---------- Aggregating & Statistics ----------
#     def statistics(self):
#         while True:
#             if self.array is None:
#                 print("No array created yet!")
#                 return

#             print("\nChoose a statistical operation:")
#             print("1. Sum\n2. Mean\n3. Median\n4. Standard Deviation\n5. Variance\n6. Go Back")
#             choice = int(input("Enter your choice: "))

#             if choice == 1:
#                 print("Sum:", np.sum(self.array))
#             elif choice == 2:
#                 print("Mean:", np.mean(self.array))
#             elif choice == 3:
#                 print("Median:", np.median(self.array))
#             elif choice == 4:
#                 print("Standard Deviation:", np.std(self.array))
#             elif choice == 5:
#                 print("Variance:", np.var(self.array))
#             elif choice == 6:
#                 return
#             else:
#                 print("Invalid choice!")


# # ---------------------- Main Menu ----------------------
# def menu():
#     obj = DataAnalytics()

#     while True:
#         print("\nWelcome to the NumPy Analyzer")
#         print("=" * 40)
#         print("1. Create a NumPy Array")
#         print("2. Perform Mathematical Operations")
#         print("3. Combine or Split Arrays")
#         print("4. Search, Sort, or Filter Arrays")
#         print("5. Compute Aggregates and Statistics")
#         print("6. Exit")

#         choice = int(input("Enter your choice: "))

#         if choice == 1:
#             obj.create_array()
#         elif choice == 2:
#             obj.math_operations()
#         elif choice == 3:
#             obj.combine_split()
#         elif choice == 4:
#             obj.search_sort_filter()
#         elif choice == 5:
#             obj.statistics()
#         elif choice == 6:
#             print("\nThank you for using the NumPy Analyzer! Goodbye!")
#             break
#         else:
#             print("Invalid choice!")

# if __name__ == "__main__":
#     menu()




