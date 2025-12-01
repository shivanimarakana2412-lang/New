import numpy as np

class DataAnalytics:
    def __init__(self):
        self.array = None

    # ---------- Array Creation ----------
    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array\n2. 2D Array\n3. 3D Array")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = list(map(float, input("Enter elements separated by space: ").split()))
            self.array = np.array(data)

        elif choice == 2:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            values = list(map(float, input(f"Enter {rows * cols} elements separated by space: ").split()))
            self.array = np.array(values).reshape(rows, cols)

        elif choice == 3:
            x = int(input("Enter dimension x: "))
            y = int(input("Enter dimension y: "))
            z = int(input("Enter dimension z: "))
            values = list(map(float, input(f"Enter {x * y * z} elements separated by space: ").split()))
            self.array = np.array(values).reshape(x, y, z)

        print("\nArray created successfully:")
        print(self.array)

    def math_operations(self):
        while True:
            if self.array is None:
                print("No array created yet!")
                return

            print("\nChoose an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Indexing")
            print("6. Slicing")
            print("7. Go Back")

            op = int(input("Enter your choice: "))
            # --- Mathematical Operations ---
            values = list(map(float, input("Enter new array elements separated by space: ").split()))
            second = np.array(values).reshape(self.array.shape)

            if op == 1:
                result = self.array + second
            elif op == 2:
                result = self.array - second
            elif op == 3:
                result = self.array * second
            elif op == 4:
                result = self.array / second

            elif op == 5:
                idx = tuple(map(int, input("Enter index (e.g., 1 2 for 2D, 0 1 2 for 3D): ").split()))
                print("\nIndexed Value:", self.array[idx])
            
            elif op == 6:
                dims = self.array.ndim
                print(f"\nArray Dimensions: {dims}")
                print("Use slicing format: start:end (example: 0:3) or press Enter for full")
                
                slices = []
                for i in range(dims):
                    s = input(f"Dimension {i + 1} slice: ")
                    if s.strip() == "":
                        slices.append(slice(None))
                    else:
                        start, end = map(int, s.split(":"))
                        slices.append(slice(start, end))

                print("\nSliced Array:")
                print(self.array[tuple(slices)])
            
            elif op == 7:
                return
            
    # ---------- Combine & Split ----------
    def combine_split(self):
        while True:
            if self.array is None:
                print("No array created yet!")
                return

            print("\nChoose an option:")
            print("1. Combine Arrays\n2. Split Array\n3. Go Back")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                values = list(map(float, input("Enter elements of another array separated by space: ").split()))
                arr = np.array(values).reshape(self.array.shape)
                result = np.vstack((self.array, arr))
                print("\nCombined Array:\n", result)

            elif choice == 2:
                parts = int(input("Enter number of parts to split into: "))
                result = np.array_split(self.array, parts)
                print("\nSplit Arrays:")
                for r in result:
                    print(r)

            elif choice == 3:
                return
            else:
                print("Invalid choice!")
                
    # ---------- Search / Sort / Filter ----------
    def search_sort_filter(self):
        while True:
            if self.array is None:
                print("No array created yet!")
                return

            print("\nChoose an option:")
            print("1. Search a value\n2. Sort the array\n3. Filter values\n4. Go Back")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                value = float(input("Enter value to search: "))
                locations = np.where(self.array == value)
                print("Value found at:", locations)

            elif choice == 2:
                result = np.sort(self.array, axis=-1)
                print("Sorted Array:\n", result)

            elif choice == 3:
                cond = float(input("Enter threshold to filter values greater than: "))
                result = self.array[self.array > cond]
                print("Filtered Values:", result)

            elif choice == 4:
                return
            else:
                print("Invalid choice!")
                
    # ---------- Aggregating & Statistics ----------
   
    def statistics(self):
        while True:
            if self.array is None:
                print("No array created yet!")
                return

            print("\nChoose a statistical operation:")
            print("1. Sum\n2. Mean\n3. Median\n4. Standard Deviation\n5. Variance\n6. Go Back")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("Sum:", np.sum(self.array))
            elif choice == 2:
                print("Mean:", np.mean(self.array))
            elif choice == 3:
                print("Median:", np.median(self.array))
            elif choice == 4:
                print("Standard Deviation:", np.std(self.array))
            elif choice == 5:
                print("Variance:", np.var(self.array))
            elif choice == 6:
                return
            else:
                print("Invalid choice!")
                
# ---------------------- Main Menu ----------------------
def menu():
    obj = DataAnalytics()

    while True:
        print("\nWelcome to the NumPy Analyzer")
        print("=" * 40)
        print("1. Create a NumPy Array")
        print("2. Perform Mathematical Operations + Index/Slice")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            obj.create_array()
        elif choice == 2:
            obj.math_operations()
        elif choice == 3:
            obj.combine_split()
        elif choice == 4:
            obj.search_sort_filter()
        elif choice == 5:
            obj.statistics()
        elif choice == 6:
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
