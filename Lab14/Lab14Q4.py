from abc import ABC
from abc import abstractmethod


# Abstract class defining the template
class OrderProcess(ABC):

    def __init__(self) -> None:
        self.__order_type = "generic"

    def process_order(self) -> None:
        self.greet_customer()
        self.take_order()
        self.prepare_order()
        self.serve_order()

    def greet_customer(self) -> None:
        print("Waiter: Hello, welcome to our restaurant!")

    def take_order(self) -> None:
        print("Waiter: Taking the customer's order.")

    def prepare_order(self) -> None:
        print("Kitchen: Preparing the customer's dish.")

    @abstractmethod
    def serve_order(self) -> None:
        pass


# Dine-in order process
class DineInOrderProcess(OrderProcess):

    def __init__(self) -> None:
        super().__init__()
        self.__order_type = "dine-in"

    def serve_order(self) -> None:
        print("Waiter: Serving the dish at the customer's table.")
        print("Order type:", self.__order_type)


# Take-out order process
class TakeOutOrderProcess(OrderProcess):

    def __init__(self) -> None:
        super().__init__()
        self.__order_type = "take-out"

    def serve_order(self) -> None:
        print("Waiter: Wrapping the dish and handing it to the customer at the counter.")
        print("Order type:", self.__order_type)


# Demo / main
def main() -> None:
    print("Dine-in order:")
    dine_in = DineInOrderProcess()
    dine_in.process_order()

    print("")
    print("Take-out order:")
    take_out = TakeOutOrderProcess()
    take_out.process_order()


if __name__ == "__main__":
    main()
