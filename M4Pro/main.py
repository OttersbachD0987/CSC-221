# A brief description of the project
# 10/7/2025
# CSC221 M4Pro
# Daley Ottersbach

import requests
from requests import Response
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame

CONVERSIONS: dict[str, int] = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
URL: str = "http://books.toscrape.com/"

def main() -> None:
    # Step 1: Fetch the webpage
    response: Response = requests.get(URL)

    # Check if request was successful
    if response.status_code != 200:
        print(f"✗ Error: Status code {response.status_code}")
        exit()

    print("✓ Successfully fetched the webpage!")

    # Step 2: Create DataFrame
    df: DataFrame = DataFrame([{
        'Title': book.h3.a["title"],
        'Price': float(book.find(attrs={"class": "price_color"}).text[1::]),
        'Rating': CONVERSIONS[book.p["class"][book.p["class"].index("star-rating") + 1]],
        'Highly Rated': CONVERSIONS[book.p["class"][book.p["class"].index("star-rating") + 1]] >= 4,
    } for book in BeautifulSoup(response.content, 'html.parser').find_all(attrs={"class": "product_pod"})])
    
    mean_price: float = round(df.Price.mean(), 2)
    mode_rating: int = df.Rating.mode()[0]
    print(f"{mean_price}")
    print(f"{mode_rating}")
    
    pd.

    # Step 3: Display and save
    print(df.head(10))
    df.to_csv('books_data.csv', index=False)
    print("\n✓ Data saved to 'books_data.csv'")

if __name__ == "__main__":
    main()