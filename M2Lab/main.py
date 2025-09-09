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
    flunked = usePrices.transpose()

    bonk: dict[str, float|None]

    for col in usePrices:
        print(col)
        for row in usePrices.transpose():
            print(usePrices[col][row])
            bonk
    
    for col in merged:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", col) is not None:
            print("Exact Match")


if __name__ == "__main__":
    Main()
