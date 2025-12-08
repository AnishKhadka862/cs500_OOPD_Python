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