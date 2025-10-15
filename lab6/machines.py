# lab6 - Machines and Parts
# Ansh Khadka Lab6 machines.py

# Implement the following class diagrams and write a main class to test all these classes.
# ● Each class implements the display method of the Displayable abstract class and the method should
# display all the current object’s and its superclass object’s information. Keep in mind, you should avoid
# code redundancy.
# ● Define appropriate __init__ method so that all the objects can be created properly.
# ● Define appropriate getters and setters using @property if needed for other classes’ methods. However,
# do not add any public or protected property or public get method for the private attribute ‘parts’ in the
# Machine class.

from abc import ABC, abstractmethod
# Interface classes
class Movable(ABC):
    @abstractmethod
    def move(self) -> None:
        pass

class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass

# Part and MovablePart classes
class Part(Displayable):
    def __init__(self, partno: int, price: float) -> None:
        self.__partno = partno
        self.__price = price

    @property
    def partno(self) -> int:
        return self.__partno

    @property
    def price(self) -> float:
        return self.__price

    def __str__(self) -> str:
        return f"partno = {self.__partno}\nprice = {self.__price}"

    def display(self) -> None:
        print(self)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Part):
            return self.__partno == other.__partno
        return False


class MovablePart(Part, Movable):
    def __init__(self, partno: int, price: float, type: str) -> None:
        super().__init__(partno, price)
        self.__type = type

    @property
    def type(self) -> str:
        return self.__type

    def __str__(self) -> str:
        return f"{super().__str__()}\ntype = {self.__type}"

    def display(self) -> None:
        print(self)

    def move(self) -> None:
        print(f"partno: {self.partno} is moving fast!")

# Machine class
class Machine(Displayable, ABC):
    def __init__(self, machine_name: str) -> None:
        self.__machine_name = machine_name
        self.__parts: list[Part] = []

    @property
    def machine_name(self) -> str:
        return self.__machine_name

    def add_part(self, part: Part) -> None:
        self.__parts.append(part)

    def remove_part_by_partno(self, partno: int) -> None:
        new_parts = []
        for part in self.__parts:
            if part.partno != partno:
                new_parts.append(part)
        self.__parts = new_parts

    def get_duplicated_parts(self) -> dict[int, int]:
        duplicates = {}
        for part in self.__parts:
            if part.partno in duplicates:
                duplicates[part.partno] += 1
            else:
                duplicates[part.partno] = 1

        result = {}
        for key, value in duplicates.items():
            if value > 1:
                result[key] = value
        return result

    def get_expensive_parts(self, priceLimit: float) -> list:
        expensive_list = []
        for part in self.__parts:
            if part.price >= priceLimit:
                expensive_list.append(part)
        return expensive_list

    def get_movable_parts_bytype(self) -> dict:
        parts_by_type = {}
        for part in self.__parts:
            if isinstance(part, MovablePart):
                if part.type not in parts_by_type:
                    parts_by_type[part.type] = []
                parts_by_type[part.type].append(part)
        return parts_by_type

    def get_movable_parts(self) -> list:
        movable_list = []
        for part in self.__parts:
            if isinstance(part, MovablePart):
                movable_list.append(part)
        return movable_list

    def __iter__(self):
        return iter(self.__parts)

    def __str__(self) -> str:
        result = f"machine_name = {self.__machine_name}\nThe machine has these parts:\n"
        for part in self.__parts:
            result += str(part) + "\n"
        return result.strip()

    def display(self) -> None:
        print(self)

    @abstractmethod
    def dowork(self) -> None:
        pass

# JetFighter class
class JetFighter(Displayable, Flyable):
    def __init__(self, model: str, speed: int) -> None:
        self.__model = model
        self.__speed = speed

    @property
    def model(self) -> str:
        return self.__model

    @property
    def speed(self) -> int:
        return self.__speed

    def __str__(self) -> str:
        return f"model = {self.__model}\nspeed = {self.__speed}"

    def display(self) -> None:
        print(self)

    def fly(self) -> None:
        print(f"The JetFighter {self.__model} is flying in the sky!")

# Robot class
class Robot(Machine, JetFighter):
    def __init__(self, machine_name: str, processor: str, model: str, speed: int) -> None:
        Machine.__init__(self, machine_name)
        JetFighter.__init__(self, model, speed)
        self.__processor = processor

    @property
    def processor(self) -> str:
        return self.__processor

    def dowork(self) -> None:
        print(f"The Robot {self.machine_name} is assembling a big truck.")

    def fly(self) -> None:
        print(f"The JetFighter {self.model} is flying in the sky!")
        print(f"The Robot {self.machine_name} is flying over the ocean!")

    def __str__(self) -> str:
        result = f"processor = {self.__processor}\n"
        result += Machine.__str__(self) + "\n"
        result += JetFighter.__str__(self)
        return result.strip()

    def display(self) -> None:
        print(self)

# main function to test all classes

def main():
    robo = Robot('MTX', 'M1X', 'F-16', 10000)
    robo.add_part(Part(111, 100))
    robo.add_part(Part(222, 200))
    robo.add_part(Part(333, 300))
    robo.add_part(Part(222, 300))
    robo.add_part(MovablePart(555, 300, "TypeA"))
    robo.add_part(Part(111, 100))
    robo.add_part(Part(111, 100))
    robo.add_part(MovablePart(777, 300, "TypeB"))
    robo.add_part(MovablePart(655, 300, "TypeA"))
    robo.add_part(MovablePart(755, 300, "TypeA"))
    robo.add_part(MovablePart(977, 300, "TypeB"))

    robo.display()
    print()
    print("\nRobot test flight----")
    robo.fly()

    print("\nRobot dowork() test ----")
    robo.dowork()

    print("\nDuplicated part list----")
    partfreq = robo.get_duplicated_parts()
    for partno in partfreq.keys():
        print(partno, '=>', partfreq[partno], 'times')

    print("\nExpensive part list----")
    expensive_parts = robo.get_expensive_parts(200)
    for part in expensive_parts:
        part.display()

    print("\nMovable part list----")
    movable_parts = robo.get_movable_parts_bytype()
    for type, parts in movable_parts.items():
        print("type =", type)
        for part in parts:
            part.display()
        print()

    print("\nAsk movable to move----")
    movable_parts = robo.get_movable_parts()
    for part in movable_parts:
        part.move()

    print("\nTest remove_part() ----")
    robo.remove_part_by_partno(333)
    for part in robo:
        if part.partno == 333:
            print('Found 333')
            break


if __name__ == "__main__":
    main()
