"""Contains the functions for the program."""

import requests
from requests import Response
from bs4 import BeautifulSoup
from pandas import DataFrame

CONVERSIONS: dict[str, int] = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
URL: str = "https://books.toscrape.com/catalogue/page-{}.html"


def get_page_books(a_index: int) -> DataFrame:
    """Get the information of the books in the page of a catalogue.

    Args:
        a_index (int): The index of the catalogue.

    Returns:
        DataFrame: The extracted books information.
    """
    # Step 1: Fetch the webpage
    response: Response = requests.get(URL.format(a_index), timeout=10)

    # Check if request was successful
    if response.status_code != 200:
        print(f"✗ Error: Status code {response.status_code}")
        return DataFrame()

    print("✓ Successfully fetched the webpage!")

    # Step 2: Create DataFrame
    return DataFrame([{
        'Title': book.h3.a["title"],
        'Price': float(book.find(attrs={"class": "price_color"}).text[1::]),
        'Rating':
            (rating := CONVERSIONS[
                (clz := book.p["class"])[clz.index("star-rating") + 1]
            ]),
        'Highly Rated': rating >= 4,
    } for book in BeautifulSoup(response.content, 'html.parser')
        .find_all(attrs={"class": "product_pod"})])
