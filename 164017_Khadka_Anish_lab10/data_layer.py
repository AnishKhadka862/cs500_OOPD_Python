import csv

class Customer:
    def __init__(self, account_number, last_name, first_name, address, balance):
        self._account_number = account_number
        self._last_name = last_name
        self._first_name = first_name
        self._address = address
        self._balance = float(balance)

    # account_number property
    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number = value

    # last_name property
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    # first_name property
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    # address property
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    # balance property
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = float(value)

    def __str__(self):
        return f"{self._account_number};{self._last_name};{self._first_name};{self._address};{self._balance}"


class CustomerDataHandler:
    def __init__(self, filename):
        self._filename = filename

    def load_customers(self):
        customers = []
        try:
            with open(self._filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file, delimiter=';')
                for row in reader:
                    if len(row) == 5:
                        account_number, last_name, first_name, address, balance = row
                        customer = Customer(account_number, last_name, first_name, address, balance)
                        customers.append(customer)
        except FileNotFoundError:
            print(f"File '{self._filename}' not found. Starting with an empty list.")
        return customers

    def save_customers(self, customers):
        with open(self._filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            for customer in customers:
                writer.writerow([
                    customer.account_number,
                    customer.last_name,
                    customer.first_name,
                    customer.address,
                    customer.balance
                ])