import sqlite3
from abc import ABC
from abc import abstractmethod


# Database (Receiver)
class Database:

    def __init__(self, db_file):
        self.__conn = sqlite3.connect(db_file)

    def execute(self, query, params=None):
        if params is None:
            params = []

        cursor = self.__conn.cursor()
        cursor.execute(query, params)
        self.__conn.commit()
        return cursor.fetchall()


# Command interface
class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


# Create table command
class CreateTableCommand(Command):

    def __init__(self, db, table_name):
        self.__db = db
        self.__table_name = table_name

    def execute(self):
        query = f"""
        CREATE TABLE IF NOT EXISTS {self.__table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
        """
        self.__db.execute(query)
        print("Table", self.__table_name, "created.")


# Insert record command
class InsertRecordCommand(Command):

    def __init__(self, db, table_name, name, age):
        self.__db = db
        self.__table_name = table_name
        self.__name = name
        self.__age = age

    def execute(self):
        query = f"INSERT INTO {self.__table_name} (name, age) VALUES (?, ?)"
        self.__db.execute(query, [self.__name, self.__age])
        print("Inserted record:", "(", self.__name, ",", self.__age, ")")


# Get record command
class GetRecordCommand(Command):

    def __init__(self, db, table_name, record_id):
        self.__db = db
        self.__table_name = table_name
        self.__record_id = record_id

    def execute(self):
        query = f"SELECT * FROM {self.__table_name} WHERE id = ?"
        rows = self.__db.execute(query, [self.__record_id])

        if rows:
            print("Record:", rows[0])
        else:
            print("Record not found")


# Update record command
class UpdateRecordCommand(Command):

    def __init__(self, db, table_name, record_id, new_name, new_age):
        self.__db = db
        self.__table_name = table_name
        self.__record_id = record_id
        self.__new_name = new_name
        self.__new_age = new_age

    def execute(self):
        query = f"UPDATE {self.__table_name} SET name = ?, age = ? WHERE id = ?"
        self.__db.execute(query, [self.__new_name, self.__new_age, self.__record_id])
        print(
            "Updated record id",
            self.__record_id,
            "to (",
            self.__new_name,
            ",",
            self.__new_age,
            ")"
        )


# Delete record command
class DeleteRecordCommand(Command):

    def __init__(self, db, table_name, record_id):
        self.__db = db
        self.__table_name = table_name
        self.__record_id = record_id

    def execute(self):
        query = f"DELETE FROM {self.__table_name} WHERE id = ?"
        self.__db.execute(query, [self.__record_id])
        print("Deleted record id", self.__record_id)


# Invoker (menu-style)
class DatabaseClient:

    def __init__(self):
        self.__command = None

    def setCommand(self, command):
        self.__command = command

    def executeCommand(self):
        if self.__command is not None:
            self.__command.execute()


# Demo
def main():
    db = Database("example.db")
    client = DatabaseClient()
    table_name = "users"

    # Create table
    create_table_cmd = CreateTableCommand(db, table_name)
    client.setCommand(create_table_cmd)
    client.executeCommand()

    # Insert records
    insert_alice_cmd = InsertRecordCommand(db, table_name, "Alice", 25)
    client.setCommand(insert_alice_cmd)
    client.executeCommand()

    insert_bob_cmd = InsertRecordCommand(db, table_name, "Bob", 30)
    client.setCommand(insert_bob_cmd)
    client.executeCommand()

    # Get a record
    get_record_cmd = GetRecordCommand(db, table_name, 1)
    client.setCommand(get_record_cmd)
    client.executeCommand()

    # Update a record
    update_record_cmd = UpdateRecordCommand(db, table_name, 1, "Alice Smith", 26)
    client.setCommand(update_record_cmd)
    client.executeCommand()

    # Get the updated record
    get_updated_cmd = GetRecordCommand(db, table_name, 1)
    client.setCommand(get_updated_cmd)
    client.executeCommand()

    # Delete a record
    delete_record_cmd = DeleteRecordCommand(db, table_name, 2)
    client.setCommand(delete_record_cmd)
    client.executeCommand()


if __name__ == "__main__":
    main()
