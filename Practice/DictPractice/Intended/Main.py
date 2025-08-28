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

def main() -> None:
    SDM.TabularDisplay(SDM.PercentageToLetterStudentGrade(SDM.AverageStudentGrade(scores)))

if __name__ == "__main__":
    main()