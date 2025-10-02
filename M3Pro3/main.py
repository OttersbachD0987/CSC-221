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
from typing import Any

def main() -> None:
    """...
    """
    frame: DataFrame = pd.read_excel("recipe_data.xlsx", None)["Sheet1"]
    print(frame)
    desserts: DataFrame = frame[(frame["Type"] == "Dessert") & (frame["Sweetness_Level"].notna())].reset_index(names=["Old_Index"])
    mainCourses: DataFrame = frame[(frame["Type"] == "Main Course") & (frame["Spice_Level"].notna())].reset_index(names=["Old_Index"])
    invalid: DataFrame = frame[((frame["Type"] == "Dessert") & (frame["Sweetness_Level"].isna())) | ((frame["Type"] == "Main Course") & (frame["Spice_Level"].isna()))].reset_index(names=["Old_Index"])
    print(desserts)
    print(mainCourses)
    print(invalid)
    def foobar(inpute):
        if isinstance(inpute, Series):
            print(inpute.to_dict())
        return Series()
    desserts.apply(foobar, axis=1)

if __name__ == "__main__":
    main()