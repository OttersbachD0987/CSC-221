# INSTRUCTIONS

1) Create a Python code file named M2Lab_Panda_DF_DaleyOttersbach.py
2) Add a title comment block to the top of the new Python file using the following form:

```Python
# A brief description of the project
# 9/8/2025
# CSC221 M2Lab– Panda DF
# Daley Ottersbach
```

3) Complete Instruction listed in Exercise 2 (S&P 500 Price Data) . Have the program display all the steps.  Display the title for the completed steps (as shown in textbook), the title is to be displayed before each set of results.

```text
For the following questions, the files sp500-constituents.csv and sp500-prices.csv are provided, which contain a list of stocks in the S&P 500 and certain data about each. For the constituent data, Symbol is a unique key column. For the prices data, Symbol and Date together uniquely define a row.

a) Use read_csv() to load two files, sp500-constituent.csv and sp500-prices.csv, each into their own DataFrame.
b) Rotate data: Transform the data organization for the price DataFrame, so prices for each date are each in their own dated column: for example, price-20201031, price-20200930, and so on.
c) Join data: Use join() to combine the constituents data and rotated price data from part (b) into one DataFrame. The resulting DataFrame should have one row for each row in the constituents data.
c) Augment data: Add a column that is the difference between the price on the last available date and the price on the prior available date.
d) Missing values: Determine which stocks do not have price data.
```
