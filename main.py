from tools.array_creation import create_array
from tools.mathematical_operation import mathematical_menu
from tools.combine_split_array import combine_split_menu
from tools.search_sort_array import search_sort_filter_menu
from tools.aggregate_stats import statistics_menu


while True:
    print("\n ===============================================" )
    print("       WELCOME TO NUMPY ANALYZER")
    print("\n ===============================================" )

    print("1. Create a NumPy Array")
    print("2. Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort or Filter")
    print("5. Aggregates and Statistics")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                create_array()

            case 2:
                mathematical_menu()

            case 3:
                combine_split_menu()

            case 4:
                search_sort_filter_menu()

            case 5:
                statistics_menu()

            case 6:
                print("\nThank you for using NumPy Analyzer!")
                break

            case _:
                print("Invalid choice. Please try again.")

    except ValueError:
        print("Please enter a valid menu number.")