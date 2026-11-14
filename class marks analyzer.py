# Class Marks Analyzer
# This program stores class marks and displays useful performance statistics.

# Ask for a valid positive number of students.
def get_student_count():
    while True:
        try:
            count = int(input("How many students are in the class? "))
            if count > 0:
                return count
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Ask for a valid mark between 0 and 100.
def get_valid_marks(student_name):
    while True:
        try:
            marks = int(input(f"Enter marks for {student_name} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Invalid marks. Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Calculate and return the average of all marks.
def calculate_average(student_marks):
    return sum(student_marks) / len(student_marks)


# Display every student who achieved the highest or lowest mark.
def display_students_with_mark(student_names, student_marks, target_mark):
    for name, mark in zip(student_names, student_marks):
        if mark == target_mark:
            print(f"{name}: {mark}")


# Display the students whose marks are above the class average.
def display_above_average(student_names, student_marks, average):
    found_student = False
    for name, mark in zip(student_names, student_marks):
        if mark > average:
            print(f"{name}: {mark}")
            found_student = True
    if not found_student:
        print("No student scored above the class average.")


def main():
    print("\n========== CLASS MARKS ANALYZER ==========")

    student_names = []
    student_marks = []

    number_of_students = get_student_count()

    # Collect each student's name and validated marks.
    for index in range(number_of_students):
        print(f"\nStudent {index + 1}")
        while True:
            name = input("Enter student name: ").strip()
            if name:
                student_names.append(name.title())
                break
            print("Name cannot be empty. Please try again.")

        mark = get_valid_marks(student_names[-1])
        student_marks.append(mark)

    class_average = calculate_average(student_marks)
    highest_marks = max(student_marks)
    lowest_marks = min(student_marks)

    passing_students = sum(1 for mark in student_marks if mark >= 50)
    failing_students = sum(1 for mark in student_marks if mark < 50)

    print("\n============= CLASS PERFORMANCE REPORT =============")
    print(f"Number of students : {len(student_names)}")
    print(f"Class average      : {class_average:.2f}")
    print(f"Highest marks      : {highest_marks}")
    display_students_with_mark(student_names, student_marks, highest_marks)
    print(f"Lowest marks       : {lowest_marks}")
    display_students_with_mark(student_names, student_marks, lowest_marks)
    print(f"Passing students   : {passing_students}")
    print(f"Failing students   : {failing_students}")

    print("\nStudents scoring above the class average:")
    display_above_average(student_names, student_marks, class_average)

    # Sort name-mark pairs by marks in descending order without losing names.
    sorted_students = sorted(
        zip(student_names, student_marks),
        key=lambda student: student[1],
        reverse=True
    )

    print("\nStudent marks (highest to lowest):")
    for name, mark in sorted_students:
        print(f"{name}: {mark}")

    print("=" * 54)


if __name__ == "__main__":
    main()
