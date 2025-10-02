from typing import override

# pylint: disable=line-too-long, trailing-whitespace

class Recipe:
    def __init__(self, a_name: str, a_ingredients: list[str], a_steps: list[str], a_isVegetarian: bool) -> None:
        """.

        Args:
            a_name (str): The name of the recipe.
            a_ingredients (list[str]): The ingredients in the recipe.
            a_steps (list[str]): The steps in the recipe.
            a_isVegetarian (bool): Whether or not the recipe is vegetarian.
        """
        self.__name: str = a_name
        self.__ingredients: list[str] = a_ingredients
        self.__steps: list[str] = a_steps
        self.__is_vegetarian: bool = a_isVegetarian

    def get_name(self) -> str:
        """Get the name of the recipe.

        Returns:
            str: The name of the recipe.
        """
        return self.__name

    def set_name(self, a_name: str) -> None:
        """Set the name of the recipe.

        Args:
            a_name (str): The new name of the recipe.
        """
        self.__name = a_name
        
    def get_ingredients(self) -> list[str]:
        """Get the ingredients of the recipe.

        Returns:
            list[str]: The ingredients of the recipe.
        """
        return self.__ingredients.copy()

    def set_ingredients(self, a_ingredients: list[str]) -> None:
        """Set the ingredients of the recipe.

        Args:
            a_ingredients (list[str]): The new ingredients of the recipe.
        """
        self.__ingredients = a_ingredients
        
    def get_steps(self) -> list[str]:
        """Get the steps of the recipe.

        Returns:
            list[str]: The steps of the recipe.
        """
        return self.__steps

    def set_steps(self, a_steps: list[str]) -> None:
        """Set the steps of the recipe.

        Args:
            a_steps (list[str]): The new steps of the recipe.
        """
        self.__steps = a_steps.copy()
        
    def get_is_vegetarian(self) -> bool:
        """Get whether the recipe is vegetarian.

        Returns:
            bool: Whether the recipe is vegetarian.
        """
        return self.__is_vegetarian

    def set_is_vegetarian(self, a_isVegetarian: bool) -> None:
        """Set whether the recipe is vegetarian.

        Args:
            a_isVegetarian (bool): Whether the recipe is vegetarian.
        """
        self.__is_vegetarian = a_isVegetarian
    
    def display_recipe(self) -> None:
        """Prints the recipe information using the print statement.
        """
        print(f"{self.__name}\nVegetarian: {self.__is_vegetarian}\nIngredients: ({self.__ingredients})\nSteps:\n{"\n".join(f"{i + 1}" for i, step in enumerate(self.__steps))}")

class DessertRecipe(Recipe):
    def __init__(self, a_name: str, a_ingredients: list[str], a_steps: list[str], a_isVegetarian: bool, a_sweetnessLevel: int) -> None:
        """.

        Args:
            a_name (str): The name of the recipe.
            a_ingredients (list[str]): The ingredients in the recipe.
            a_steps (list[str]): The steps in the recipe.
            a_isVegetarian (bool): Whether or not the recipe is vegetarian.
            a_sweetnessLevel (int): The sweetness level of the recipe between 1-10.
        """
        super().__init__(a_name, a_ingredients, a_steps, a_isVegetarian)
        self.__sweetness_level: int = a_sweetnessLevel
    
    def get_sweetness_level(self) -> int:
        """Get the sweetness level of the recipe between 1-10.

        Returns:
            int: The sweetness level of the recipe between 1-10.
        """
        return self.__sweetness_level

    def set_sweetness_level(self, a_sweetnessLevel: int) -> None:
        """Set the sweetness level of the recipe between 1-10.

        Args:
            a_sweetnessLevel (int): The new sweetness level of the recipe between 1-10.
        """
        self.__sweetness_level = a_sweetnessLevel
    
    @override
    def display_recipe(self) -> None:
        """Prints the recipe information using the print statement.
        """
        print(f"{self.__name}\nVegetarian: {self.__is_vegetarian}\nSweetness Level: {self.__sweetness_level}\nIngredients: ({self.__ingredients})\nSteps:\n{"\n".join(f"{i + 1}" for i, step in enumerate(self.__steps))}")

class MainCourseRecipe(Recipe):
    def __init__(self, a_name: str, a_ingredients: list[str], a_steps: list[str], a_isVegetarian: bool, a_spiceLevel: int) -> None:
        """.

        Args:
            a_name (str): The name of the recipe.
            a_ingredients (list[str]): The ingredients in the recipe.
            a_steps (list[str]): The steps in the recipe.
            a_isVegetarian (bool): Whether or not the recipe is vegetarian.
            a_spiceLevel (int): The spice level of the recipe between 1-5.
        """
        super().__init__(a_name, a_ingredients, a_steps, a_isVegetarian)
        self.__spice_level: int = a_spiceLevel
    
    def get_spice_level(self) -> int:
        """Get the spice level of the recipe between 1-5.

        Returns:
            int: The spice level of the recipe between 1-5.
        """
        return self.__spice_level

    def set_spice_level(self, a_spiceLevel: int) -> None:
        """Set the spice level of the recipe between 1-5.

        Args:
            a_spiceLevel (int): The new spice level of the recipe between 1-5.
        """
        self.__spice_level = a_spiceLevel
    
    @override
    def display_recipe(self) -> None:
        """Prints the recipe information using the print statement.
        """
        print(
            f"{self.__name}\nVegetarian: {self.__is_vegetarian}\nSpice Level: {self.__spice_level}\nIngredients: ({self.__ingredients})\nSteps:\n{"\n".join(f"{i + 1}" for i, step in enumerate(self.__steps))}")