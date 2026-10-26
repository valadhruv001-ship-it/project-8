
import numpy as np
from tools import array_data


def mathematical_menu():
    a = array_data.current_array

    if a is None:
        print("Please create an array first.")
        return

    print("Mathematical Operations:")

    while True:
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        try:
            choice = int(input("Enter your choice: "))

            match choice:
                case 1 | 2 | 3 | 4:
                    print("\nOriginal Array:")
                    print(a)

                    values = list(map(
                        int,
                        input(
                            f"\nEnter the same-size array elements "
                            f"({a.size} elements separated by space): "
                        ).split()
                    ))

                    if len(values) != a.size:
                        print("Incorrect number of elements.")
                        continue

                    b = np.array(values).reshape(a.shape)

                    print("\nSecond Array:")
                    print(b)

                    match choice:
                        case 1:
                            print("\nResult of Addition:")
                            print(a + b)

                        case 2:
                            print("\nResult of Subtraction:")
                            print(a - b)

                        case 3:
                            print("\nResult of Multiplication:")
                            print(a * b)

                        case 4:
                            if np.any(b == 0):
                                print("Cannot divide by zero.")
                                continue

                            print("\nResult of Division:")
                            print(a / b)

                    break

                case _:
                    print("Invalid choice.")

        except ValueError:
            print("Please enter valid integer values.")