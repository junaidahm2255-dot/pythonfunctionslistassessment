# Student Result Card Generator
# This program collects one student's details and generates a formatted result card.

# Get a valid mark between 0 and 100 for a subject.
def get_valid_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter marks in {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Invalid marks. Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Calculate the percentage from obtained and maximum marks.
def calculate_percentage(total, max_total):
    return (total / max_total) * 100


# Return the letter grade according to the given grading criteria.
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


# Remove extra spaces and capitalize each part of the student's name.
def format_name(name):
    return name.strip().title()


# Ask for a non-empty student name.
def get_student_name():
    while True:
        name = input("Enter student name: ")
        if name.strip():
            return format_name(name)
        print("Name cannot be empty. Please try again.")


# Ask for a roll number containing digits only.
def get_roll_number():
    while True:
        roll_number = input("Enter roll number: ").strip()
        if roll_number.isdigit():
            return roll_number
        print("Invalid roll number. Use digits only.")


def main():
    print("\n========== STUDENT RESULT CARD GENERATOR ==========")

    student_name = get_student_name()
    roll_number = get_roll_number()

    subjects = ["English", "Mathematics", "Computer Science", "Physics", "Statistics"]
    student_marks = {}

    for subject in subjects:
        student_marks[subject] = get_valid_marks(subject)

    total_obtained = sum(student_marks.values())
    maximum_total = len(subjects) * 100
    percentage = calculate_percentage(total_obtained, maximum_total)

    # A mark below 40 in any subject makes the overall result a failure.
    has_failed_subject = any(mark < 40 for mark in student_marks.values())
    grade = get_grade(percentage)
    if has_failed_subject:
        grade = "Fail"

    final_status = "Fail" if has_failed_subject or percentage < 50 else "Pass"

    print("\n" + "=" * 48)
    print("                 STUDENT RESULT CARD")
    print("=" * 48)
    print(f"Student Name       : {student_name}")
    print(f"Roll Number        : {roll_number}")
    print("-" * 48)
    print(f"{'Subject':<25}{'Marks':>10}")
    print("-" * 48)

    for subject, marks in student_marks.items():
        print(f"{subject:<25}{marks:>10}")

    print("-" * 48)
    print(f"{'Total Obtained':<25}{total_obtained:>10} / {maximum_total}")
    print(f"{'Percentage':<25}{percentage:>9.2f}%")
    print(f"{'Letter Grade':<25}{grade:>10}")
    print(f"{'Final Status':<25}{final_status:>10}")
    print("=" * 48)


if __name__ == "__main__":
    main()
