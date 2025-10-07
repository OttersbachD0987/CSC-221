from recipes import DessertRecipe, MainCourseRecipe, Recipe
from pandas import DataFrame, Series
from typing import Optional
    
def intput(a_prompt: str) -> int:
    """Get an int formated input.
    """
    try:
        return int(input(a_prompt))
    except Exception as e:
        #print(e)
        return intput(a_prompt)

def displayInstructions() -> None:
    """Display instructions for the menu.
    """
    print("1) View all recipes\n2) Search for a recipe by name\n3) Filter recipes by type (Dessert, Main Course, Vegetarian)\n4) Exit the program")

def printRow(a_row: Series) -> Series:
    """Print a recipe row.
    """
    if "Recipe" in a_row and isinstance(a_row["Recipe"], Recipe):
        a_row["Recipe"].display_recipe()
        print("-" * 60)
    return Series()

def viewAll(a_recipes: DataFrame) -> None:
    """Display all recipes in a dataframe.
    """
    print()
    a_recipes.apply(printRow, axis=1)

def search(a_recipes: DataFrame, a_name: str) -> Optional[DataFrame]:
    """Search for recipes that contain a string for the name.
    """
    a_name = a_name.lower()
    return a_recipes[(a_recipes["Name"].apply(lambda v: v.lower().find(a_name) != -1))]

def filterBy(a_recipes: DataFrame) -> Optional[DataFrame]:
    """Filter all recipes from 3 options or go back.
    """
    print("Choice of filter:\n1) Dessert\n2) Main Course\n3) Vegetarian\n4) Back\n")
    choice: int = -1
    while not 0 < choice <= 4:
        choice = intput("Choice: ")
        match choice:
            case 1:
                return a_recipes[(a_recipes["Type"] == "Dessert") & (a_recipes["Sweetness_Level"].notna())]
            case 2:
                return a_recipes[(a_recipes["Type"] == "Main Course") & (a_recipes["Spice_Level"].notna())]
            case 3:
                return a_recipes[(a_recipes["Is_Vegetarian"])]
            case 4:
                return None