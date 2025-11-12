# Anish Khadka
# student id: 164017
# Lab 10 - Bank Customer Management System

from business_layer import CustomerManager

def main():
    filename = "customers.csv"
    manager = CustomerManager(filename)

    while True:
        print("-----BANK CUSTOMER MANAGEMENT SYSTEM-----")
        print("1. Add New Customer")
        print("2. View Customer List")
        print("3. Search and Edit Customer")
        print("4. Delete Customer")
        print("5. Find Customers with Negative Balance")
        print("6. Find Max/Min Balance")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("\n--- Add New Customer ---")
            account_number = input("Enter Account Number: ")
            last_name = input("Enter Last Name: ")
            first_name = input("Enter First Name: ")
            address = input("Enter Address: ")
            balance = input("Enter Account Balance: ")

            try:
                balance = float(balance)
                manager.add_customer(account_number, last_name, first_name, address, balance)
            except ValueError:
                print("Invalid balance amount.\n")

        elif choice == "2":
            print("\n--- View Customers ---")
            order = input("Sort order (asc/desc): ").lower()
            if order not in ["asc", "desc"]:
                order = "asc"
            manager.view_customers(order)

        elif choice == "3":
            print("\n--- Search and Edit Customer ---")
            last_name = input("Enter Last Name to Search: ")
            found_customers = manager.search_customer(last_name)
            if len(found_customers) > 0:
                print("\nDo you want to edit this customer's information?")
                ans = input("Enter Y to edit, N to skip: ").lower()
                if ans == "y":
                    new_first_name = input("Enter new First Name (leave blank to skip): ")
                    new_address = input("Enter new Address (leave blank to skip): ")
                    new_balance = input("Enter new Balance (leave blank to skip): ")

                    if new_balance.strip() == "":
                        new_balance = None
                    else:
                        try:
                            new_balance = float(new_balance)
                        except ValueError:
                            print("Invalid balance. Edit canceled.\n")
                            continue

                    if new_first_name.strip() == "":
                        new_first_name = None
                    if new_address.strip() == "":
                        new_address = None

                    manager.edit_customer(last_name, new_first_name, new_address, new_balance)

        elif choice == "4":
            print("\n--- Delete Customer ---")
            last_name = input("Enter Last Name of the Customer to Delete: ")
            manager.delete_customer(last_name)

        elif choice == "5":
            print("\n--- Customers with Negative Balance ---")
            manager.find_negative_balance()

        elif choice == "6":
            print("\n--- Find Max/Min Balance ---")
            manager.find_max_min_balance()

        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 7.\n")


if __name__ == "__main__":
    main()