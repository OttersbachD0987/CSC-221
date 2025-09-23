from pandas import DataFrame

def DisplayMenu() -> None:
    """Displays the menu.
    """
    print("1. Display First 15 records in dataset\n2. Get Number of record(parks) listed in dataset\n3. Get Number of State Parks by State\n4. Get Number of State Parks per Region\n5. Get Top 2, by acreage, per Region\n6. Get State Parks with Waterfalls by State\n7. Search Parks by Feature\n8. Allow to Search DataFrame by State Code\n9. Exit")

def DisplayTopRecords(a_data: DataFrame) -> None:
    """Display the top records of a dataframe.
    """
    print(a_data.head(15))

def NumberOfParks(a_data: DataFrame) -> None:
    """Display the number of parks in a dataframe.
    """
    print(f"Number of Parks: {a_data.count()["park name"]}")

def NumberOfParksByState(a_data: DataFrame) -> None:
    """Display the number of parks by state.
    """
    print("\n".join([f"{state}: {parkCount}" for state, parkCount in a_data.pivot(values=["park name"], columns=["park name"], index=["state"]).count(axis=1).items()]))

def NumberOfParksByRegion(a_data: DataFrame) -> None:
    """Display the number of parks by region.
    """
    print("\n".join([f"{county}: {parkCount}" for county, parkCount in a_data.pivot(values=["park name"], columns=["park name"], index=["county"]).count(axis=1).items()]))

def TopParksByAcreagePerRegion(a_data: DataFrame) -> None:
    """Display the top two parks by acerage per region.
    """
    for state in a_data["state"].unique():
        print(a_data[a_data["state"] == state].sort_values("acreage").head(2)[["state", "acreage", "park name"]])

def StateParksWithWaterfallsByState(a_data: DataFrame) -> None:
    """Display state parks with waterfalls by states.
    """
    print(a_data[a_data["Feature"].str.contains("waterfalls", False)])

def SearchParksByFeature(a_data: DataFrame) -> None:
    """Display parks by feature put in by user.
    """
    feature: str = input("Feature: ").lower()
    
    if (a_data["Feature"].str.contains(feature, False)).any():
        print(a_data[a_data["Feature"].str.contains(feature, False)])
    else:
        print(f"There are no parks with the feature: {feature}.")

def ParksByStateCode(a_data: DataFrame) -> None:
    """Display parks by state code input by user.
    """
    print(a_data)
    stateCode: str = input("State Code: ").upper().strip()
    while stateCode not in a_data["State Codes"].values:
        stateCode = input("Valid states are Georgia, Maryland, North Carolina, South Carolina and Virginia:\nState Code: ").upper().strip()
    print(a_data[a_data["State Codes"] == stateCode])

def AggregateFunction(a_entry: str) -> str:
    """Burner function to return a result for aggregation.
    """
    return a_entry