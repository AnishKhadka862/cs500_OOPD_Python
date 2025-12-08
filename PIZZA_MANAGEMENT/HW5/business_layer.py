from colorama import Fore, Style
from data_layer import CsvDataLoader

class IngredientManager:
    def __init__(self):
        self.__inventory = {}

    def load_inventory(self, file_path):
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
        print(Fore.GREEN + "Ingredient inventory loaded." + Style.RESET_ALL)

    def consume_ingredients(self, ingredients):
        i = 0
        while i < len(ingredients):
            ing = ingredients[i]
            if ing in self.__inventory:
                self.__inventory[ing] = self.__inventory[ing] - 1
                if self.__inventory[ing] <= 5:
                    print(
                        Fore.YELLOW
                        + "LOW STOCK: "
                        + ing
                        + " ("
                        + str(self.__inventory[ing])
                        + ")"
                        + Style.RESET_ALL
                    )
            else:
                print(
                    Fore.RED
                    + "Ingredient not found in inventory: "
                    + ing
                    + Style.RESET_ALL
                )
            i = i + 1

    def return_ingredients(self, ingredients):
        i = 0
        while i < len(ingredients):
            ing = ingredients[i]
            if ing in self.__inventory:
                self.__inventory[ing] = self.__inventory[ing] + 1
            i = i + 1

    def display_inventory(self):
        print("\n" + Fore.CYAN + "INGREDIENT INVENTORY" + Style.RESET_ALL)
        for name in self.__inventory:
            stock = self.__inventory[name]
            line = name + ": " + str(stock) + " units"
            if stock <= 10:
                print(Fore.YELLOW + line + " (LOW)" + Style.RESET_ALL)
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

        print(Fore.GREEN + "Pizza recipes loaded." + Style.RESET_ALL)

    def get_menu(self):
        return self.__recipes

    def add_recipe(self, name, category, ingredients, price):
        if name in self.__recipes:
            print(
                Fore.RED
                + "Recipe already exists: "
                + name
                + Style.RESET_ALL
            )
            return

        recipe = PizzaRecipe(name, category, ingredients, price)
        self.__recipes[name] = recipe
        self.__ingredient_manager.consume_ingredients(ingredients)
        print(Fore.GREEN + "Recipe added: " + name + Style.RESET_ALL)

    def edit_recipe(self, name, new_category, new_ingredients, new_price):
        if name not in self.__recipes:
            print(
                Fore.RED
                + "Recipe not found: "
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

        print(Fore.GREEN + "Recipe updated: " + name + Style.RESET_ALL)

    def delete_recipe(self, name):
        if name not in self.__recipes:
            print(
                Fore.RED
                + "Recipe not found: "
                + name
                + Style.RESET_ALL
            )
            return

        recipe = self.__recipes[name]
        ingredients = recipe.get_ingredients()
        self.__ingredient_manager.return_ingredients(ingredients)
        del self.__recipes[name]
        print(Fore.GREEN + "Recipe deleted: " + name + Style.RESET_ALL)

    def categorize_recipes(self):
        categories = []
        for recipe_name in self.__recipes:
            recipe = self.__recipes[recipe_name]
            cat = recipe.get_category()
            if cat not in categories:
                categories.append(cat)

        print("\n" + Fore.CYAN + "RECIPE CATEGORIES" + Style.RESET_ALL)
        i = 0
        while i < len(categories):
            print("- " + categories[i])
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
                + "No recipes found for keyword: "
                + keyword
                + Style.RESET_ALL
            )
            return

        print(
            "\n"
            + Fore.CYAN
            + "Found "
            + str(len(found))
            + " recipe(s):"
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
                    line = line + ", "
                j = j + 1
            print(
                "- "
                + recipe.get_name()
                + " | Category: "
                + recipe.get_category()
                + " | Price: $"
                + str(recipe.get_price())
            )
            print("  Ingredients: " + line)
            i = i + 1

class StandardMenuManager:
    def __init__(self):
        self.__standard_menu = {}

    def load_menu(self, file_path):
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

        print(Fore.GREEN + "Standard pizza menu loaded." + Style.RESET_ALL)

    def display_menu(self):
        print("\n" + Fore.CYAN + "STANDARD PIZZA MENU" + Style.RESET_ALL)
        for name in self.__standard_menu:
            item = self.__standard_menu[name]
            print("Name: " + name)
            print("Description: " + item["Description"])
            print("Price: $" + str(item["Price"]))
            print("")

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

        print(Fore.GREEN + "Customizable ingredients loaded." + Style.RESET_ALL)

    def __select_single(self, title, options):
        print("\n" + title + ":")
        names = list(options.keys())
        i = 0
        while i < len(names):
            item_name = names[i]
            print(
                str(i + 1)
                + ". "
                + item_name
                + " - $"
                + str(options[item_name])
            )
            i = i + 1

        while True:
            choice = input("Enter number: ").strip()
            if choice.isdigit():
                number = int(choice)
                if number >= 1 and number <= len(names):
                    name = names[number - 1]
                    self.__selected[name] = options[name]
                    break
            print(Fore.RED + "Invalid choice." + Style.RESET_ALL)

    def __select_multiple(self, title, options):
        print("\n" + title + ":")
        names = list(options.keys())
        i = 0
        while i < len(names):
            item_name = names[i]
            print(
                str(i + 1)
                + ". "
                + item_name
                + " - $"
                + str(options[item_name])
            )
            i = i + 1

        indices = []

        while True:
            raw = input(
                "Enter numbers separated by commas (0 to skip): "
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
                print(Fore.RED + "No valid numbers." + Style.RESET_ALL)

        k = 0
        while k < len(indices):
            index_num = indices[k]
            name = names[index_num - 1]
            self.__selected[name] = options[name]
            k = k + 1

    def customize_pizza(self):
        self.__selected = {}

        if len(self.__pizza_bases) > 0:
            self.__select_single("Choose Pizza Base", self.__pizza_bases)

        if len(self.__sauces) > 0:
            self.__select_single("Choose Sauce", self.__sauces)

        if len(self.__toppings) > 0:
            self.__select_multiple("Choose Toppings", self.__toppings)

        if len(self.__extras) > 0:
            self.__select_multiple(
                "Choose Additional Ingredients", self.__extras
            )

        print(Fore.GREEN + "Pizza customization completed." + Style.RESET_ALL)

    def display_order_summary(self):
        print("\n" + Fore.CYAN + "CUSTOMIZED PIZZA SUMMARY" + Style.RESET_ALL)
        total = 0.0
        for name in self.__selected:
            price = self.__selected[name]
            print("- " + name + ": $" + str(price))
            total = total + price
        print("Total Price: $" + str(total))

    def get_selected_ingredients(self):
        return self.__selected

class SideDishManager:
    def __init__(self):
        self.__side_dishes = {}

    def load_menu(self, file_path):
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

        print(Fore.GREEN + "Side dish menu loaded." + Style.RESET_ALL)

    def display_menu(self):
        print("\n" + Fore.CYAN + "SIDE DISH MENU" + Style.RESET_ALL)
        for name in self.__side_dishes:
            item = self.__side_dishes[name]
            print("Name: " + name)
            print("Description: " + item["Description"])
            print("Type: " + item["Type"])
            print("Price: $" + str(item["Price"]))
            print("")

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
        order = {
            "Standard": [],
            "Custom": [],
            "Sides": [],
        }

        print("\n" + Fore.MAGENTA + "PROCESSING ORDER" + Style.RESET_ALL)

        self.__add_standard_pizzas(order)
        self.__add_custom_pizza(order)
        self.__add_sides(order)
        self.__display_summary(order)

        self.__orders.append(order)
        print(Fore.GREEN + "Order processed." + Style.RESET_ALL)

    def __add_standard_pizzas(self, order):
        menu = self.__standard_menu_manager.get_menu()
        names = list(menu.keys())

        while True:
            print("\n" + Fore.BLUE + "Standard Pizzas:" + Style.RESET_ALL)
            i = 0
            while i < len(names):
                nm = names[i]
                price = menu[nm]["Price"]
                print(str(i + 1) + ". " + nm + " - $" + str(price))
                i = i + 1

            choice = input(
                "Enter pizza number to add (0 to finish): "
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
                        Fore.GREEN
                        + "Added standard pizza: "
                        + pizza_name
                        + Style.RESET_ALL
                    )
                else:
                    print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid input." + Style.RESET_ALL)

    def __add_custom_pizza(self, order):
        selected = self.__customized_pizza_order.get_selected_ingredients()
        if len(selected) == 0:
            return

        total = 0.0
        ingredients = []
        for name in selected:
            price = selected[name]
            total = total + price
            ingredients.append(name)

        self.__ingredient_manager.consume_ingredients(ingredients)
        order["Custom"].append({"Ingredients": selected, "Price": total})

    def __add_sides(self, order):
        menu = self.__side_dish_manager.get_menu()
        names = list(menu.keys())

        while True:
            print("\n" + Fore.BLUE + "Side Dishes:" + Style.RESET_ALL)
            i = 0
            while i < len(names):
                nm = names[i]
                price = menu[nm]["Price"]
                print(str(i + 1) + ". " + nm + " - $" + str(price))
                i = i + 1

            choice = input(
                "Enter side dish number to add (0 to finish): "
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
                        Fore.GREEN
                        + "Added side dish: "
                        + dish_name
                        + Style.RESET_ALL
                    )
                else:
                    print(Fore.RED + "Invalid choice." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Invalid input." + Style.RESET_ALL)

    def __display_summary(self, order):
        print("\n" + Fore.YELLOW + "ORDER SUMMARY" + Style.RESET_ALL)

        total = 0.0

        if len(order["Standard"]) > 0:
            print("\nStandard Pizzas:")
            i = 0
            while i < len(order["Standard"]):
                item = order["Standard"][i]
                print("- " + item["Name"] + " : $" + str(item["Price"]))
                total = total + item["Price"]
                i = i + 1

        if len(order["Custom"]) > 0:
            print("\nCustomized Pizzas:")
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
                        line = line + ", "
                    k = k + 1
                print("- Custom Pizza (" + line + ") : $" + str(custom["Price"]))
                total = total + custom["Price"]
                j = j + 1

        if len(order["Sides"]) > 0:
            print("\nSide Dishes:")
            m = 0
            while m < len(order["Sides"]):
                item = order["Sides"][m]
                print("- " + item["Name"] + " : $" + str(item["Price"]))
                total = total + item["Price"]
                m = m + 1

        print("\nTOTAL PRICE: $" + str(total))
