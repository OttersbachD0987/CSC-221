import csv
import pandas


def ReadCSV(a_filepath: str) -> None:
    with open(a_filepath, "r") as csvFile:
        reader: csv.DictReader = csv.DictReader(csvFile)
