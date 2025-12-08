from colorama import Fore, Style


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
                        line = line + " + "
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