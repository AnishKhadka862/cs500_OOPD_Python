from colorama import Fore, Style
from data_layer import CsvDataLoader # Assuming this is in data_layer.py

class IngredientManager:
    def __init__(self):
        self.__inventory = {}

    def load_inventory(self, file_path):
        """Pulls ingredient inventory data from a source file."""
        rows = CsvDataLoader.load_rows(file_path)
        index = 0
        while index < len(rows):
            row = rows[index]
            name = row.get("Ingredient", "").strip()
            stock_text = row.get("Stock", "0").strip()
            if name != "":
                try:
                    stock_value = int(stock_text)
                except ValueError:
                    stock_value = 0
                self.__inventory[name] = stock_value
            index = index + 1
        print(Fore.LIGHTGREEN_EX + "Inventory check complete. All ingredients loaded." + Style.RESET_ALL)

    def consume_ingredients(self, ingredients):
        """Reduces the stock count for each ingredient used in an order."""
        i = 0
        while i < len(ingredients):
            ing = ingredients[i]
            if ing in self.__inventory:
                self.__inventory[ing] = self.__inventory[ing] - 1
                # Different low stock threshold and message
                if self.__inventory[ing] <= 2:
                    print(
                        Fore.RED
                        + "ALERT: "
                        + ing
                        + " stock is critically low ("
                        + str(self.__inventory[ing])
                        + " units remaining!)"
                        + Style.RESET_ALL
                    )
            else:
                print(
                    Fore.MAGENTA
                    + "Warning: Ingredient not recognized in stock system: "
                    + ing
                    + Style.RESET_ALL
                )
            i = i + 1

    def return_ingredients(self, ingredients):
        """Restores stock, typically after a recipe modification or deletion."""
        i = 0
        while i < len(ingredients):
            ing = ingredients[i]
            if ing in self.__inventory:
                self.__inventory[ing] = self.__inventory[ing] + 1
            i = i + 1

    def display_inventory(self):
        """Outputs the current status of all ingredients in stock."""
        print("\n" + Fore.BLUE + "--- CURRENT KITCHEN STOCK ---" + Style.RESET_ALL)
        for name in self.__inventory:
            stock = self.__inventory[name]
            line = name + ": " + str(stock) + " units on hand"
            if stock <= 5: # New low stock threshold for display
                print(Fore.YELLOW + line + " [URGENT RESTOCK]" + Style.RESET_ALL)
            else:
                print(line)

class PizzaRecipe:
    def __init__(self, name, category, ingredients, price):
        self.__name = name
        self.__category = category
        self.__ingredients = ingredients
        self.__price = price

    def get_name(self):
        return self.__name

    def get_category(self):
        return self.__category

    def get_ingredients(self):
        return self.__ingredients

    def get_price(self):
        return self.__price

    def set_category(self, category):
        self.__category = category

    def set_ingredients(self, ingredients):
        self.__ingredients = ingredients

    def set_price(self, price):
        self.__price = price


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
            print(">> " + categories[i]) # Changed bullet point to '>>'
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
                    line = line + " / " # Changed separator
                j = j + 1
            print(
                "--- "
                + recipe.get_name()
                + " | Group: "
                + recipe.get_category()
                + " | Price: $"
                + str(f"{recipe.get_price():.2f}") # Added formatting
            )
            print("  Required Components: " + line)
            i = i + 1

