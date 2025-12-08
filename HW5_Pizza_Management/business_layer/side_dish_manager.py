from colorama import Fore, Style
from data_layer.csv_data_loader import CsvDataLoader


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