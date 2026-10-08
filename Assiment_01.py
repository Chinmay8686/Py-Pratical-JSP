# Assignment 1 - Student Performance Management System
# Requirements:
# - integer & float: store student scores (marks) in integer or float values
# - string: store student names, subjects, and display formatted messages
# - boolean: flag a student as passed or failed (True/False)
# - list: maintain a list of all students
# - tuple: store immutable values like student ID or birthdate
# - set: store unique subjects taken by each student
# - dictionary: map student IDs to their details and scores

# Dictionary for students
students = {
    "S101": {
        "name": "Ash",
        "scores": [85, 90, 88],  # integer marks
        "subjects": {"Math", "Science", "English"},
        "birthdate": (2008, 4, 15),
    },
    "S102": {
        "name": "patil",
        "scores": [72, 65, 80.5],  # float marks
        "subjects": {"Math", "History", "Computer"},
        "birthdate": (2009, 1, 22),
    },
    "S103": {
        "name": "Geera",
        "scores": [50, 60, 58],
        "subjects": {"Math", "Science", "Art"},
        "birthdate": (2008, 9, 10),
    },
}

# List of all students
student_list = [student["name"] for student in students.values()]


def calculate_average(marks):
    """Calculate the average of a list of marks."""
    return sum(marks) / len(marks)


passed_students = []

for student_id, details in students.items():
    student_name = details["name"]
    student_marks = details["scores"]
    average_score = calculate_average(student_marks)
    passed = average_score >= 60  # boolean logic for pass/fail
    details["passed"] = passed
    details["average"] = average_score

    if passed:
        passed_students.append(student_name)

    print(f"Student ID: {student_id}")
    print(f"Name: {student_name}")
    print(f"Subjects: {sorted(details['subjects'])}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Pass/Fail: {'Passed' if passed else 'Failed'}")
    print(f"Birthdate: {details['birthdate']}")
    print("-" * 30)

print("All students:", student_list)
print("Students who passed:", passed_students)
