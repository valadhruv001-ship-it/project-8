import numpy as np
from tools import array_data


def combine_split_menu():
    a = array_data.current_array

    if a is None:
        print("Please create an array first.")
        return

    while True:
        print("\nCombine or Split Arrays:")
        print("1. Combine Arrays")
        print("2. Split Array")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    print("\nOriginal Array:")
                    print(a)

                    values = list(map(
                        int,
                        input(
                            f"Enter the elements of another array "
                            f"to combine ({a.size} elements separated "
                            f"by space): "
                        ).split()
                    ))

                    if len(values) != a.size:
                        print("Incorrect number of elements.")
                        continue

                    b = np.array(values).reshape(a.shape)

                    print("\nSecond Array:")
                    print(b)

                    result = np.vstack((a, b))

                    print("\nCombined Array (Vertical Stack):")
                    print(result)

                case 2:
                    print("\nOriginal Array:")
                    print(a)

                    n = int(input("Enter number of equal parts: "))

                    if n <= 0 or a.shape[0] % n != 0:
                        print("Array cannot be split into equal parts.")
                        continue

                    parts = np.split(a, n, axis=0)

                    print("\nSplit Arrays:")
                    for part in parts:
                        print(part)

                case 3:
                    print("Exiting Combine or Split Arrays.")
                    break

                case _:
                    print("Invalid choice.")

        except ValueError:
            print("Please enter valid values.")