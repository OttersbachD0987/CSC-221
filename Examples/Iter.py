subject_students: dict[str, dict[str, float]] = {
    "Math": {
        "Bob": 97.35,
        "Shirley": 78.84,
        "Hammond": 64.53
    },
    "Science": {
        "Bob": 64.84,
        "Shirley": 97.53,
        "Hammond": 78.35
    }
}

students = subject_students["Math"].keys()

# Align to 9
print(f"{" " * 9} {" ".join([f"{student:<9}" for student in students])} Average")
for subject, student_grades in subject_students.items():
    print(f"{subject:<9} {" ".join([f"{grade:<9.2f}" for grade in student_grades.values()])} {sum(student_grades.values())/len(student_grades):<9.2f}")
print(f"{"Average":<9} {" ".join([f"{sum([student_grades[student] for student_grades in subject_students.values()])/len(subject_students):<9.2f}" for student in students])}")
print()
