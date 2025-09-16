# A brief description of the project
# Date
# CSC221 M2Pro1– Panda DF
# Daley Ottersbach

import pandas as pd
from pandas._typing import IntStrT
from pandas import DataFrame

def DisplayMenu() -> None:
    print("1. Display First 15 records in dataset\n2. Get Number of record(parks) listed in dataset\n3. Get Number of State Parks by State\n4. Get Number of State Parks per Region\n5. Get Top 2, by acreage, per Region\n6. Get State Parks with Waterfalls by State\n7. Search Parks by Feature\n8. Allow to Search DataFrame by State Code\n9. Exit")

def DisplayTopRecords() -> None:
    ...

def NumberOfParks() -> None:
    ...

def OptionThree() -> None:
    ...

def OptionFour() -> None:
    ...

def OptionFive() -> None:
    ...

def OptionSix() -> None:
    ...

def OptionSeven() -> None:
    ...

def OptionEight() -> None:
    ...

def Main() -> None:
    dataSheets: dict[IntStrT, DataFrame] = pd.read_excel("east_coast_major_state_parks-1.xlsx", None)
    a: DataFrame = dataSheets["east_coast_major_state_parks"].pivot_table(index=["state", "county", "park name"], values=["acreage", "Feature"], aggfunc=lambda a: a)
    b: DataFrame = dataSheets["us_states_code"]
    print(a)
    print(b)

if __name__ == "__main__":
    Main()