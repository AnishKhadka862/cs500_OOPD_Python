# HW5 Pizza Management System
# Anish Khadka, 164017
# Samir Ghimire, 164061
# CS 500 - Object Oriented Programming in Python
from colorama import Fore, Style, init

from business_layer.ingredient_manager import IngredientManager
from business_layer.pizza_manager import PizzaManager
from business_layer.standard_menu_manager import StandardMenuManager
from business_layer.customized_pizza_order import CustomizedPizzaOrder
from business_layer.side_dish_manager import SideDishManager
from business_layer.order_processor import OrderProcessor

init(autoreset=True)


class PizzaStoreApp:
    def __init__(self):
        self.__ingredient_manager = IngredientManager()
        self.__pizza_manager = PizzaManager(self.__ingredient_manager)
        self.__standard_menu_manager = StandardMenuManager()
        self.__custom_order = CustomizedPizzaOrder()
        self.__side_dish_manager = SideDishManager()
        self.__order_processor = None

    def initialize(self):
        # Loading all system data from source files
        self.__ingredient_manager.load_inventory(
            "Dataset/ingredient_inventory.csv"
        )
        self.__pizza_manager.load_dataset("Dataset/pizza_dataset.csv")
        self.__standard_menu_manager.load_menu("Dataset/standard_menu.csv")
        self.__custom_order.load_ingredients(
            "Dataset/customizable_ingredients.csv"
        )
        self.__side_dish_manager.load_menu("Dataset/side_dish_menu.csv")

        # Set up the order processing unit
        self.__order_processor = OrderProcessor(
            self.__pizza_manager,
            self.__standard_menu_manager,
            self.__custom_order,
            self.__side_dish_manager,
            self.__ingredient_manager,
        )

    def run(self):
        # Start the main interactive application loop
        while True:
            print("\n" + Fore.CYAN + "=====PIZZA MANAGEMENT SYSTEM=====" + Style.RESET_ALL)
            
            # (Customer/Sales Flow)
            print("1. Process Customer Order")
            print("2. Display House Menu Options")
            print("3. Start Create Your Own Pizza")
            print("4. Show Side Dish Menu")

            # (Recipe/Data Management)
            print("5. Create New Pizza Recipe")
            print("6. Update Existing Recipe Details")
            print("7. Remove Recipe from Catalog")
            print("8. Lookup Recipe by Term")
            print("9. Review Recipe Categories")
            
            # STATUS/UTILITY
            print("10. View Kitchen Stock")
            print("11. close Application")

            choice = input(Fore.YELLOW + "Enter your function number (1-11): " + Style.RESET_ALL).strip()

            # --- MAPPED ACTIONS ---
            if choice == "1":
                if self.__order_processor is None:
                    # Re-instantiate if necessary (safety check)
                    self.__order_processor = OrderProcessor(
                        self.__pizza_manager,
                        self.__standard_menu_manager,
                        self.__custom_order,
                        self.__side_dish_manager,
                        self.__ingredient_manager,
                    )
                self.__order_processor.process_order()
            elif choice == "2":
                self.__standard_menu_manager.display_menu()
            elif choice == "3":
                self.__custom_order.customize_pizza()
                self.__custom_order.display_order_summary()
            elif choice == "4":
                self.__side_dish_manager.display_menu()
            elif choice == "5":
                self.__add_recipe_ui()
            elif choice == "6":
                self.__edit_recipe_ui()
            elif choice == "7":
                self.__delete_recipe_ui()
            elif choice == "8":
                keyword = input("Type a keyword for searching recipes: ").strip()
                self.__pizza_manager.search_recipe(keyword)
            elif choice == "9":
                self.__pizza_manager.categorize_recipes()
            elif choice == "10":
                self.__ingredient_manager.display_inventory()
            elif choice == "11":
                print(Fore.CYAN + "System logoff successful. Have a productive day!" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Selection not recognized. Please use a number from the list." + Style.RESET_ALL)


    def __add_recipe_ui(self):
        """User input sequence for adding a new recipe."""
        name = input("Enter the full name for the new recipe: ").strip()
        category = input("Enter the pizza category (e.g., 'Gourmet', 'Classic'): ").strip()
        ingredients_text = input("List ingredients (separate each with a comma): ").strip()

        # Processing the comma-separated ingredients list
        ingredients = []
        parts = ingredients_text.split(",")
        i = 0
        while i < len(parts):
            part = parts[i].strip()
            if part != "":
                ingredients.append(part)
            i = i + 1

        price_input = input("Enter the sale price (e.g., 15.99): ").strip()
        try:
            price = float(price_input)
        except ValueError:
            print(Fore.RED + "Error: Price must be a valid number. Recipe creation failed." + Style.RESET_ALL)
            return

        self.__pizza_manager.add_recipe(name, category, ingredients, price)


    def __edit_recipe_ui(self):
        """User input sequence for modifying an existing recipe."""
        name = input("Enter the exact recipe name to modify: ").strip()
        new_category = input(
            "New category (leave blank to keep current): "
        ).strip()
        category_value = new_category if new_category != "" else None

        ing_text = input(
            "New ingredients list (comma-separated, blank to keep current): "
        ).strip()
        new_ingredients = None
        if ing_text != "":
            new_ingredients = []
            parts = ing_text.split(",")
            i = 0
            while i < len(parts):
                part = parts[i].strip()
                if part != "":
                    new_ingredients.append(part)
                i = i + 1

        price_text = input("New price (leave blank to keep current): ").strip()
        price_value = None
        if price_text != "":
            try:
                price_value = float(price_text)
            except ValueError:
                print(Fore.RED + "Error: Price must be a valid number. Update aborted." + Style.RESET_ALL)
                return

        self.__pizza_manager.edit_recipe(
            name, category_value, new_ingredients, price_value
        )


    def __delete_recipe_ui(self):
        """User input sequence for removing a recipe."""
        name = input("Enter the exact recipe name to delete permanently: ").strip()
        self.__pizza_manager.delete_recipe(name)


def main():
    app = PizzaStoreApp()
    app.initialize()
    app.run()


if __name__ == "__main__":
    main()