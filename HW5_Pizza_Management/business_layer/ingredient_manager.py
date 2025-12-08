# --- business_layer/ingredient_manager.py ---
from colorama import Fore, Style
from data_layer.csv_data_loader import CsvDataLoader


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
            line = name + ": " + str(stock) + " units left"
            if stock <= 5: # New low stock threshold for display
                print(Fore.YELLOW + line + " [URGENT RESTOCK]" + Style.RESET_ALL)
            else:
                print(line)