import functions
import pandas
import re


def Main() -> None:
    prices: pandas.DataFrame = pandas.read_csv("SP500_Adjusted_Prices.csv")
    constituents: pandas.DataFrame = pandas.read_csv(
        "SP500_Constituents.csv", index_col="Symbol"
    )
    usePrices = prices.pivot(index="Symbol", columns="Date", values="Adjusted_price")
    print(usePrices)
    merged = constituents.join(usePrices)
    print(merged)
    for col in merged:
        print(col)
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", col) is not None:
            print("Exact Match")
            print(merged[col])
            print(merged[merged[col].isna()])


if __name__ == "__main__":
    Main()
