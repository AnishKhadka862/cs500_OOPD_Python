# Anish Khadka
# student ID: 164017
# Real Estate House Listing System with Observer Pattern
# Lab 11 Question 2

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Optional


# ------------------- Abstract Base Classes ------------------- #
class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify_observers(self, message: str) -> None:
        pass


# ------------------- Entity Classes ------------------- #
class House(Displayable):
    def __init__(self, address: str, square_feet: int, num_rooms: int, price: float, city: str):
        self.__address = address
        self.__square_feet = square_feet
        self.__num_rooms = num_rooms
        self.__price = price
        self.__city = city

    @property
    def address(self) -> str:
        return self.__address

    @property
    def price(self) -> float:
        return self.__price

    def set_price(self, new_price: float) -> None:
        self.__price = new_price

    def __eq__(self, value: object) -> bool:
        if isinstance(value, House):
            return self.__address == value.__address
        return False

    def __str__(self) -> str:
        return f'Address = {self.__address}, Square Feet = {self.__square_feet}, Number of Rooms = {self.__num_rooms}, Price = {self.__price}'

    def display(self) -> None:
        print(self.__str__())


class Contact(Displayable, Observer):
    def __init__(self, lastname: str, firstname: str, phone_number: str, email: str):
        self._lastname = lastname
        self._firstname = firstname
        self._phone_number = phone_number
        self._email = email

    @property
    def lastname(self) -> str:
        return self._lastname

    @property
    def firstname(self) -> str:
        return self._firstname

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @property
    def email(self) -> str:
        return self._email

    def update(self, message: str) -> None:
        print(f"Notification to {self._firstname} {self._lastname}: {message}")

    def __str__(self) -> str:
        return f'Last Name = {self._lastname}, First Name = {self._firstname}, Phone Number = {self._phone_number}, Email = {self._email}'

    def display(self) -> None:
        print(self.__str__())


class Owner(Contact):
    def __init__(self, lastname: str, firstname: str, phone_number: str, email: str):
        super().__init__(lastname, firstname, phone_number, email)
        self.__houses: List[House] = []

    def add_house(self, house: House) -> None:
        if house not in self.__houses:
            self.__houses.append(house)

    def remove_house(self, house: House) -> None:
        if house in self.__houses:
            self.__houses.remove(house)

    def display(self) -> None:
        print(f'{super().__str__()}')
        print('Owns the following houses:')
        for house in self.__houses:
            house.display()


class Buyer(Contact):
    def __init__(self, lastname: str, firstname: str, phone_number: str, email: str):
        super().__init__(lastname, firstname, phone_number, email)
        self.__watch_list: List[House] = []

    @property
    def watch_list(self) -> List[House]:
        return self.__watch_list

    def save_to_watchlist(self, house: House) -> None:
        if house not in self.__watch_list:
            self.__watch_list.append(house)

    def remove_from_watchlist(self, house: House) -> None:
        if house in self.__watch_list:
            self.__watch_list.remove(house)

    def __str__(self) -> str:
        output = super().__str__() + '\nWatching the following houses:\n'
        for house in self.__watch_list:
            output += str(house) + '\n'
        return output.strip()

    def display(self) -> None:
        print(self.__str__())


