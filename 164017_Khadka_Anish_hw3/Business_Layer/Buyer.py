from Business_Layer.Address import Address
from Business_Layer.Owner import Displayable

class Buyer(Displayable):
    def __init__(self, name: str, phone: str, email: str, address: Address)->None:
        self.__name = name
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.__interested_properties: list = []

    @property
    def name(self)->str:
        return self.__name

    @property
    def phone(self)->str:
        return self.__phone

    @property
    def email(self)->str:
        return self.__email

    @property
    def address(self)->Address:
        return self.__address

    @property
    def interested_properties(self)->list:
        return self.__interested_properties

    def add_interested_property(self, property)->None:
        self.__interested_properties.append(property)

    def remove_interested_property(self, property)->None:
        if property in self.__interested_properties:
            self.__interested_properties.remove(property)

    def display(self)->None:
        print(f"Buyer: {self.__name}, Phone: {self.__phone}, Email: {self.__email}")
        self.__address.display()
        print("Interested Properties:")
        for property in self.__interested_properties:
            property.display()

    def __str__(self)->str:
        return f"{self.__name}, {self.__phone}, {self.__email}, {self.__address}"