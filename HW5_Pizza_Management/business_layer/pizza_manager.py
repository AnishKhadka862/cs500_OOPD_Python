from colorama import Fore, Style
from data_layer.csv_data_loader import CsvDataLoader
from .pizza_recipe import PizzaRecipe


class PizzaManager:
    def __init__(self, ingredient_manager):
        self.__recipes = {}
        self.__ingredient_manager = ingredient_manager

    def load_dataset(self, file_path):
        """Loads all base pizza recipes from a file."""
        rows = CsvDataLoader.load_rows(file_path)
        index = 0
        while index < len(rows):
            row = rows[index]
            name = row.get("Name", "").strip()
            category = row.get("Category", "").strip()
            ing_text = row.get("Ingredients", "")
            ingredients = []

            parts = ing_text.split(",")
            j = 0
            while j < len(parts):
                part = parts[j].strip()
                if part != "":
                    ingredients.append(part)
                j = j + 1

            price_text = row.get("Price", "0").strip()
            try:
                price_value = float(price_text)
            except ValueError:
                price_value = 0.0

            if name != "":
                recipe = PizzaRecipe(name, category, ingredients, price_value)
                self.__recipes[name] = recipe

            index = index + 1

        print(Fore.LIGHTGREEN_EX + "Pizza recipe catalog synchronized." + Style.RESET_ALL)

    def get_menu(self):
        return self.__recipes

    def add_recipe(self, name, category, ingredients, price):
        if name in self.__recipes:
            print(
                Fore.RED
                + "Error: A recipe with this name already exists in the catalog: "
                + name
                + Style.RESET_ALL
            )
            return

        recipe = PizzaRecipe(name, category, ingredients, price)
        self.__recipes[name] = recipe
        self.__ingredient_manager.consume_ingredients(ingredients)
        print(Fore.LIGHTGREEN_EX + "Successfully saved new recipe: " + name + Style.RESET_ALL)

    def edit_recipe(self, name, new_category, new_ingredients, new_price):
        if name not in self.__recipes:
            print(
                Fore.RED
                + "Update failed. Recipe not found in the system: "
                + name
                + Style.RESET_ALL
            )
            return

        recipe = self.__recipes[name]

        if new_ingredients is not None:
            old_ingredients = recipe.get_ingredients()
            self.__ingredient_manager.return_ingredients(old_ingredients)
            self.__ingredient_manager.consume_ingredients(new_ingredients)
            recipe.set_ingredients(new_ingredients)

        if new_category is not None and new_category != "":
            recipe.set_category(new_category)

        if new_price is not None:
            recipe.set_price(new_price)

        print(Fore.LIGHTGREEN_EX + "Recipe parameters updated for: " + name + Style.RESET_ALL)

    def delete_recipe(self, name):
        if name not in self.__recipes:
            print(
                Fore.RED
                + "Deletion failed. Recipe not found: "
                + name
                + Style.RESET_ALL
            )
            return

        recipe = self.__recipes[name]
        ingredients = recipe.get_ingredients()
        self.__ingredient_manager.return_ingredients(ingredients)
        del self.__recipes[name]
        print(Fore.LIGHTGREEN_EX + "Recipe permanently removed from the catalog: " + name + Style.RESET_ALL)

    def categorize_recipes(self):
        categories = []
        for recipe_name in self.__recipes:
            recipe = self.__recipes[recipe_name]
            cat = recipe.get_category()
            if cat not in categories:
                categories.append(cat)

        print("\n" + Fore.BLUE + "--- PIZZA CLASSIFICATIONS ---" + Style.RESET_ALL)
        i = 0
        while i < len(categories):
            print(">> " + categories[i])
            i = i + 1

    def search_recipe(self, keyword):
        keyword_lower = keyword.lower()
        found = []
        for name in self.__recipes:
            if keyword_lower in name.lower():
                found.append(self.__recipes[name])

        if len(found) == 0:
            print(
                Fore.YELLOW
                + "No matching recipes located for search term: "
                + keyword
                + Style.RESET_ALL
            )
            return

        print(
            "\n"
            + Fore.BLUE
            + "Found "
            + str(len(found))
            + " matching entry(s) in the catalog:"
            + Style.RESET_ALL
        )
        i = 0
        while i < len(found):
            recipe = found[i]
            ing_list = recipe.get_ingredients()
            line = ""
            j = 0
            while j < len(ing_list):
                line = line + ing_list[j]
                if j != len(ing_list) - 1:
                    line = line + " / "
                j = j + 1
            print(
                "--- "
                + recipe.get_name()
                + " | Group: "
                + recipe.get_category()
                + " | Price: $"
                + str(f"{recipe.get_price():.2f}")
            )
            print("  Required Components: " + line)
            i = i + 1