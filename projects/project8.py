import numpy as np



print("Welcom to NumPy Analyzer!")
print("============================================")
while True:
    print("Choose an option: ")
    print("1. create a Numpy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit\n")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
            print("Select the type of array to create: ")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")
            
            ch = int(input("Enter your choice: "))
            if ch == 1 :
                elements = input("Enter elements for the 1D array separated by space: ").split()
                elements = [int(x) for x in elements]
                array_1d = np.array(elements)

                print("1D Array created successfully:")
                print(array_1d)
            
            elif ch == 2:
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                elements = input(f"Enter {rows * cols} elements for the array separated by space: ").split()
                elements = [int(x) for x in elements]
                array_2d = np.array(elements).reshape(rows, cols)
                print("Array created successfully:")
                print(array_2d)
            
            elif ch == 3:
                d1 = int(input("Enter the number of blocks (depth): "))
                d2 = int(input("Enter the number of rows: "))
                d3 = int(input("Enter the number of columns: "))

                total = d1 * d2 * d3 
                elements = input(f"Enter {total} elements separated by space: ").split()
                elements = [int(x) for x in elements]

                array_3d = np.array(elements).reshape(d1, d2, d3)

                print("3D Array created successfully:")
                print(array_3d)
    
            else:
                print("Invalid choice.")
          
            
    elif choice == 2: