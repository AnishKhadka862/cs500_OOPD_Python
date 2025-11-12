class Address:
    def __init__(self,street:str,city:str,state:str,zipcode:str)->None:
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode

    @property
    def street(self)->str:
        return self.__street

    @property
    def city(self)->str:
        return self.__city

    @property
    def state(self)->str:
        return self.__state

    @property
    def zipcode(self)->str:
        return self.__zipcode

    def display(self)->None:
        print(f"Street:{self.__street},City:{self.__city},State:{self.__state},Zipcode:{self.__zipcode}")

    def __str__(self)->str:
        return f"{self.__street},{self.__city},{self.__state},{self.__zipcode}"