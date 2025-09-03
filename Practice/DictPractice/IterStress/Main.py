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
    rawTime = (timeit.timeit(stmt="SDM.TabularDisplay(gunk)", setup="import StudentDictManipulations as SDM", number=25, globals={"gunk": gunk}))
    genTime = (timeit.timeit(stmt="SDM.TabularDisplayGenerator(gunk)", setup="import StudentDictManipulations as SDM", number=25, globals={"gunk": gunk}))
    itrTime = (timeit.timeit(stmt="SDM.TabularDisplayGenerator(gunk)", setup="import StudentDictManipulations as SDM", number=25, globals={"gunk": gunk}))
    print(f"{len(scores)} Students")
    print("-" * 26)
    print(f"Raw: {rawTime:.8f}s")
    print(f"Gen: {genTime:.8f}s")
    print(f"Itr: {itrTime:.8f}s")
    print("-" * 26)
    print(f"Raw/Gen: {rawTime/genTime:.4f}x")
    print(f"Raw/Itr: {rawTime/itrTime:.4f}x")
    print()
    print(f"Gen/Raw: {genTime/rawTime:.4f}x")
    print(f"Gen/Itr: {genTime/itrTime:.4f}x")
    print()
    print(f"Itr/Raw: {itrTime/rawTime:.4f}x")
    print(f"Itr/Gen: {itrTime/genTime:.4f}x")
    print("=" * 26)

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
    for _ in range(9):
        AddStudents(10000)
        main()
