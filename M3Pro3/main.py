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
from pandas import DataFrame

def main() -> None:
    """...
    """
    frame: DataFrame = pd.read_excel("recipe_data.xlsx", None)["Sheet1"]
    print(frame)

if __name__ == "__main__":
    main()