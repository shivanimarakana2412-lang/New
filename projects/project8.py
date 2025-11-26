# # import numpy as np



# # print("Welcom to NumPy Analyzer!")
# # print("============================================")
# # while True:
# #     print("Choose an option: ")
# #     print("1. create a Numpy Array")
# #     print("2. Perform Mathematical Operations")
# #     print("3. Combine or Split Arrays")
# #     print("4. Search, Sort, or Filter Arrays")
# #     print("5. Compute Aggregates and Statistics")
# #     print("6. Exit\n")
    
# #     choice = int(input("Enter your choice: "))
    
# #     if choice == 1:
# #             print("Select the type of array to create: ")
# #             print("1. 1D Array")
# #             print("2. 2D Array")
# #             print("3. 3D Array")
            
# #             ch = int(input("Enter your choice: "))
# #             if ch == 1 :
# #                 elements = input("Enter elements for the 1D array separated by space: ").split()
# #                 elements = [int(x) for x in elements]
# #                 array_1d = np.array(elements)

# #                 print("1D Array created successfully:")
# #                 print(array_1d)
            
# #             elif ch == 2:
# #                 rows = int(input("Enter the number of rows: "))
# #                 cols = int(input("Enter the number of columns: "))
# #                 elements = input(f"Enter {rows * cols} elements for the array separated by space: ").split()
# #                 elements = [int(x) for x in elements]
# #                 array_2d = np.array(elements).reshape(rows, cols)
# #                 print("Array created successfully:")
# #                 print(array_2d)
            
# #             elif ch == 3:
# #                 d1 = int(input("Enter the number of blocks (depth): "))
# #                 d2 = int(input("Enter the number of rows: "))
# #                 d3 = int(input("Enter the number of columns: "))

# #                 total = d1 * d2 * d3 
# #                 elements = input(f"Enter {total} elements separated by space: ").split()
# #                 elements = [int(x) for x in elements]

# #                 array_3d = np.array(elements).reshape(d1, d2, d3)

# #                 print("3D Array created successfully:")
# #                 print(array_3d)
    
# #             else:
# #                 print("Invalid choice.")
          
            
# #     elif choice == 2:












# import numpy as np

# """
# NumPy Analyzer Program
# ----------------------
# A simple interactive tool that lets users create NumPy arrays
# and perform various mathematical, statistical, and structural operations.
# """


# def create_array():
#     """
#     Create a NumPy array based on user input.

#     Options:
#     - 1D array
#     - 2D array
#     - 3D array

#     Returns:
#         numpy.ndarray: The created array.
#         None: If invalid choice is entered.
#     """
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
#     """
#     Perform mathematical operations between the given array and another user-input array.



# def combine_or_split(arr):
#     """
#     Combine two arrays vertically or split an array into equal halves.

#     Args:
#     arr (numpy.ndarray): The original array.
#     """
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
#     """
#     Perform search, sorting, or filtering operations on the array.

#     Supported features:
#     - Search for a value
#     - Sort the array
#     - Filter values above a threshold

#     Args:
#         arr (numpy.ndarray): The array to process.
#     """
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
#     """
#     Compute aggregate/statistical measures of the array.

#     Supported metrics:
#     - Sum
#     - Mean
#     - Median
#     - Standard deviation
#     - Variance

# Args:
#     arr (numpy.ndarray): The input array.
#     """
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








import numpy as np

"""
Simple NumPy Analyzer Program
"""


def create_array():
    """Creates a NumPy array based on user input."""
    print("\nArray Creation:")
    print("Select the type of array to create:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of elements: "))
        elements = list(map(int, input("Enter elements separated by space: ").split()))
        arr = np.array(elements)
        print("Array created successfully:\n", arr)

    elif choice == 2:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        elements = list(map(int, input(f"Enter {rows*cols} elements separated by space: ").split()))
        arr = np.array(elements).reshape(rows, cols)
        print("Array created successfully:\n", arr)

    elif choice == 3:
        x = int(input("Enter dimension 1: "))
        y = int(input("Enter dimension 2: "))
        z = int(input("Enter dimension 3: "))
        elements = list(map(int, input(f"Enter {x*y*z} elements separated by space: ").split()))
        arr = np.array(elements).reshape(x, y, z)
        print("Array created successfully:\n", arr)

    else:
        print("Invalid choice.")
        return None
    
    return arr


def mathematical_operations(arr):
    """Performs basic math operations on arrays."""
    print("\nMathematical Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))
    elements = list(map(int, input("Enter the same-size array elements separated by space: ").split()))
    arr2 = np.array(elements).reshape(arr.shape)

    print("\nOriginal Array:\n", arr)
    print("\nSecond Array:\n", arr2)

    if choice == 1:
        print("\nResult of Addition:\n", arr + arr2)
    elif choice == 2:
        print("\nResult of Subtraction:\n", arr - arr2)
    elif choice == 3:
        print("\nResult of Multiplication:\n", arr * arr2)
    elif choice == 4:
        print("\nResult of Division:\n", arr / arr2)
    else:
        print("Invalid choice.")


def combine_or_split(arr):
    """Combines two arrays or splits one array."""
    print("\nChoose an option:")
    print("1. Combine Arrays")
    print("2. Split Array")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        elements = list(map(int, input(f"Enter {arr.size} elements for the second array: ").split()))
        arr2 = np.array(elements).reshape(arr.shape)
        combined = np.vstack([arr, arr2])
        print("\nCombined Array (Vertical Stack):\n", combined)

    elif choice == 2:
        print("\nOriginal Array:\n", arr)
        print("\nSplitting into two equal parts:")
        try:
            split_arrays = np.split(arr, 2)
            for i, s in enumerate(split_arrays, 1):
                print(f"Part {i}:\n{s}")
        except:
            print("Array cannot be split equally.")

    else:
        print("Invalid choice.")


def search_sort_filter(arr):
    """Searches, sorts, or filters the array."""
    print("\nSearch, Sort, and Filter:")
    print("1. Search a value")
    print("2. Sort the array")
    print("3. Filter values")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value to search: "))
        result = np.where(arr == val)
        print("Found at positions:", result)

    elif choice == 2:
        print("Original Array:\n", arr)
        print("\nSorted Array:\n", np.sort(arr))

    elif choice == 3:
        threshold = int(input("Enter minimum value: "))
        print("Filtered values:", arr[arr > threshold])

    else:
        print("Invalid choice.")


def aggregates(arr):
    """Calculates basic statistical values."""
    print("\nChoose an aggregate/statistical operation:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Standard Deviation")
    print("5. Variance")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Sum:", np.sum(arr))
    elif choice == 2:
        print("Mean:", np.mean(arr))
    elif choice == 3:
        print("Median:", np.median(arr))
    elif choice == 4:
        print("Standard Deviation:", np.std(arr))
    elif choice == 5:
        print("Variance:", np.var(arr))
    else:
        print("Invalid choice.")


# ---------------- MAIN PROGRAM --------------------
print("\nWelcome to the NumPy Analyzer!")
print("===================================")

arr = None

while True:
    print("\nChoose an option:")
    print("1. Create a NumPy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        arr = create_array()

    elif option == 2:
        if arr is None:
            print("Create an array first.")
        else:
            mathematical_operations(arr)

    elif option == 3:
        if arr is None:
            print("Create an array first.")
        else:
            combine_or_split(arr)

    elif option == 4:
        if arr is None:
            print("Create an array first.")
        else:
            search_sort_filter(arr)

    elif option == 5:
        if arr is None:
            print("Create an array first.")
        else:
            aggregates(arr)

    elif option == 6:
        print("Thank you for using the NumPy Analyzer! Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
