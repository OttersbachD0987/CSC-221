# Lets you search parks in the data set by many different factors.
# 11/16/2025
# CSC221 M6Lab
# # Daley Ottersbach

from functions import AggregateFunction, DisplayMenu, DisplayTopRecords, NumberOfParks, NumberOfParksByRegion, NumberOfParksByState, ParksByStateCode, SearchParksByFeature, StateParksWithWaterfallsByState, TopParksByAcreagePerRegion
from pandas import DataFrame
import pandas as pd


def Main() -> None:
    """The main function.
    """
    # Load the data sheets.
    dataSheets: dict[str, DataFrame] = pd.read_excel("east_coast_major_state_parks_updated.xlsx", None)
    # Load the major parks sheet.
    majorParks: DataFrame = dataSheets["east_coast_major_state_parks"]
    # Display major parks.
    print(majorParks)
    # Load the state codes sheet.
    statecodesDict: dict[str, str] = dataSheets["us_states_code"].set_index("State").to_dict()["Abbreviation"]
    # Display state codes.
    print(statecodesDict)
    # Load the regions sheet.
    regionsDict: dict[str, str] = dataSheets["Region_by_park"].set_index("Park").to_dict()["Region"]
    # Display regions.
    print(regionsDict)
    # Pivot major parks.
    pivotedParks: DataFrame = majorParks.pivot_table(index=["state", "county", "Region", "park name"], values=["acreage", "Feature"], aggfunc=AggregateFunction)
    # Display pivoted major parks.
    print(pivotedParks)
    # Merge the major parks with the state codes.
    unusableParkTable: DataFrame = majorParks.join(majorParks.apply(lambda r: statecodesDict[r.state], axis=1).rename("State Codes"))
    def Dunder(a_row):
        print("Row")
        print(a_row)
        a_row["Region"] = regionsDict[a_row["park name"]]
        return a_row
    usableParkTable: DataFrame = unusableParkTable.apply(Dunder, axis=1)
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