# import numpy as np


# # while True:
# # print("Select the type of array to create:")
# # print("1. 1D Array")
# # print("2. 2D Array")
# # print("3. 3D Array")

# # choice = int(input("Enter your choice: "))
# # if choice == 1:
# # # choice 1
# #     elements = input("Enter elements for the 1D array separated by space: ").split()
# #     elements = [int(x) for x in elements]
# #     array_1d = np.array(elements)

# #     print("1D Array created successfully:")
# #     print(array_1d)

# # elif choice == 2:
# #     rows = int(input("Enter the number of rows: "))
# #     cols = int(input("Enter the number of columns: "))
# #     elements = input(f"Enter {rows * cols} elements for the array separated by space: ").split()
# #     elements = [int(x) for x in elements]
# #     array_2d = np.array(elements).reshape(rows, cols)
# #     print("Array created successfully:")
# #     print(array_2d)

# # elif choice == 3:
# #     d1 = int(input("Enter the number of blocks (depth): "))
# #     d2 = int(input("Enter the number of rows: "))
# #     d3 = int(input("Enter the number of columns: "))

# #     total = d1 * d2 * d3 
# #     elements = input(f"Enter {total} elements separated by space: ").split()
# #     elements = [int(x) for x in elements]

# #     array_3d = np.array(elements).reshape(d1, d2, d3)

# #     print("3D Array created successfully:")
# #     print(array_3d)
    
# # else:
# #     break



import numpy as np

def create_array():
    print("\nArray Creation:")
    print("Select the type of array to create:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        elements = list(map(float, input("Enter elements separated by space: ").split()))
        arr = np.array(elements)
    
    elif choice == 2:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        elements = list(map(float, input(f"Enter {rows*cols} elements: ").split()))
        arr = np.array(elements).reshape(rows, cols)

    elif choice == 3:
        d1 = int(input("Enter dimension 1: "))
        d2 = int(input("Enter dimension 2: "))
        d3 = int(input("Enter dimension 3: "))
        elements = list(map(float, input(f"Enter {d1*d2*d3} elements: ").split()))
        arr = np.array(elements).reshape(d1, d2, d3)

    else:
        print("Invalid choice!")
        return None

    print("\nArray created successfully:")
    print(arr)
    return arr


def mathematical_operations(arr):
    print("\nMathematical Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))

    elements = list(map(float, input("Enter same-size array elements separated by space: ").split()))
    arr2 = np.array(elements).reshape(arr.shape)

    if choice == 1:
        result = arr + arr2
    elif choice == 2:
        result = arr - arr2
    elif choice == 3:
        result = arr * arr2
    elif choice == 4:
        result = arr / arr2
    else:
        print("Invalid choice!")
        return

    print("\nResult:")
    print(result)


def combine_or_split(arr):
    print("\n1. Combine Arrays")
    print("2. Split Array")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        elements = list(map(float, input("Enter elements of another array: ").split()))
        arr2 = np.array(elements).reshape(arr.shape)
        combined = np.vstack((arr, arr2))
        print("\nCombined Array:")
        print(combined)

    elif choice == 2:
        print("\n1. Split horizontally")
        print("2. Split vertically")
        s = int(input("Choose split option: "))
        if s == 1: 
            print(np.hsplit(arr, 2))
        elif s == 2:
            print(np.vsplit(arr, 2))
        else:
            print("Invalid split option!")

    else:
        print("Invalid choice!")


def search_sort_filter(arr):
    print("\nSearch, Sort, Filter:")
    print("1. Search a value")
    print("2. Sort the array")
    print("3. Filter values > threshold")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = float(input("Enter value to search: "))
        result = np.where(arr == val)
        print("\nFound at indices:", result)

    elif choice == 2:
        print("\nOriginal Array:")
        print(arr)
        print("\nSorted Array:")
        print(np.sort(arr))

    elif choice == 3:
        t = float(input("Enter threshold: "))
        print("\nFiltered Values:")
        print(arr[arr > t])

    else:
        print("Invalid choice!")


def aggregate_statistics(arr):
    print("\nAggregates and Statistics:")
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
        print("Invalid choice!")


# ================== MAIN PROGRAM ==================

def main():
    current_array = None

    print("Welcome to the NumPy Analyzer!")
    while True:
        print("\nChoose an option:")
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            current_array = create_array()

        elif choice == 2:
            if current_array is not None:
                mathematical_operations(current_array)
            else:
                print("Create an array first!")

        elif choice == 3:
            if current_array is not None:
                combine_or_split(current_array)
            else:
                print("Create an array first!")

        elif choice == 4:
            if current_array is not None:
                search_sort_filter(current_array)
            else:
                print("Create an array first!")

        elif choice == 5:
            if current_array is not None:
                aggregate_statistics(current_array)
            else:
                print("Create an array first!")

        elif choice == 6:
            print("Thank you for using NumPy Analyzer! Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
