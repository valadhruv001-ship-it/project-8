
import numpy as np
from tools import array_data


def statistics_menu():
    a = array_data.current_array

    if a is None:
        print("Please create an array first.")
        return

    while True:
        print("\nChoose an aggregate/statistical option: ")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    print("Sum:", np.sum(a))

                case 2:
                    print("Mean:", np.mean(a))

                case 3:
                    print("Median:", np.median(a))

                case 4:
                    print("Standard Deviation:", np.std(a))

                case 5:
                    print("Variance:", np.var(a))

                case 6:
                    break

                case _:
                    print("Invalid choice.")

        except ValueError:
            print("Please enter valid values.")
