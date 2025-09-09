# A brief description of the project
# 9/8/2025
# CSC221 M2Lab– Panda DF
# Daley Ottersbach

import functions
import pandas
import re


def Main() -> None:
    prices: pandas.DataFrame = pandas.read_csv("SP500_Adjusted_Prices.csv")
    constituents: pandas.DataFrame = pandas.read_csv("SP500_Constituents.csv", index_col="Symbol")
    print("Data frames loaded")
    usePrices = prices.pivot(index="Symbol", columns="Date", values="Adjusted_price")
    print("Rotated prices")
    merged = constituents.join(usePrices)
    print("Joined data")

    bonk: dict[str, list[float]] = {}

    for row in merged.transpose():
        for col in usePrices:
            bonk[row] = bonk.get(row, []) + ([usePrices[col][row]] if row in usePrices[col] and isinstance(usePrices[col][row], float) else [])
        merged.


if __name__ == "__main__":
    Main()
