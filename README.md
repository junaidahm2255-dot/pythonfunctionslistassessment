# Python Functions, Strings and Lists Assessment

## Project Overview
This repository contains two separate Python programs developed for the Functions, Strings and Lists assessment. Both programs validate user input and use custom functions.

## Program 1: Student Result Card Generator
`result_card_generator.py` asks for one student's name, roll number, and marks in five subjects. It calculates the total and percentage, assigns a grade, and prints a formatted result card. A mark below 40 in any subject makes the final result Fail, regardless of the overall percentage.

### Concepts used
- Defining and calling functions with `def`
- Function parameters and `return`
- String methods: `strip()`, `title()`, and `isdigit()`
- Input validation with `while` loops and `try/except`
- Dictionaries, `sum()`, `len()`, `any()`
- f-strings and formatted decimal output

### Run
```bash
python result_card_generator.py
```

### Sample input
```text
Enter student name:   ali ahmad
Enter roll number: 1025
Enter marks in English (0-100): 85
Enter marks in Mathematics (0-100): 91
Enter marks in Computer Science (0-100): 88
Enter marks in Physics (0-100): 79
Enter marks in Statistics (0-100): 90
```

### Sample output (result summary)
```text
Student Name       : Ali Ahmad
Roll Number        : 1025
Total Obtained     : 433 / 500
Percentage         : 86.60%
Letter Grade       : A
Final Status       : Pass
```

## Program 2: Class Marks Analyzer
`class_marks_analyzer.py` collects names and marks for a class. It calculates the class average, finds the highest and lowest marks (including ties), counts passing and failing students, lists students above average, and sorts marks from highest to lowest.

### Concepts used
- Lists: `student_names = []` and `student_marks = []`
- `append()`, `len()`, `sum()`, `max()`, `min()`, and `sorted()`
- `for` and `while` loops
- Custom functions, parameters, and return values
- Input validation with `try/except`
- `zip()` to keep student names matched with marks
- `lambda` as the sorting key

### Run
```bash
python class_marks_analyzer.py
```

### Sample input
```text
How many students are in the class? 3
Enter student name: Ali
Enter marks for Ali (0-100): 75
Enter student name: Sara
Enter marks for Sara (0-100): 90
Enter student name: Ahmed
Enter marks for Ahmed (0-100): 45
```

### Sample output (summary)
```text
Number of students : 3
Class average      : 70.00
Highest marks      : 90
Sara: 90
Lowest marks       : 45
Ahmed: 45
Passing students   : 2
Failing students   : 1

Students scoring above the class average:
Ali: 75
Sara: 90

Student marks (highest to lowest):
Sara: 90
Ali: 75
Ahmed: 45
```

## Requirements
- Python 3
- No third-party packages are required.

## Repository Structure
```text
python-functions-lists-assessment/
├── result_card_generator.py
├── class_marks_analyzer.py
└── README.md
```

## Notes
Run each program separately. Enter whole-number marks from 0 to 100. The programs will ask again when an invalid value is entered.