class StandardMenuManager:
    def __init__(self):
        self.__standard_menu = {}

    def load_menu(self, file_path):
        """Loads fixed items that are ready-to-order."""
        rows = CsvDataLoader.load_rows(file_path)
        index = 0
        while index < len(rows):
            row = rows[index]
            name = row.get("Name", "").strip()
            desc = row.get("Description", "").strip()
            price_text = row.get("Price", "0").strip()

            try:
                price_value = float(price_text)
            except ValueError:
                price_value = 0.0

            if name != "":
                self.__standard_menu[name] = {
                    "Description": desc,
                    "Price": price_value,
                }

            index = index + 1

        print(Fore.LIGHTGREEN_EX + "Standard fixed menu successfully retrieved." + Style.RESET_ALL)

    def display_menu(self):
        """Shows the list of standard pizzas available."""
        print("\n" + Fore.BLUE + "--- House Specialty Pizzas ---" + Style.RESET_ALL)
        for name in self.__standard_menu:
            item = self.__standard_menu[name]
            print(Fore.YELLOW + "Item Name: " + name + Style.RESET_ALL)
            print("Details: " + item["Description"])
            print("Price Tag: $" + str(f"{item['Price']:.2f}"))
            print("--------------------")

    def get_menu(self):
        return self.__standard_menu

class CustomizedPizzaOrder:
    def __init__(self):
        self.__pizza_bases = {}
        self.__sauces = {}
        self.__toppings = {}
        self.__extras = {}
        self.__selected = {}

    def load_ingredients(self, file_path):
        """Loads all components available for customer customization."""
        rows = CsvDataLoader.load_rows(file_path)
        index = 0
        while index < len(rows):
            row = rows[index]
            category = row.get("Category", "").strip()
            name = row.get("Name", "").strip()
            price_text = row.get("Price", "0").strip()

            try:
                price_value = float(price_text)
            except ValueError:
                price_value = 0.0

            if category == "Pizza Base":
                self.__pizza_bases[name] = price_value
            elif category == "Sauce":
                self.__sauces[name] = price_value
            elif category == "Topping":
                self.__toppings[name] = price_value
            elif category == "Additional Ingredient":
                self.__extras[name] = price_value

            index = index + 1

        print(Fore.LIGHTGREEN_EX + "Custom build ingredients are ready." + Style.RESET_ALL)

    def __select_single(self, title, options):
        """Helper for selecting one item from a list of options."""
        print("\n" + Fore.MAGENTA + f"--- {title} Selection ---" + Style.RESET_ALL)
        names = list(options.keys())
        i = 0
        while i < len(names):
            item_name = names[i]
            print(
                str(i + 1)
                + ". "
                + item_name
                + " (Cost: $"
                + str(f"{options[item_name]:.2f}") + ")"
            )
            i = i + 1

        while True:
            choice = input("Enter the corresponding number: ").strip()
            if choice.isdigit():
                number = int(choice)
                if number >= 1 and number <= len(names):
                    name = names[number - 1]
                    self.__selected[name] = options[name]
                    break
            print(Fore.RED + "Invalid number entered. Please try again." + Style.RESET_ALL)

    def __select_multiple(self, title, options):
        """Helper for selecting multiple items from a list of options."""
        print("\n" + Fore.MAGENTA + f"--- {title} Selection (Multiple Allowed) ---" + Style.RESET_ALL)
        names = list(options.keys())
        i = 0
        while i < len(names):
            item_name = names[i]
            print(
                str(i + 1)
                + ". "
                + item_name
                + " (Cost: $"
                + str(f"{options[item_name]:.2f}") + ")"
            )
            i = i + 1

        indices = []

        while True:
            raw = input(
                "Enter item numbers, separated by commas (Type 0 to complete): "
            ).strip()
            if raw == "0":
                break

            parts = raw.split(",")
            valid_found = False
            j = 0
            while j < len(parts):
                part = parts[j].strip()
                if part.isdigit():
                    number = int(part)
                    if number >= 1 and number <= len(names):
                        if number not in indices:
                            indices.append(number)
                        valid_found = True
                j = j + 1

            if valid_found:
                break
            else:
                print(Fore.RED + "No valid item numbers were detected in your input." + Style.RESET_ALL)

        k = 0
        while k < len(indices):
            index_num = indices[k]
            name = names[index_num - 1]
            self.__selected[name] = options[name]
            k = k + 1

    def customize_pizza(self):
        """Main method to guide the user through building a custom pizza."""
        self.__selected = {}

        if len(self.__pizza_bases) > 0:
            self.__select_single("Pizza Base", self.__pizza_bases)

        if len(self.__sauces) > 0:
            self.__select_single("Sauce Type", self.__sauces)

        if len(self.__toppings) > 0:
            self.__select_multiple("Main Toppings", self.__toppings)

        if len(self.__extras) > 0:
            self.__select_multiple(
                "Extra Flavorings/Ingredients", self.__extras
            )

        print(Fore.LIGHTGREEN_EX + "Custom pizza finished. Proceeding to summary." + Style.RESET_ALL)

    def display_order_summary(self):
        """Prints a list of selected custom components and the total cost."""
        print("\n" + Fore.BLUE + "--- CUSTOM PIZZA BREAKDOWN ---" + Style.RESET_ALL)
        total = 0.0
        for name in self.__selected:
            price = self.__selected[name]
            print(f"* {name} (item cost): ${price:.2f}")
            total = total + price
        print(Fore.YELLOW + f"Total Custom Price: ${total:.2f}" + Style.RESET_ALL)

    def get_selected_ingredients(self):
        return self.__selected

