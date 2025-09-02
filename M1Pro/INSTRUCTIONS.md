## Introduction:

Assignment requires creating functions, lists, and formatting strings

## Instructions:

### Part 1:60 points

1. Under Chapter 9, complete Exercise 2(Country Statistics-Multiple Measures).

```text
Assume a program begins with the statement:

allData = {
  'US': {'pop':325.7, 'gdp': 19.39, 'ccy': 'USD', 'fx': 1.0},
  'CA': {'pop': 36.5, 'gdp': 1.65, 'ccy': 'CAD', 'fx': 1.35},
  'MX': {'pop':129.2, 'gdp': 1.15, 'ccy': 'MXN', 'fx': 19.68}
}

Write subsequent statements that (in a loop) prompt the user for a country code (US, CA, or MX), then prompt for a measure name (pop, gdp, ccy, or fx), then look up in the above dictionary for the corresponding value, and display that value. Example run:

Please enter a country code: CA
Please enter a statistic: pop
CA pop = 36.5
Your program should handle the cases where a user-entered country code or measure name is not found.
```

There are specific requirements that this assignment MUST meet, see below:
  - Use string methods to convert user input to the appropriate format (upper or lower case)
  - The program should handle cases where a user-entered country code or measure that is not found.

### Part 2: 30 points

2. Enhance the program so that it continues to run and only stops if the user were to enter the word stop instead of Country Code (requires using sentinel).
- If the user enters "stop", it doesn't matter if upper or lower, the program is to stop WITHOUT asking for statistics to be entered.

3. Submit your finished code solution file(s) through the assignment link posted below this instruction post

## Grading criteria:

Program Pseudocode (detailed algorithm) required
Remember (Custom functions must always have docstrings
Program MUST be modularized (2 code files)
while True is NOT to be used.
