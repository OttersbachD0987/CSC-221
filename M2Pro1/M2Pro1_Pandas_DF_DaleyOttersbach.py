# Lets you search parks in the data set by many different factors.
# 9/21/2025
# CSC221 M2Pro1– Panda DF
# Daley Ottersbach

from functions import AggregateFunction, DisplayMenu, DisplayTopRecords, NumberOfParks, NumberOfParksByRegion, NumberOfParksByState, ParksByStateCode, SearchParksByFeature, StateParksWithWaterfallsByState, TopParksByAcreagePerRegion
from pandas import DataFrame
import pandas as pd


def Main() -> None:
    """The main function.
    """
    # Load the data sheets.
    dataSheets: dict[str, DataFrame] = pd.read_excel("east_coast_major_state_parks-1.xlsx", None)
    # Load the major parks sheet.
    majorParks: DataFrame = dataSheets["east_coast_major_state_parks"]
    # Display major parks.
    print(majorParks)
    # Load the state codes sheet.
    statecodesDict: dict[str, str] = dataSheets["us_states_code"].set_index("State").to_dict()["Abbreviation"]
    # Display state codes.
    print(statecodesDict)
    # Pivot major parks.
    pivotedParks: DataFrame = majorParks.pivot_table(index=["state", "county", "park name"], values=["acreage", "Feature"], aggfunc=AggregateFunction)
    # Display pivoted major parks.
    print(pivotedParks)
    # Merge the major parks with the state codes.
    usableParkTable: DataFrame = majorParks.join(majorParks.apply(lambda r: statecodesDict[r.state], axis=1).rename("State Codes"))
    # Print the merged tables.
    print(usableParkTable)

    # Create the sentinel.
    option: int = -1
    while option != 9:
        # Display menu and get the input.
        DisplayMenu()
        option = int(input("Choice: "))
        # Switch options: 1, 2, 3, 4, 5, 6, 7, 8, & 9
        match option:
            case 1:
                DisplayTopRecords(usableParkTable.set_index(["park name", "state", "county"]))
            case 2:
                NumberOfParks(usableParkTable)
            case 3:
                NumberOfParksByState(usableParkTable)
            case 4:
                NumberOfParksByRegion(usableParkTable)
            case 5:
                TopParksByAcreagePerRegion(usableParkTable)
            case 6:
                StateParksWithWaterfallsByState(usableParkTable)
            case 7:
                SearchParksByFeature(usableParkTable)
            case 8:
                ParksByStateCode(usableParkTable)
            case 9:
                ...

# Do the main if main.
if __name__ == "__main__":
    Main()