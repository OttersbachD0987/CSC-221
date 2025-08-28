# the dictionary

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

import StudentDictManipulations as SDM
import timeit

def main() -> None:
    print(timeit.timeit(stmt="SDM.TabularDisplay(SDM.PercentageToLetterStudentGrade(SDM.AverageStudentGrade(scores)))", setup="import StudentDictManipulations as SDM", number=5, globals={"scores": scores}))
    print(timeit.timeit(stmt="SDM.TabularDisplayGenerator(SDM.PercentageToLetterStudentGrade(SDM.AverageStudentGrade(scores)))", setup="import StudentDictManipulations as SDM", number=5, globals={"scores": scores}))

if __name__ == "__main__":
    main()