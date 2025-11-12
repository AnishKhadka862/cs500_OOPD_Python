from data_layer import Customer, CustomerDataHandler

class CustomerManager:
    def __init__(self, filename):
        self._data_handler = CustomerDataHandler(filename)
        self._customers = self._data_handler.load_customers()

    # Add new customer
    def add_customer(self, account_number, last_name, first_name, address, balance):
        new_customer = Customer(account_number, last_name, first_name, address, balance)
        self._customers.append(new_customer)
        self._data_handler.save_customers(self._customers)
        print("Customer added successfully.\n")

    # View all customers (sorted order optional)
    def view_customers(self, order="asc"):
        if len(self._customers) == 0:
            print("No customers found.\n")
            return

        sorted_customers = sorted(self._customers, key=lambda c: c.last_name, reverse=(order == "desc"))
        for customer in sorted_customers:
            print(f"{customer.account_number} | {customer.last_name}, {customer.first_name} | "
                  f"{customer.address} | Balance: ${customer.balance}")
        print()

    # Search customer by last name
    def search_customer(self, last_name):
        found_customers = []
        for customer in self._customers:
            if customer.last_name.lower() == last_name.lower():
                found_customers.append(customer)

        if len(found_customers) == 0:
            print("No customer found with that last name.\n")
        else:
            for c in found_customers:
                print(f"Found: {c.account_number} | {c.last_name}, {c.first_name} | {c.address} | Balance: ${c.balance}")
        return found_customers

    # Edit customer information
    def edit_customer(self, last_name, new_first_name=None, new_address=None, new_balance=None):
        found = False
        for customer in self._customers:
            if customer.last_name.lower() == last_name.lower():
                if new_first_name is not None:
                    customer.first_name = new_first_name
                if new_address is not None:
                    customer.address = new_address
                if new_balance is not None:
                    customer.balance = new_balance
                found = True

        if found:
            self._data_handler.save_customers(self._customers)
            print("Customer information updated successfully.\n")
        else:
            print("Customer not found.\n")

    # Delete customer by last name
    def delete_customer(self, last_name):
        new_list = []
        deleted = False
        for customer in self._customers:
            if customer.last_name.lower() != last_name.lower():
                new_list.append(customer)
            else:
                deleted = True

        self._customers = new_list
        self._data_handler.save_customers(self._customers)

        if deleted:
            print("Customer deleted successfully.\n")
        else:
            print("No matching customer found.\n")

    # Find customers with negative balance
    def find_negative_balance(self):
        print("Customers with negative balance:")
        found = False
        for c in self._customers:
            if c.balance < 0:
                print(f"{c.last_name}, {c.first_name} | Balance: ${c.balance}")
                found = True
        if not found:
            print("No customers with negative balance.\n")

    # Find customer with max and min balance
    def find_max_min_balance(self):
        if len(self._customers) == 0:
            print("No customers available.\n")
            return

        max_customer = self._customers[0]
        min_customer = self._customers[0]

        for c in self._customers:
            if c.balance > max_customer.balance:
                max_customer = c
            if c.balance < min_customer.balance:
                min_customer = c

        print(f"Highest Balance: {max_customer.last_name}, {max_customer.first_name} — ${max_customer.balance}")
        print(f"Lowest Balance: {min_customer.last_name}, {min_customer.first_name} — ${min_customer.balance}\n")