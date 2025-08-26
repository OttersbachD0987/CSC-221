#region List
subject_grades: list[list[float]] = [
    [100,  95,  89],
    [ 89,  81,  87]
]

header: str = " ".join([f"{f"Stu {index + 1}":<6}" for index in range(len(subject_grades[0]))])

print(header)
for grades in subject_grades:
    for grade in grades:
        print(f"{grade:<6.2f} ", end="")
    print()

print()

print(header)
for grades in subject_grades:
    print(" ".join([f"{grade:<6.2f}" for grade in grades]))

print()

print(header)
print("\n".join([" ".join([f"{grade:<6.2f}" for grade in grades]) for grades in subject_grades]))

print()

for grades in subject_grades:
    print(f"{sum(grades)/len(grades):.2f}")

print()

print("\n".join([f"{sum(grades)/len(grades):.2f}" for grades in subject_grades]))
#endregion

#region List
subject_grades: dict[str, list[float]] = {
    "Math": [100,  95,  89],
    "Sci":  [ 89,  81,  87]
}

header: str = " ".join([f"{f"Stu {index + 1}":<6}" for index in range(len(subject_grades["Math"]))])

print(header)
for subject, grades in subject_grades.items():
    for grade in grades:
        print(f"{grade:<6.2f} ", end="")
    print()

print()

print(header)
for subject, grades in subject_grades.items():
    print(" ".join([f"{grade:<6.2f}" for grade in grades]))

print()

print(header)
print("\n".join([" ".join([f"{grade:<6.2f}" for grade in grades]) for subject, grades in subject_grades.items()]))

print()

for subject, grades in subject_grades.items():
    print(f"{sum(grades)/len(grades):.2f}")

print()

print("\n".join([f"{f"{subject}:":<7} {sum(grades)/len(grades):.2f}" for subject, grades in subject_grades.items()]))
#endregion