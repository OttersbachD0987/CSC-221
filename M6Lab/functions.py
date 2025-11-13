from pandas import DataFrame
from matplotlib import pyplot
import pandas

def DisplayMenu() -> None:
    """Displays the menu.
    """
    print("1. Display First 15 records in dataset\n2. Get Number of record(parks) listed in dataset\n3. Get Number of State Parks by State\n4. Get Number of State Parks per Region\n5. Get Top 2, by acreage, per Region\n6. Get State Parks with Waterfalls by State\n7. Search Parks by Feature\n8. Allow to Search DataFrame by State Code\n9. Exit")

def DisplayTopRecords(a_data: DataFrame) -> None:
    """Display the top records of a dataframe.
    """
    print(a_data.head(15))
    _, ax = pyplot.subplots()
    a_data.head(15).plot(kind="bar", ax=ax, title="Top 15 Parks", legend=True)
    #ax.legend(["# Of Parks"])
    pyplot.savefig("top_records.png")
    pyplot.show()

def NumberOfParks(a_data: DataFrame) -> None:
    """Display the number of parks in a dataframe.
    """
    print(f"Number of Parks: {a_data.count()["park name"]}")

def NumberOfParksByState(a_data: DataFrame) -> None:
    """Display the number of parks by state.
    """
    print("\n".join([f"{state}: {parkCount}" for state, parkCount in a_data.pivot(values=["park name"], columns=["park name"], index=["state"]).count(axis=1).items()]))
    _, ax = pyplot.subplots()
    a_data.pivot(values=["park name"], columns=["park name"], index=["state"]).count(axis=1).plot(kind="bar", ax=ax, title="Parks By State", legend=True, xlabel="State", ylabel="# Of Parks")
    ax.legend(["# Of Parks"])
    pyplot.savefig("parks_by_state.png")
    pyplot.show()

def NumberOfParksByRegion(a_data: DataFrame) -> None:
    """Display the number of parks by region.
    """
    print("\n".join([f"{region}: {parkCount}" for region, parkCount in a_data.pivot(values=["park name"], columns=["park name"], index=["Region"]).count(axis=1).items()]))
    _, ax = pyplot.subplots()
    a_data.pivot(values=["park name"], columns=["park name"], index=["Region"]).count(axis=1).plot(kind="bar", ax=ax, title="Parks By Region", legend=True, xlabel="Region", ylabel="# Of Parks")
    ax.legend(["# Of Parks"])
    pyplot.savefig("parks_by_region.png")
    pyplot.show()

def TopParksByAcreagePerRegion(a_data: DataFrame) -> None:
    """Display the top two parks by acerage per region.
    """
    counter1 = 0
    counter2 = 0
    t: DataFrame = DataFrame(index=["acreage"])
    p: list[list[str]] = []
    for region in a_data["Region"].unique():
        counter1+=1
        p.append([])
        print(datable := a_data[a_data["Region"] == region].sort_values("acreage").head(2)[["Region", "acreage", "park name"]])
        for a in datable.values:
            counter2+=1
            p[-1].append(name := "".join(str(b) for b in a.tolist() if not isinstance(b, int)))
            print(name)
            print(t)
            print(DataFrame({name: a[1]}, index=["acreage"]))
            t = t.join(DataFrame({name: a[1]}, index=["acreage"]), how="outer")
    print(p)
    print(t)
    
    print(counter1)
    print(counter2)
    print([tuple(e) for e in p])
    print(t.columns)
    fig, ax = pyplot.subplots()
    t.plot(y="acreage", kind="bar", ax=ax, sharex=True, sharey=True, layout=(1, len(a_data["Region"].unique())), title="Parks By Region", legend=True, subplots=[tuple(e) for e in p])
    #ax.legend(["# Of Parks"])
    pyplot.savefig("parks_by_acreage_by_region.png")
    pyplot.show()

def StateParksWithWaterfallsByState(a_data: DataFrame) -> None:
    """Display state parks with waterfalls by states.
    """
    print(a_data[a_data["Feature"].str.contains("waterfalls", False)])
    _, ax = pyplot.subplots()
    a_data[a_data["Feature"].str.contains("waterfalls", False)].pivot(values=["park name"], columns="park name", index="state").count(axis=1).plot(kind="bar", ax=ax, title="Parks With Waterfalls", legend=True, xlabel="State", ylabel="# Of Parks")
    ax.legend(["# Of Parks"])
    pyplot.savefig("parks_with_waterfalls.png")
    pyplot.show()

def SearchParksByFeature(a_data: DataFrame) -> None:
    """Display parks by feature put in by user.
    """
    feature: str = input("Feature: ").lower()
    
    if (a_data["Feature"].str.contains(feature, False)).any():
        print(a_data[a_data["Feature"].str.contains(feature, False)])
        _, ax = pyplot.subplots()
        a_data[a_data["Feature"].str.contains(feature, False)].pivot(values=["park name"], columns="park name", index="state").count(axis=1).plot(kind="bar", ax=ax, title=f"Parks By {feature.title()}", legend=True, xlabel="State", ylabel="# Of Parks")
        #ax.legend(["# Of Parks"])
        pyplot.savefig(f"parks_by_{feature}.png")
        pyplot.show()
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
    _, ax = pyplot.subplots()
    a_data[a_data["State Codes"] == stateCode].plot(kind="bar", ax=ax, title="Parks By State Code", legend=True)
    #ax.legend(["# Of Parks"])
    pyplot.savefig("parks_by_state_code.png")
    pyplot.show()

def AggregateFunction(a_entry: str) -> str:
    """Burner function to return a result for aggregation.
    """
    return a_entry