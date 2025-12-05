from __future__ import annotations
from abc import ABC, abstractmethod


class InvalidStateError(Exception):
    """Custom exception for invalid state transitions."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.__message = message

    def __str__(self) -> str:
        return f"InvalidStateError: {self.__message}"


class State(ABC):
    """Abstract base class representing a Light Switch state."""

    def __init__(self, name: str) -> None:
        self._name = name

    def turn_on(self, light_switch):
        raise InvalidStateError("Cannot turn ON from current state.")

    def turn_off(self, light_switch):
        raise InvalidStateError("Cannot turn OFF from current state.")

    def dim(self, light_switch):
        raise InvalidStateError("Cannot DIM from current state.")

    def __str__(self):
        return self._name


class OffState(State):
    def __init__(self) -> None:
        super().__init__("OFF")

    def turn_on(self, light_switch):
        light_switch.state = OnState()
        print("Light is now ON.")


class OnState(State):
    def __init__(self) -> None:
        super().__init__("ON")

    def turn_off(self, light_switch):
        light_switch.state = OffState()
        print("Light is now OFF.")

    def dim(self, light_switch):
        light_switch.state = DimState()
        print("Light is now DIMMED.")


class DimState(State):
    def __init__(self) -> None:
        super().__init__("DIM")

    def turn_off(self, light_switch):
        light_switch.state = OffState()
        print("Light is now OFF.")

    def turn_on(self, light_switch):
        light_switch.state = OnState()
        print("Light is now ON.")


class LightSwitch:
    """Context class that maintains the current state."""

    def __init__(self) -> None:
        self.__state: State = OffState()

    @property
    def state(self) -> State:
        return self.__state

    @state.setter
    def state(self, state: State):
        self.__state = state
        print(f"[STATE] Current state → {state}")

    def turn_on(self):
        self.__state.turn_on(self)

    def turn_off(self):
        self.__state.turn_off(self)

    def dim(self):
        self.__state.dim(self)


def show_menu():
    print("\n====== LIGHT SWITCH MENU ======")
    print("1. Turn ON")
    print("2. Turn OFF")
    print("3. DIM")
    print("4. Exit")


def main():
    switch = LightSwitch()

    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1–4.")
            continue

        try:
            if choice == 1:
                switch.turn_on()
            elif choice == 2:
                switch.turn_off()
            elif choice == 3:
                switch.dim()
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Please choose a valid option (1–4).")
        except InvalidStateError as err:
            print(f"Action failed: {err}")


if __name__ == "__main__":
    main()