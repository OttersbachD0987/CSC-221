# Lets you look through recipes from an XML file.
# 10/7/2025
# CSC221 M3Pro3
# Daley Ottersbach

# Name
#  String
# Ingredients
#  Comma Separated List
# Steps
#  Comma Separated List
# Type
#  Dessert/Main Course
# Sweetness_Level
#  int/None
# Spice_Level
#  int/None
# Is_Vegetarian
#  TRUE/FALSE

import pandas as pd
from pandas import DataFrame, Series
from typing import Any, Optional
from recipes import DessertRecipe, Recipe, MainCourseRecipe
from functions import displayInstructions, filterBy, intput, search, viewAll

def main() -> None:
    """Handles running the menus with loaded excel file.
    """
    try:
        frame: DataFrame = pd.read_excel("recipe_data.xlsx", None)["Sheet1"]
        def createClasses(inputSeries: Series) -> Series:
            data: dict[str, Any] = inputSeries.to_dict()
            match data["Type"]:
                case "Dessert":
                    inputSeries["Recipe"] = DessertRecipe(data["Name"], data["Ingredients"].split(", "), data["Steps"].split(", "), data["Is_Vegetarian"], data["Sweetness_Level"])
                case "Main Course":
                    inputSeries["Recipe"] = MainCourseRecipe(data["Name"], data["Ingredients"].split(", "), data["Steps"].split(", "), data["Is_Vegetarian"], data["Spice_Level"])
                case _:
                    inputSeries["Recipe"] = None
            return inputSeries
        use: DataFrame = frame.apply(createClasses, axis=1)

        choice: int = 0
        viewable: Optional[DataFrame] = None
        while choice != 4:
            displayInstructions()
            choice = intput("Choice: ")
            print()
            match choice:
                case 1:
                    viewAll(use)
                case 2:
                    viewable = search(use, input("Name: "))
                    if viewable is not None:
                        viewAll(viewable)
                case 3:
                    viewable = filterBy(use)
                    if viewable is not None:
                        viewAll(viewable)
                case 4:
                    ...
                case _:
                    print(f"{choice} is invalid input.")
    except FileNotFoundError as e:
        print(f"The file {e.filename} does not exist.")
    except PermissionError as e:
        print(f"You do not have sufficient permissions to access the file {e.filename}.")
    except IsADirectoryError as e:
        print(f"{e.filename} is not a file, it is a directory.")
    except ValueError as e:
        print(f"{e}")


if __name__ == "__main__":
    main()