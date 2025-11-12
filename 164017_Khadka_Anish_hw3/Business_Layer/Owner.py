from abc import ABC,abstractmethod

class Displayable(ABC):
    @abstractmethod
    def display(self)->None:
        pass

class Owner(Displayable):
    def __init__(self,first_name: str,last_name: str)->None:
        self.__first_name = first_name
        self.__last_name = last_name
        self.__properties: list = []

    @property
    def first_name(self)->str:
        return self.__first_name

    @property
    def last_name(self)->str:
        return self.__last_name

    @property
    def properties(self)->list:
        return self.__properties

    def add_property(self,property)->None:
        self.__properties.append(property)

    def remove_property(self,property)->None:
        if property in self.__properties:
            self.__properties.remove(property)

    def display(self)->None:
        print(f"Owner: {self.__first_name} {self.__last_name}")
        print("Properties:")
        for property in self.__properties:
            print(f"  - ID: {property.id},Title: {property.title}")

    def __str__(self)->str:
        return f"{self.__first_name} {self.__last_name}"