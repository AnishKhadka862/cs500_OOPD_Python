from colorama import Fore, Style
from data_layer.csv_data_loader import CsvDataLoader


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