class Company(Displayable, Subject):
    def __init__(self, companyName: str):
        self.__companyName = companyName
        self.__owners: List[Owner] = []
        self.__buyers: List[Buyer] = []
        self.__agents: List[Agent] = []
        self.__houses: List[House] = []
        self.__observers: List[Observer] = []

    # -------- Subject interface -------- #
    def register_observer(self, observer: Observer) -> None:
        if observer not in self.__observers:
            self.__observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        if observer in self.__observers:
            self.__observers.remove(observer)

    def notify_observers(self, message: str) -> None:
        for observer in self.__observers:
            observer.update(message)

    # -------- Company-specific methods -------- #
    def add_owner(self, owner: Owner) -> None:
        if owner not in self.__owners:
            self.__owners.append(owner)
            self.register_observer(owner)

    def add_buyer(self, buyer: Buyer) -> None:
        if buyer not in self.__buyers:
            self.__buyers.append(buyer)
            self.register_observer(buyer)

    def add_agent(self, agent: Agent) -> None:
        if agent not in self.__agents:
            self.__agents.append(agent)
            self.register_observer(agent)

    def add_house_to_listing(self, house: House, owner: Owner) -> None:
        if house not in self.__houses:
            self.__houses.append(house)
            msg = f"New house added to listing: {house.address}"
            self.notify_observers(msg)

    def get_house_by_address(self, address: str) -> Optional[House]:
        for house in self.__houses:
            if house.address == address:
                return house
        return None

    def remove_house_from_listing(self, house: House, owner: Owner) -> None:
        if house in self.__houses:
            self.__houses.remove(house)
            msg = f"House removed from listing: {house.address}"
            self.notify_observers(msg)

    def update_house_price(self, house: House, new_price: float, owner: Owner) -> None:
        house.set_price(new_price)
        msg = f"Price updated for house {house.address}: new price is {new_price}"
        self.notify_observers(msg)

    def display(self) -> None:
        print(f'Company Name = {self.__companyName}')
        print('=========================== The list of agents: ==============================')
        for agent in self.__agents:
            agent.display()
        print('=========================== The house listing: ===============================')
        for house in self.__houses:
            house.display()
        print('=========================== The list of owners: ==============================')
        for owner in self.__owners:
            owner.display()
        print('=========================== The list of buyers: ==============================')
        for buyer in self.__buyers:
            buyer.display()


class Agent(Contact):
    def __init__(self, lastname: str, firstname: str, phone_number: str, email: str, position: str, company: Company):
        super().__init__(lastname, firstname, phone_number, email)
        self.__position = position
        self.__company = company

    def add_house_to_listing_for_owner(self, owner: Owner, house: House) -> None:
        owner.add_house(house)
        self.__company.add_owner(owner)
        self.__company.add_house_to_listing(house, owner)

    def help_buyer_to_save_to_watchlist(self, buyer: Buyer, house: House) -> None:
        buyer.save_to_watchlist(house)
        self.__company.add_buyer(buyer)

    def edit_house_price(self, address: str, new_price: float) -> None:
        house = self.__company.get_house_by_address(address)
        if house:
            self.__company.update_house_price(house, new_price, None) # type: ignore

    def sold_house(self, house: House, owner: Owner) -> None:
        self.__company.remove_house_from_listing(house, owner)

    def __str__(self) -> str:
        return f'Last Name = {self.lastname}, First Name = {self.firstname}, Phone Number = {self.phone_number}, Email = {self.email}\nPosition = {self.__position}'

    def display(self) -> None:
        print(self.__str__())


# ------------------- MAIN ------------------- #
def main() -> None:
    company = Company("Good Future Real Estate")
    agent1 = Agent("Henderson", "Dave", "408-777-3333", "dave@yahoo.com", "Senior Agent", company)
    company.add_agent(agent1)

    owner1 = Owner("Li", "Peter", "510-111-2222", "peter@yahoo.com")
    owner2 = Owner("Buck", "Carl", "408-111-2222", "carl@yahoo.com")

    house1 = House("1111 Mission Blvd", 1000, 2, 1000000, "Fremont")
    house2 = House("2222 Mission Blvd", 2000, 3, 1200000, "San Jose")

    agent1.add_house_to_listing_for_owner(owner1, house1)
    agent1.add_house_to_listing_for_owner(owner2, house2)

    buyer1 = Buyer("Buke", "Tom", "408-555-2222", "tom@yahoo.com")
    buyer2 = Buyer("Go", "Lily", "510-222-3333", "lily@yahoo.com")
    company.add_buyer(buyer1)
    company.add_buyer(buyer2)

    agent1.help_buyer_to_save_to_watchlist(buyer1, house1)
    agent1.help_buyer_to_save_to_watchlist(buyer2, house2)

    # Update price
    agent1.edit_house_price("2222 Mission Blvd", 1300000)

    # Sell house
    agent1.sold_house(house1, owner1)

    company.display()


if __name__ == "__main__":
    main()
