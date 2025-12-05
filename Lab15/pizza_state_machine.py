# Anish Khadka
# 164017
# Lab 15 Quiz
from __future__ import annotations
from state_machine import (State, Event, acts_as_state_machine,
                           before, after, InvalidStateTransition)
import random


@acts_as_state_machine
class OrderProcess:
    CheckOut = State(initial=True)
    SelectPizza = State()
    PlacedOrder = State()
    PreparingOrder = State()
    MakingPizza = State()
    ReadyForPickupOrder = State()
    CompletedOrder = State()

    select_pizza = Event(from_states=(CheckOut,), to_state=SelectPizza)
    check_ingredients = Event(from_states=(SelectPizza,), to_state=PlacedOrder)
    prepare_order = Event(from_states=(PlacedOrder,), to_state=PreparingOrder)
    make_pizza = Event(from_states=(PreparingOrder,), to_state=MakingPizza)
    pizza_baked = Event(from_states=(MakingPizza,), to_state=ReadyForPickupOrder)
    pick_up_order = Event(from_states=(ReadyForPickupOrder,), to_state=CompletedOrder)
    ready_for_new_order = Event(from_states=(CompletedOrder,), to_state=CheckOut)
    cancel_order = Event(from_states=(CheckOut, SelectPizza, PlacedOrder), to_state=CheckOut)

    def __init__(self, store: "PizzaStore") -> None:
        self.__store = store

    @before("select_pizza")
    def before_select(self) -> None:
        self.__store.choose_pizza()

    @after("select_pizza")
    def after_select(self) -> None:
        print("You have successfully selected your pizza.")

    @after("check_ingredients")
    def after_check(self) -> None:
        print("Ingredients confirmed. Order is now placed.")

    @after("prepare_order")
    def after_prepare(self) -> None:
        print("Getting the dough and toppings ready...")

    @after("make_pizza")
    def after_make(self) -> None:
        print("Pizza is being cooked in the oven...")

    @after("pizza_baked")
    def after_baked(self) -> None:
        print("Pizza is perfectly baked and waiting for pickup.")

    @after("pick_up_order")
    def after_pickup(self) -> None:
        print("The customer has collected the order.")

    @after("ready_for_new_order")
    def after_reset(self) -> None:
        print("System reset. Ready for a new order.")

    @after("cancel_order")
    def after_cancel(self) -> None:
        print("Order has been cancelled. Returning to checkout.")


class PizzaStore:
    def __init__(self) -> None:
        self.__process = OrderProcess(self)
        self.__inventory = {"Margherita": 15.0, "Pepperoni": 14.0, "Veggie": 12.0}
        self.__recipe_size = {"large": 2.0, "medium": 1.0, "small": 0.5}

    def choose_pizza(self) -> None:
        self.__type = input("Choose pizza type (Margherita, Pepperoni, Veggie): ")
        self.__size = input("Choose pizza size (large, medium, small): ")
        qty_text = input("Enter quantity: ")
        self.__qty = int(qty_text)

    def has_enough(self) -> bool:
        if self.__type not in self.__inventory or self.__size not in self.__recipe_size:
            return False
        required = self.__recipe_size[self.__size] * self.__qty
        return self.__inventory[self.__type] >= required

    def select_pizza(self) -> None:
        self.__process.select_pizza()

    def check_ingredients(self) -> None:
        if not self.has_enough():
            print("Sorry, not enough ingredients to fulfill this order.")
            return
        self.__process.check_ingredients()

    def prepare_order(self) -> None:
        if not self.has_enough():
            print("Inventory changed. Cannot prepare order now.")
            return
        required = self.__recipe_size[self.__size] * self.__qty
        self.__inventory[self.__type] -= required
        self.__process.prepare_order()

    def make_pizza(self) -> None:
        self.__process.make_pizza()

    def bake_pizza(self) -> None:
        outcome = random.randint(0, 9)
        if outcome > 1:
            print("Baking done. Pizza is ready!")
        else:
            print("Pizza slightly overcooked but acceptable.")
        self.__process.pizza_baked()

    def pick_up_order(self) -> None:
        self.__process.pick_up_order()

    def ready_for_next_order(self) -> None:
        self.__process.ready_for_new_order()

    def cancel_order(self) -> None:
        self.__process.cancel_order()

    def show_inventory(self) -> None:
        print("\nCurrent Inventory:")
        for key, val in self.__inventory.items():
            print(f"{key}: {val} lbs")
        print("------------------------")

    def get_current_state(self):
        return self.__process.current_state


def show_menu() -> None:
    print()
    print("======== MENU =========")
    print("1. Select Pizza")
    print("2. Check Ingredients")
    print("3. Prepare Order")
    print("4. Make Pizza")
    print("5. Bake Pizza")
    print("6. Pick Up Order")
    print("7. Ready for Next Order")
    print("8. Cancel Order")
    print("9. View Inventory")
    print("10. Exit")


def main() -> None:
    store = PizzaStore()
    while True:
        show_menu()
        choice_text = input("Enter choice number: ")
        try:
            choice = int(choice_text)
        except ValueError:
            print("Please enter a valid number.")
            continue

        try:
            if choice == 1:
                store.select_pizza()
            elif choice == 2:
                store.check_ingredients()
            elif choice == 3:
                store.prepare_order()
            elif choice == 4:
                store.make_pizza()
            elif choice == 5:
                store.bake_pizza()
            elif choice == 6:
                store.pick_up_order()
            elif choice == 7:
                store.ready_for_next_order()
            elif choice == 8:
                store.cancel_order()
            elif choice == 9:
                store.show_inventory()
            elif choice == 10:
                print("Exiting the system. See you next time!")
                break
            else:
                print("Invalid option, try again.")
        except InvalidStateTransition:
            print(f"Action not allowed in current state: {store.get_current_state()}")


if __name__ == "__main__":
    main()
