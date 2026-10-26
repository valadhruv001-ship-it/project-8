🔢 NumPy Analyzer
An Interactive, Menu-Driven NumPy Array Toolkit

Create an array once. Explore it, transform it, and analyze it — all through a simple, beginner-friendly Python menu.

!Python !NumPy !Project !Status

📌 About the Project

NumPy Analyzer is a Python-based project designed to make working with NumPy arrays simple and interactive.

Instead of writing separate code for every operation, users can create a NumPy array once and perform multiple operations on the same array using a menu-driven interface.

The project is organized into separate Python modules, making the code easier to understand, maintain, and extend.

🎯 Project Objectives
Understand NumPy arrays and their dimensions.
Practice Python functions, modules, and packages.
Use match-case statements for menu navigation.
Perform mathematical and statistical computations.
Learn how multiple Python files share data.
✨ Features
#	Feature	Description
1️⃣	Array Creation	Create 1D, 2D, and 3D NumPy arrays from user input.
2️⃣	Indexing & Slicing	Access individual elements and extract portions of arrays.
3️⃣	Mathematical Operations	Perform addition, subtraction, multiplication, and division.
4️⃣	Combine & Split	Stack arrays vertically or horizontally and split arrays into equal parts.
5️⃣	Search	Find the positions of a specified value.
6️⃣	Sort	Sort array values in ascending or descending order.
7️⃣	Filter	Select values greater than, less than, or equal to a given number.
8️⃣	Statistics	Calculate sum, mean, median, standard deviation, and variance.
🛠️ Built With
Python — Core programming language.
NumPy — Numerical computing and array operations.

Prerequisite: Python 3.10 or newer, because the project uses match-case statements.

📂 Project Structure
text
numpy-analyzer/
│
├── main.py
│
└── tools/
    ├── __init__.py
    ├── array_data.py
    ├── array_creation.py
    ├── mathematical_operation.py
    ├── combine_split_array.py
    ├── search_sort_array.py
    └── aggregate_stats.py

File	Responsibility
main.py	Displays the main menu and connects all modules.
array_data.py	Stores the shared NumPy array.
array_creation.py	Creates arrays and handles indexing and slicing.
mathematical_operation.py	Performs arithmetic operations.
combine_split_array.py	Combines and splits arrays.
search_sort_array.py	Handles searching, sorting, and filtering.
aggregate_stats.py	Calculates aggregate and statistical values.
🔗 How the Shared Array Works

One of the key features of this project is shared array storage.

The array is created once and stored in array_data.py. The other modules access that same array instead of repeatedly asking the user to enter it.

For example, array_data.py contains:

python
current_array = None


When a user creates an array, array_creation.py saves it:

python
array_data.current_array = arr


Other modules retrieve it using:

python
from tools import array_data

arr = array_data.current_array


This approach keeps the project modular and allows different tools to work with the same array.

🚀 Getting Started
1. Clone the repository
bash
git clone <your-repository-url>


Replace <your-repository-url> with your GitHub repository URL.

2. Navigate to the project folder
bash
cd numpy-analyzer

3. Install NumPy
bash
python -m pip install numpy

4. Run the application

Make sure your terminal is in the folder containing main.py and the tools directory.

bash
python main.py

💻 Application Menu

When the application starts, the user sees the following menu:

text
===============================================
          WELCOME TO NUMPY ANALYZER
===============================================

1. Create a NumPy Array
2. Mathematical Operations
3. Combine or Split Arrays
4. Search, Sort or Filter
5. Aggregates and Statistics
6. Exit

Enter your choice:

📊 Example: Creating a 2D Array
text
Select the type of Array to create:
1. 1D Array
2. 2D Array
3. 3D Array

Enter your choice: 2
Enter number of rows: 2
Enter number of columns: 2
Enter elements: 1 2 3 4

Array created successfully!
[[1 2]
 [3 4]]


After creation, the indexing and slicing menu opens automatically.

The user can then return to the main menu and perform other operations on the existing array.

🧮 Example: Mathematical Operation

For an existing array:

text
[[1 2]
 [3 4]]


If the user chooses addition and enters the second array:

text
5 6 7 8


The result is:

text
Addition:
[[ 6  8]
 [10 12]]


Both arrays must have the same shape for element-wise mathematical operations.

🛡️ Input Validation

The project includes checks to make the application more reliable:

Dimensions must be positive.
The number of input elements must match the selected array dimensions.
Invalid menu selections and non-numeric input are handled.
Division by zero is prevented.
Operations requiring an array check whether one has been created.
Array splitting validates whether equal-sized parts are possible.
📚 Concepts Demonstrated

This project provides practical experience with:

Python functions and modules
Packages and import statements
match-case control flow
Loops and conditional logic
Exception handling
NumPy arrays and array reshaping
Indexing, slicing, and Boolean filtering
Mathematical and statistical functions
Shared data between modules
👩‍💻 Author

Bhavya Shah

Built as a Python and NumPy learning project to explore array manipulation, modular programming, and data analysis.

⭐ If you find this project useful, consider giving the repository a star!

Made with Python and NumPy.
