
import numpy as np
from tools import array_data


def search_sort_filter_menu():
    a = array_data.current_array

    if a is None:
        print("Please create an array first.")
        return

    while True:
        print("\nChoose an option:")
        print("1. Search a Value")
        print("2. Sort Array")
        print("3. Filter Values")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    x = float(input("Enter value to search: "))
                    indexes = np.argwhere(a == x)

                    if len(indexes) > 0:
                        print("Found at indices:")
                        print(indexes)
                    else:
                        print("Value not found.")

                case 2:
                    print("1. Ascending")
                    print("2. Descending")

                    order = int(input("Enter your choice: "))

                    match order:
                        case 1:
                            print("Sorted Array:", np.sort(a, axis=-1))

                        case 2:
                            print(
                                "Sorted Array:",
                                np.flip(np.sort(a, axis=-1), axis=-1)
                            )

                        case _:
                            print("Invalid choice.")

                case 3:
                    print("1. Greater than")
                    print("2. Less than")
                    print("3. Equal to")

                    condition = int(input("Enter your choice: "))
                    x = float(input("Enter comparison value: "))

                    match condition:
                        case 1:
                            result = a[a > x]

                        case 2:
                            result = a[a < x]

                        case 3:
                            result = a[a == x]

                        case _:
                            print("Invalid choice.")
                            continue

                    print("Filtered Array:", result)

                case 4:
                    break

                case _:
                    print("Invalid choice.")

        except ValueError:
            print("Please enter valid values.")