class SideDishManager:
    def __init__(self):
        self.__side_dishes = {}

    def load_menu(self, file_path):
        """Loads data for side dishes and extra items."""
        rows = CsvDataLoader.load_rows(file_path)
        index = 0
        while index < len(rows):
            row = rows[index]
            name = row.get("Name", "").strip()
            description = row.get("Description", "").strip()
            dish_type = row.get("Type", "").strip()
            price_text = row.get("Price", "0").strip()

            try:
                price_value = float(price_text)
            except ValueError:
                price_value = 0.0

            if name != "":
                self.__side_dishes[name] = {
                    "Description": description,
                    "Type": dish_type,
                    "Price": price_value,
                }

            index = index + 1

        print(Fore.LIGHTGREEN_EX + "Side dish menu successfully configured." + Style.RESET_ALL)

    def display_menu(self):
        """Outputs the complete menu of side dishes."""
        print("\n" + Fore.BLUE + "--- SIDES AND EXTRAS MENU ---" + Style.RESET_ALL)
        for name in self.__side_dishes:
            item = self.__side_dishes[name]
            print(f"** {name} **")
            print(f"Description: {item['Description']}")
            print(f"Classification: {item['Type']}")
            print(f"Retail Price: ${item['Price']:.2f}")
            print("--------------------")

    def get_menu(self):
        return self.__side_dishes

