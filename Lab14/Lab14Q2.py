from abc import ABC, abstractmethod


# Database class
class Database:
    def insert(self) -> None:
        print("Inserting record into the database")

    def delete(self) -> None:
        print("Deleting record from the database")

    def update(self) -> None:
        print("Updating record in the database")


# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


# InsertCommand
class InsertCommand(Command):
    def __init__(self, obj: Database) -> None:
        self.__obj = obj

    def execute(self) -> None:
        self.__obj.insert()


# UpdateCommand
class UpdateCommand(Command):
    def __init__(self, obj: Database) -> None:
        self.__obj = obj

    def execute(self) -> None:
        self.__obj.update()


# DeleteCommand
class DeleteCommand(Command):
    def __init__(self, obj: Database) -> None:
        self.__obj = obj

    def execute(self) -> None:
        self.__obj.delete()


# Client class
class Client:
    def __init__(self) -> None:
        self.__command: Command | None = None

    def setCommand(self, command: Command) -> None:
        self.__command = command

    def executeCommand(self) -> None:
        if self.__command:
            self.__command.execute()


# Demo / main
def main():
    db = Database()
    client = Client()

    # Set and execute InsertCommand
    client.setCommand(InsertCommand(db))
    client.executeCommand()  # Inserting record into the database

    # Set and execute UpdateCommand
    client.setCommand(UpdateCommand(db))
    client.executeCommand()  # Updating record in the database

    # Set and execute DeleteCommand
    client.setCommand(DeleteCommand(db))
    client.executeCommand()  # Deleting record from the database


if __name__ == "__main__":
    main()
