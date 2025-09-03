import os, sys

def PercentageToLetterGrade(a_percentage: float) -> str:
    """Converts a percentage grade to a letter grade.

    Args:
        a_percentage (float): The percentage grade to convert.

    Returns:
        str: The letter grade.
    """
    if a_percentage >= 90:
        return "A"
    elif a_percentage >= 80:
        return "B"
    elif a_percentage >= 70:
        return "C"
    elif a_percentage >= 60:
        return "D"
    else:
        return "F"

def AverageStudentGrade(a_students: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:
    """Converts a dictionary of students to a dictionary of students with average grades.

    Args:
        a_students (dict[str, dict[str, int]]): The dictionary of dictionaries that contain the students grades.

    Returns:
        dict[str, dict[str, int]]: A new dictionary with added averages.
    """
    dict_to_return: dict[str, dict[str, int]] = {student_name: {subject_name: subject_grade for subject_name, subject_grade in student_grades.items() if subject_name != "Avg"} for student_name, student_grades in a_students.items()}
    for _, student_subjects in dict_to_return.items():
        student_subjects["Avg"] = sum(student_subjects.values()) / len(student_subjects)
    return dict_to_return

def PercentageToLetterStudentGrade(a_students: dict[str, dict[str, int]]) -> dict[str, dict[str, str]]:
    """Converts a dictionary of students to a dictionary of students with letter grades.

    Args:
        a_students (dict[str, dict[str, int]]): The dictionary of dictionaries that contain the students grades.

    Returns:
        dict[str, dict[str, str]]: A new dictionary with letter grades.
    """
    return {
        student_name: {
            subject_name: PercentageToLetterGrade(subject_grade) for subject_name, subject_grade in student_grades.items()
        } for student_name, student_grades in a_students.items()
    }

def TabularDisplay(a_students: dict[str, dict[str, str]]) -> None:
    """Display a dictionary of students in a tabular format.

    Args:
        a_students (dict[str, dict[str, str]]): The dictionary of students.
    """
    with open(os.devnull, "w") as f:
        print(f"{"Name":<15} {" ".join([f"{subject_name:<6}" for subject_name in list(a_students.values())[0].keys()])}", file=f)
        for student_name, student_subjects in a_students.items():
            print(f"{student_name:<15} {" ".join([f"{subject_grade:<6}" for subject_grade in student_subjects.values()])}", file=f)

def TabularDisplayGenerator(a_students: dict[str, dict[str, str]]) -> None:
    """Display a dictionary of students in a tabular format.

    Args:
        a_students (dict[str, dict[str, str]]): The dictionary of students.
    """
    with open(os.devnull, "w") as f:
        print(f"{"Name":<15} {" ".join([f"{subject_name:<6}" for subject_name in list(a_students.values())[0].keys()])}", file=f)
        print("\n".join([f"{student_name:<15} {" ".join([f"{subject_grade:<6}" for subject_grade in student_subjects.values()])}" for student_name, student_subjects in a_students.items()]), file=f)
