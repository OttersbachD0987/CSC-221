# the dictionary
import random

letters = "abcdefghijklmnopqrstuvwxyz"

def RandomWord(a_size: int = 7) -> str:
    return "".join([random.choice(letters) for _ in range(a_size)]).capitalize()

scores: dict[str, dict[str, int]] = {
    "Tom":{
        "Math":70,
        "Sci":100
    },
    "Jessica":{
        "Math":99,
        "Sci":85
    },
    "Seira":{
        "Math":78,
        "Sci":77
    }
}

def AddStudents(a_amount: int) -> None: 
    global scores

    for _ in range(a_amount):
        scores[RandomWord()] = {
            "Math": random.randint(0, 100),
            "Sci": random.randint(0, 100)
        }

import StudentDictManipulations as SDM
import timeit

def main() -> None:
    gunk = SDM.PercentageToLetterStudentGrade(SDM.AverageStudentGrade(scores))
    print(f"{len(scores)} Students")
    print(timeit.timeit(stmt="SDM.TabularDisplay(gunk)", setup="import StudentDictManipulations as SDM", number=25, globals={"gunk": gunk}))
    print(timeit.timeit(stmt="SDM.TabularDisplayGenerator(gunk)", setup="import StudentDictManipulations as SDM", number=25, globals={"gunk": gunk}))

if __name__ == "__main__":
    main()
    AddStudents(97)
    main()
    for _ in range(9):
        AddStudents(100)
        main()
    for _ in range(9):
        AddStudents(1000)
        main()
