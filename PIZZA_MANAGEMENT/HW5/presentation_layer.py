from colorama import Fore, Style, init

from business_layer import (
    IngredientManager,
    PizzaManager,
    StandardMenuManager,
    CustomizedPizzaOrder,
    SideDishManager,
    OrderProcessor,
)

init(autoreset=True)


class PizzaStoreApp:
    def __init__(self):
        # Initialize all required business layer components
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
            print("\n" + Fore.CYAN + "PIZZA MANAGEMENT SYSTEM" + Style.RESET_ALL)
            print("1. Create New Pizza Recipe")
            print("2. Update Existing Recipe Details")
            print("3. Remove Recipe from Catalog")
            print("4. Review Recipe Categories")
            print("5. Lookup Recipe by Term")
            print("6. View Kitchen Stock Levels")
            print("7. Display Fixed Menu Items")
            print("8. Start Custom Pizza Build")
            print("9. Show Available Sides/Extras")
            print("10. Finalize Customer Transaction")
            print("11. Shut Down Application")

            choice = input(Fore.YELLOW + "Enter your function number (1-11): " + Style.RESET_ALL).strip()

            if choice == "1":
                self.__add_recipe_ui()
            elif choice == "2":
                self.__edit_recipe_ui()
            elif choice == "3":
                self.__delete_recipe_ui()
            elif choice == "4":
                self.__pizza_manager.categorize_recipes()
            elif choice == "5":
                keyword = input("Type a keyword for searching recipes: ").strip()
                self.__pizza_manager.search_recipe(keyword)
            elif choice == "6":
                self.__ingredient_manager.display_inventory()
            elif choice == "7":
                self.__standard_menu_manager.display_menu()
            elif choice == "8":
                self.__custom_order.customize_pizza()
                self.__custom_order.display_order_summary()
            elif choice == "9":
                self.__side_dish_manager.display_menu()
            elif choice == "10":
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