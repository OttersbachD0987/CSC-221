# Load two files, pivot one, join to the other, augment the result by getting the difference between the two last available prices, and print missing values.
# 9/14/2025
# CSC221 M2Lab– Panda DF
# Daley Ottersbach

import functions
import pandas

def Main() -> None:
    """Runs the main loop of the program.
    """
    try:
        prices: pandas.DataFrame = pandas.read_csv("SP500_Adjusted_Prices.csv")
        constituents: pandas.DataFrame = pandas.read_csv("SP500_Constituents.csv", index_col="Symbol")
        print("Data frames loaded")
        print(prices)
        print(constituents)
        usePrices = prices.pivot(index="Symbol", columns="Date", values="Adjusted_price")
        print("Rotated prices")
        print(usePrices)
        merged = constituents.join(usePrices)
        print("Joined data")
        print(merged)

        # I don't like doing it like this.
        merged = functions.FindDifference(merged, usePrices)

        print("Added difference column")
        print(merged)
        
        missing = merged[merged.difference.isna()]
        print("Determined Missing Stocks")
        print(missing)
    except FileNotFoundError as e:
        print(f"The file {e.filename} does not exist.")

if __name__ == "__main__":
    Main()

#### Psuedocode
## Set prices to CSV Content of SP500_Adjusted_Prices.csv
## Set constituents to CSV Content of SP500_Constituents.csv with index column Symbol
## Display "Data frames loaded"
## Display prices
## Display constituents
## Set usePrices to prices pivoted with index symbol, columns Date, values Adjusted_price
## Display "Rotated prices"
## Display usePrices
## Set merged to constituents joined with usePrices
## Display "Joined data"
## Display merged
## Set merged to FindDifference with merged, usePrices
## Display "Added difference column"
## Display merged
## Set missing to merged boolean selection of difference column is NaN
## Display "Joined data"
## Display missing