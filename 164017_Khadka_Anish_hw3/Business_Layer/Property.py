from Business_Layer.Address import Address
from Business_Layer.Owner import Displayable

class Property(Displayable):
    def __init__(self,id_str: str,title: str,address: Address,price: float,sqft: int,bedrooms: int,owner_name: str="")->None:
        self.__id=id_str
        self.__title=title
        self.__address=address
        self.__price=price
        self.__sqft=sqft
        self.__bedrooms=bedrooms
        self.__owner_name=owner_name
        self.__interested_buyers: list=[]

    @property
    def id(self)->str:
        return self.__id

    @property
    def title(self)->str:
        return self.__title

    @property
    def address(self)->Address:
        return self.__address

    @property
    def price(self)->float:
        return self.__price

    @property
    def sqft(self)->int:
        return self.__sqft

    @property
    def bedrooms(self)->int:
        return self.__bedrooms

    @property
    def owner_name(self)->str:
        return self.__owner_name

    @owner_name.setter
    def owner_name(self,name: str)->None:
        self.__owner_name=name

    @property
    def interested_buyers(self)->list:
        return self.__interested_buyers

    def add_interested_buyer(self,buyer)->None:
        self.__interested_buyers.append(buyer)

    def remove_interested_buyer(self,buyer)->None:
        if buyer in self.__interested_buyers:
            self.__interested_buyers.remove(buyer)

    def display(self)->None:
        print(f"ID: {self.__id},Title: {self.__title},Price: {self.__price},Square Footage: {self.__sqft},Bedrooms: {self.__bedrooms}")
        if self.__owner_name:
            print(f"Owner: {self.__owner_name}")
        self.__address.display()
        print("Interested Buyers:")
        for buyer in self.__interested_buyers:
            buyer.display()

    def __str__(self)->str:
        addr_str=f"{self.__address.street},{self.__address.city},{self.__address.state},{self.__address.zipcode}"
        return f"{self.__id};{self.__title};{addr_str};{self.__price};{self.__sqft};{self.__bedrooms};{self.__owner_name}"