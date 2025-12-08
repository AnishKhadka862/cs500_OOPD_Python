from colorama import Fore, Style
from data_layer.csv_data_loader import CsvDataLoader


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