
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
        self.__ingredient_manager = IngredientManager()
        self.__pizza_manager = PizzaManager(self.__ingredient_manager)
        self.__standard_menu_manager = StandardMenuManager()
        self.__custom_order = CustomizedPizzaOrder()
        self.__side_dish_manager = SideDishManager()
        self.__order_processor = None

    def initialize(self):
        self.__ingredient_manager.load_inventory(
            "Dataset/ingredient_inventory.csv"
        )
        self.__pizza_manager.load_dataset("Dataset/pizza_dataset.csv")
        self.__standard_menu_manager.load_menu("Dataset/standard_menu.csv")
        self.__custom_order.load_ingredients(
            "Dataset/customizable_ingredients.csv"
        )
        self.__side_dish_manager.load_menu("Dataset/side_dish_menu.csv")

        self.__order_processor = OrderProcessor(
            self.__pizza_manager,
            self.__standard_menu_manager,
            self.__custom_order,
            self.__side_dish_manager,
            self.__ingredient_manager,
        )

    def run(self):
        while True:
            print("\n" + Fore.MAGENTA + "Main Menu:" + Style.RESET_ALL)
            print("1. Add Recipe")
            print("2. Edit Recipe")
            print("3. Delete Recipe")
            print("4. Categorize Recipes")
            print("5. Search Recipe")
            print("6. Display Ingredient Inventory")
            print("7. Display Standard Pizza Menu")
            print("8. Customize Pizza Order")
            print("9. Display Side Dish Menu")
            print("10. Process Order")
            print("11. Exit")

            choice = input("Enter your choice (1-11): ").strip()

            if choice == "1":
                self.__add_recipe_ui()
            elif choice == "2":
                self.__edit_recipe_ui()
            elif choice == "3":
                self.__delete_recipe_ui()
            elif choice == "4":
                self.__pizza_manager.categorize_recipes()
            elif choice == "5":
                keyword = input("Enter search keyword: ").strip()
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
                    self.__order_processor = OrderProcessor(
                        self.__pizza_manager,
                        self.__standard_menu_manager,
                        self.__custom_order,
                        self.__side_dish_manager,
                        self.__ingredient_manager,
                    )
                self.__order_processor.process_order()
            elif choice == "11":
                print(Fore.MAGENTA + "Exiting system. Goodbye!" + Style.RESET_ALL)
                break
            else:
                print(Fore.RED + "Invalid choice." + Style.RESET_ALL)

    def __add_recipe_ui(self):
        name = input("Enter new recipe name: ").strip()
        category = input("Enter category: ").strip()
        ingredients_text = input("Enter ingredients (comma-separated): ").strip()

        ingredients = []
        parts = ingredients_text.split(",")
        i = 0
        while i < len(parts):
            part = parts[i].strip()
            if part != "":
                ingredients.append(part)
            i = i + 1

        price_input = input("Enter price: ").strip()
        try:
            price = float(price_input)
        except ValueError:
            print(Fore.RED + "Invalid price." + Style.RESET_ALL)
            return

        self.__pizza_manager.add_recipe(name, category, ingredients, price)

    def __edit_recipe_ui(self):
        name = input("Enter recipe name to edit: ").strip()
        new_category = input(
            "Enter new category (leave blank to keep): "
        ).strip()
        category_value = new_category if new_category != "" else None

        ing_text = input(
            "Enter new ingredients (comma-separated, blank to keep): "
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

        price_text = input("Enter new price (blank to keep): ").strip()
        price_value = None
        if price_text != "":
            try:
                price_value = float(price_text)
            except ValueError:
                print(Fore.RED + "Invalid price." + Style.RESET_ALL)
                return

        self.__pizza_manager.edit_recipe(
            name, category_value, new_ingredients, price_value
        )

    def __delete_recipe_ui(self):
        name = input("Enter recipe name to delete: ").strip()
        self.__pizza_manager.delete_recipe(name)


def main():
    app = PizzaStoreApp()
    app.initialize()
    app.run()


if __name__ == "__main__":
    main()

