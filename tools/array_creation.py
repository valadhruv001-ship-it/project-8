
import numpy as np
from tools import array_data


def create_array():
    print("\nSelect the type of Array to create: ")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")

    try:
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                num = int(input("Enter number of elements: "))

                if num <= 0:
                    print("Number of elements must be positive.")
                    return

                values = list(map(
                    int, input("Enter elements: ").split()
                ))

                if len(values) != num:
                    print("Invalid number of elements.")
                    return

                arr = np.array(values)

            case 2:
                row = int(input("Enter number of rows: "))
                col = int(input("Enter number of columns: "))

                if row <= 0 or col <= 0:
                    print("Dimensions must be positive.")
                    return

                values = list(map(
                    int, input("Enter elements: ").split()
                ))

                if len(values) != row * col:
                    print("Invalid number of elements.")
                    return

                arr = np.array(values).reshape(row, col)

            case 3:
                depth = int(input("Enter number of layers: "))
                row = int(input("Enter number of rows: "))
                col = int(input("Enter number of columns: "))

                if min(depth, row, col) <= 0:
                    print("Dimensions must be positive.")
                    return

                total = depth * row * col

                values = list(map(
                    int, input("Enter elements: ").split()
                ))

                if len(values) != total:
                    print("Invalid number of elements.")
                    return

                arr = np.array(values).reshape(depth, row, col)

            case _:
                print("Invalid choice.")
                return

        # Array is save in array data.py
        array_data.current_array = arr

        print("\nArray created successfully!")
        print(arr)

        array_operations()

    except ValueError:
        print("Please enter valid integer values.")


def array_operations():
    while True:
        print("\nChoose an Operation: ")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Exit")

        try:
            op = int(input("Enter your choice: "))
            arr = array_data.current_array

            match op:
                case 1:
                    print("Array shape:", arr.shape)
                    print("Enter one index for each dimension.")

                    indices = tuple(map(
                        int,
                        input("Enter indices separated by spaces: ").split()
                    ))

                    if len(indices) != arr.ndim:
                        print(f"Please enter {arr.ndim} index value(s).")
                        continue

                    print("Element:", arr[indices])

                case 2:
                    if arr.ndim == 1:
                        start = int(input("Enter start index: "))
                        stop = int(input("Enter stop index: "))

                        print("Sliced Array:", arr[start:stop])

                    else:
                        print("Enter a slice for each dimension.")
                        print("Example 2D: 0:2,0:2")
                        print("Example 3D: 0:2,0:2,0:2")

                        expression = input("Enter slices: ")
                        parts = expression.split(",")

                        if len(parts) != arr.ndim:
                            print("Incorrect number of slices.")
                            continue

                        slices = []

                        for part in parts:
                            values = part.strip().split(":")

                            if len(values) not in (2, 3):
                                raise ValueError("Invalid slice format.")

                            numbers = [
                                int(x.strip()) if x.strip() else None
                                for x in values
                            ]

                            slices.append(slice(*numbers))

                        print("Sliced Array:", arr[tuple(slices)])

                case 3:
                    print("Returning to the main menu.")
                    break

                case _:
                    print("Invalid choice.")

        except (ValueError, IndexError):
            print("Invalid input or index. Please try again.")
