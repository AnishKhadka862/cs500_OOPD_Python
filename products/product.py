class Product:
    def __init__(self, name: str, price: float) -> None:
        self.__name = name
        self.__price = price
    
class Phone(Product):
    def __init__(self, name: str, price: int, network: str) -> None:
        Product.__init__(self, name, price)
        self.__network = network

class Computer(Product):
    def __init__(self, name: str, price: int, speed: int) -> None:
        Product.__init__(self, name, price)
        self.__speed = speed
        
class SmartPhone(Phone, Computer):
    def __init__(self, name: str, price: int, network: str, speed: int, camera: str) -> None:
        Phone.__init__(self, name, price, network)
        Computer.__init__(self, name, price, speed)
        self.__camera = camera

def main() -> None:
    obj = SmartPhone("xPhone", 1200, "5G", 4000, "BK")

if __name__ == "__main__":
    main()