class OrderProcessor:
    def __init__(
        self,
        pizza_manager,
        standard_menu_manager,
        customized_pizza_order,
        side_dish_manager,
        ingredient_manager,
    ):
        self.__pizza_manager = pizza_manager
        self.__standard_menu_manager = standard_menu_manager
        self.__customized_pizza_order = customized_pizza_order
        self.__side_dish_manager = side_dish_manager
        self.__ingredient_manager = ingredient_manager
        self.__orders = []

    def process_order(self):
        """Coordinates the creation and fulfillment of a new customer order."""
        order = {
            "Standard": [],
            "Custom": [],
            "Sides": [],
        }

        print("\n" + Fore.CYAN + "--- INITIATING NEW CUSTOMER ORDER ---" + Style.RESET_ALL)

        self.__add_standard_pizzas(order)
        self.__add_custom_pizza(order)
        self.__add_sides(order)
        self.__display_summary(order)

        self.__orders.append(order)
        print(Fore.LIGHTGREEN_EX + "Order successfully completed and logged." + Style.RESET_ALL)

    def __add_standard_pizzas(self, order):
        menu = self.__standard_menu_manager.get_menu()
        names = list(menu.keys())

        while True:
            print("\n" + Fore.MAGENTA + "Standard Fixed Pizzas Available:" + Style.RESET_ALL)
            i = 0
            while i < len(names):
                nm = names[i]
                price = menu[nm]["Price"]
                print(f"{i + 1}. {nm} - Listed at ${price:.2f}")
                i = i + 1

            choice = input(
                "Enter item number to add to order (0 to proceed to next step): "
            ).strip()

            if choice == "0":
                break

            if choice.isdigit():
                number = int(choice)
                if number >= 1 and number <= len(names):
                    pizza_name = names[number - 1]
                    price = menu[pizza_name]["Price"]

                    recipe_dict = self.__pizza_manager.get_menu()
                    if pizza_name in recipe_dict:
                        recipe = recipe_dict[pizza_name]
                        ingredients = recipe.get_ingredients()
                        self.__ingredient_manager.consume_ingredients(
                            ingredients
                        )

                    order["Standard"].append(
                        {"Name": pizza_name, "Price": price}
                    )
                    print(
                        Fore.YELLOW
                        + "Fixed item added: "
                        + pizza_name
                        + Style.RESET_ALL
                    )
                else:
                    print(Fore.RED + "Selection is out of range." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)

    def __add_custom_pizza(self, order):
        selected = self.__customized_pizza_order.get_selected_ingredients()
        if len(selected) == 0:
            print(Fore.YELLOW + "Note: No custom pizza was configured for this order." + Style.RESET_ALL)
            return

        total = 0.0
        ingredients = []
        for name in selected:
            price = selected[name]
            total = total + price
            ingredients.append(name)

        self.__ingredient_manager.consume_ingredients(ingredients)
        order["Custom"].append({"Ingredients": selected, "Price": total})
        print(Fore.LIGHTGREEN_EX + "Custom pizza successfully added to order ticket." + Style.RESET_ALL)

    def __add_sides(self, order):
        menu = self.__side_dish_manager.get_menu()
        names = list(menu.keys())

        while True:
            print("\n" + Fore.MAGENTA + "Side Dishes and Extras Available:" + Style.RESET_ALL)
            i = 0
            while i < len(names):
                nm = names[i]
                price = menu[nm]["Price"]
                print(f"{i + 1}. {nm} - ${price:.2f}")
                i = i + 1

            choice = input(
                "Enter number of extra item to purchase (0 to finish order preparation): "
            ).strip()

            if choice == "0":
                break

            if choice.isdigit():
                number = int(choice)
                if number >= 1 and number <= len(names):
                    dish_name = names[number - 1]
                    price = menu[dish_name]["Price"]
                    order["Sides"].append(
                        {"Name": dish_name, "Price": price}
                    )
                    print(
                        Fore.YELLOW
                        + "Extra item recorded: "
                        + dish_name
                        + Style.RESET_ALL
                    )
                else:
                    print(Fore.RED + "Selection is out of range." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)

    def __display_summary(self, order):
        """Generates the final receipt for the customer."""
        print("\n" + Fore.RED + "--- FINAL ORDER RECEIPT ---" + Style.RESET_ALL)

        total = 0.0

        if len(order["Standard"]) > 0:
            print("\n** Fixed Pizzas **")
            i = 0
            while i < len(order["Standard"]):
                item = order["Standard"][i]
                print(f"- {item['Name']} : ${item['Price']:.2f}")
                total = total + item["Price"]
                i = i + 1

        if len(order["Custom"]) > 0:
            print("\n** Custom Creations **")
            j = 0
            while j < len(order["Custom"]):
                custom = order["Custom"][j]
                ing_dict = custom["Ingredients"]
                names = list(ing_dict.keys())
                line = ""
                k = 0
                while k < len(names):
                    line = line + names[k]
                    if k != len(names) - 1:
                        line = line + " + " # Changed separator
                    k = k + 1
                print(f"- Custom Build ({line}) : ${custom['Price']:.2f}")
                total = total + custom["Price"]
                j = j + 1

        if len(order["Sides"]) > 0:
            print("\n** Sides & Extras **")
            m = 0
            while m < len(order["Sides"]):
                item = order["Sides"][m]
                print(f"- {item['Name']} : ${item['Price']:.2f}")
                total = total + item["Price"]
                m = m + 1

        print(Fore.RED + "\nGRAND TOTAL PAYABLE: $" + str(f"{total:.2f}") + Style.RESET_ALL)