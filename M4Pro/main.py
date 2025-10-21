"""Placeholder since we have this and it's just not recognized."""

# Scrapes the books to scrape webpage and displays
#   information about the books gathered.
# 10/19/2025
# CSC221 M4Pro
# Daley Ottersbach

import time
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from functions import get_page_books


def main() -> None:
    """Main function.
    """
    # Step 1: Get Page
    df: DataFrame = get_page_books(1)
    for i in range(1, 3):
        time.sleep(0.1)
        df = pd.concat([df, get_page_books(1 + i)], ignore_index=True)

    # Step 2: Display
    print("="*81)
    print(df.head(10))
    print("="*81)

    print(f"Mean Price: ${round(df.Price.mean(), 2):.2f}")
    print(f"Mode Rating: {df.Rating.mode()[0]}")

    df.Rating.value_counts().plot.bar().plot()
    plt.show()

    # Step 3: Save
    df.to_csv('books_data.csv', index=False)
    print("\n✓ Data saved to 'books_data.csv'")


if __name__ == "__main__":
    main()
