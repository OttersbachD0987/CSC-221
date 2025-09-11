# INSTRUCTIONS

1.Create a Python code file named M2Pro1_Panda_DF_FirstLast.py
(replace "FirstLast" with your own name)
2. Add a title comment block to the top of the new Python file using the following form


# A brief description of the project
# Date
# CSC221 M2Pro1– Panda DF
# Your Name

 

Task 1: Add State Code (10 points)

You'll notice that the Excel sheet you downloaded has two sheets ( "east_coast_major_state_parks" and "us_states_code")

 

The data you're to analyze is referenced in the "east_coast_major_state_parks" sheet , you'll notice however that the "State" column refrences the name of the state. We want to add another column that references the State Code.

The reason we want to do that is because you will be required plot the output in one of the following modules and long names don't always look right on charts. 

What you'll need to do....

1. Read the content of the "east_coast_major_state_parks" sheet into a DataFrame. Make sure the DataFrame is assigned an appropriate name.

2. Add a column a "State code" column to the DataFrame you created, this column will reference the state code.

3. You'll notice that the "us_states_code" sheet references the state name AND code. So you'll want to use Python to find the matching State Code for each row, based on the value referenced under "State" column , and add the relevant state code for that row under the "State Code" column.

Task 2 Menu Options (70 points)

You are to create a menu driven program, see menu below

1. Display First 15 records in dataset
2. Get Number of record(parks) listed in dataset
3. Get Number of State Parks by State
4. Get Number of State Parks per Region
5. Get Top 2, by acreage, per Region
6. Get State Parks with Waterfalls by State
7. Search Parks by Feature
8. Allow to Search DataFrame by State Code
9. Exit

How the program should work?

The program is to automatically read the Excel file into a DataFrame upon execution and add the "State Code" column. It is then to display the menu shown above then ask the user to enter choice.

If user enters 1, the program is to display the first 15 rows of DataFrame that was created.

If user enters 2, the program is to display the number of records the DataFrame Contains ( shouldn't include header row)

If the user enters 3, the program is to display number of Parks per State ("Number of Parks" and "State Name"). Since the dataset references 5 states, the output should show 5 rows (one row for each state).

If the user enters 4, the program is to display number of Parks per Region ("Number of Parks" and "Region"). 

If the user enters 5, the program is to find the largest 2 parks in acreage in each state. 

The output should show "State Name", "Park Name" and "Acreage".
Output should be displayed in ascending order, first by state and then by acreage.
If the user enters 6, the program is to display list all the Parks that have waterfalls for each State. Output should show (State Name, County, Park Name, Feature)

If the user enters 7, ask the user to enter the feature they are looking for (for instance, waterfall, lake, cliffs, etc...)

The program is to convert what is entered to the right format.

Note that features in the dataset start with a capital letter. You are NOT to require the user to enter the feature in a certain format. Get the program to use string methods to change what the user enters to match. For example, if the first letter of the word(s) the enter is NOT capitalized, you will have to use a method that changes what the user enters to match.

List all parks that have the feature the user is looking for. Output should show (State Name, County, Park Name, Feature)
If feature is NOT found , notify the user.

If the user enters 8,ask the user to enter the state code (again, no restriction on format)

The program is to convert what is entered to the right format.

Get the program to use string methods to change what the user enters to match. For example, if the user entered "nc", use a method that changes what the user enters to convert what the user entered to capital letters.

If the user enters a valid state code, the program is to then display all state parks in the state the chose. Output should show (Park Name, Region, Acreage, Feature and State Code)
If and invalid state code is entered, for instance a state code for a state that is NOT referenced in the dataset, notify the user that the dataset only references parks in the following 5 states  (Georgia, Maryland, North Carolina, South Carolina and Virginia) and ask them to re-enter choice

If the user enters 9, the program should thank the user for using the program and then terminate

If the user makes an invalid choice (not a valid menu option), the program is to notify the user that they entered an invalid choice and display the menu again.

Important points to take note of (20 points)

The program is to display the menu after every operation and should only stop if the user enters 9.
Functions MUST be used (at least 2 custom functions must be created, the program must also have a main function) 
Program must be modularized
Exception handling Must be used
Write program Pseudocode (detail algorithm) and add it as a comment block to the submitted program.

While True is NOT to be used.  If submission doesn't comply, you will get a grade of "1"
