from Business_Layer.ListingManager import ListingManager
from Business_Layer.Property import Property
from Business_Layer.Address import Address
from Business_Layer.Owner import Owner

class ConsoleUI:
    def __init__(self, manager:ListingManager)->None:
        self.__manager=manager

    def show_menu(self)->None:
        print("\nReal Estate Listing Management")
        print("1.Add New Property")
        print("2.Update Existing Property")
        print("3.Delete Property")
        print("4.Search Property by Owner")
        print("5.Generate List of Owners")
        print("6.Retrieve Buyer Information")
        print("7.Display Interested Buyers for a Property")
        print("8.Save and Load Data")
        print("9.Add New Owner")
        print("10.Exit")

    def run(self)->None:
        self.__manager.load_data()
        while True:
            self.show_menu()
            choice=input("Enter your choice:")

            if choice=="1":
                self.add_new_property()
            elif choice=="2":
                self.update_property()
            elif choice=="3":
                self.delete_property()
            elif choice=="4":
                self.search_property_by_owner()
            elif choice=="5":
                self.generate_owner_list()
            elif choice=="6":
                self.retrieve_buyer_info()
            elif choice=="7":
                self.display_interested_buyers()
            elif choice=="8":
                self.save_and_load_data()
            elif choice=="9":
                self.add_new_owner()
            elif choice=="10":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.Please enter 1-10.")

    def add_new_property(self)->None:
        id_str=input("Enter property ID:")
        title=input("Enter property title:")
        street=input("Enter street:")
        city=input("Enter city:")
        state=input("Enter state:")
        zipcode=input("Enter zipcode:")
        address=Address(street, city, state, zipcode)
        price=float(input("Enter property price:"))
        sqft=int(input("Enter square footage:"))
        bedrooms=int(input("Enter number of bedrooms:"))
        owner_name=input("Enter owner name for this property:") 
        property=Property(id_str, title, address, price, sqft, bedrooms, owner_name)
        self.__manager.add_property(property)
        print("Property added successfully.")

    def update_property(self)->None:
        property_id=input("Enter property ID to update:")
        if property_id not in self.__manager._ListingManager__properties:
            print("Property not found.")
            return

        property_to_update=self.__manager._ListingManager__properties[property_id]

        new_title=input("Enter new title (leave blank to keep current):")
        new_street=input("Enter new street (leave blank to keep current):")
        new_city=input("Enter new city (leave blank to keep current):")
        new_state=input("Enter new state (leave blank to keep current):")
        new_zipcode=input("Enter new zipcode (leave blank to keep current):")
        new_price_str=input("Enter new price (leave blank to keep current):")
        new_sqft_str=input("Enter new square footage (leave blank to keep current):")
        new_bedrooms_str=input("Enter new number of bedrooms (leave blank to keep current):")
        new_owner_name=input("Enter new owner name (leave blank to keep current):")

        new_data={}
        if new_title != "":
            new_data['title']=new_title
        if new_street != "" or new_city != "" or new_state != "" or new_zipcode != "":
            print("To update address, please re-enter the whole address.")
            street=input("Enter new street:")
            city=input("Enter new city:")
            state=input("Enter new state:")
            zipcode=input("Enter new zipcode:")
            new_data['address']=Address(street, city, state, zipcode)
        if new_price_str != "":
            new_data['price']=float(new_price_str)
        if new_sqft_str != "":
            new_data['sqft']=int(new_sqft_str)
        if new_bedrooms_str != "":
            new_data['bedrooms']=int(new_bedrooms_str)
        if new_owner_name != "":
            new_data['owner_name']=new_owner_name

        if new_data:
            self.__manager.update_property(property_id, new_data)
            print("Property updated successfully.")
        else:
            print("No changes made.")

    def delete_property(self)->None:
        property_id=input("Enter property ID to delete:")
        self.__manager.delete_property(property_id)
        print("Property deleted successfully.")

    def search_property_by_owner(self)->None:
        owner_name=input("Enter owner name to search:")
        properties=self.__manager.search_property_by_owner(owner_name)
        if properties:
            print(f"\nProperties for owner '{owner_name}':")
            for property in properties:
                property.display()
        else:
            print(f"No properties found for owner '{owner_name}'.")

    def generate_owner_list(self)->None:
        owners=self.__manager.get_owner_list()
        print("\nList of Owners:")
        for owner in owners:
            print(f"Owner:{owner.first_name} {owner.last_name}")

    def retrieve_buyer_info(self)->None:
        buyer_name=input("Enter buyer name to retrieve info:")
        buyer=self.__manager.get_buyer_info(buyer_name)
        if buyer is not None:
            buyer.display()
        else:
            print("Buyer not found.")

    def display_interested_buyers(self)->None:
        property_id=input("Enter property ID to display interested buyers:")
        buyers=self.__manager.get_interested_buyers_for_property(property_id)
        print(f"\nInterested Buyers for Property ID '{property_id}':")
        for buyer in buyers:
            buyer.display()

    def save_and_load_data(self)->None:
        self.__manager.save_data()
        print("Data saved successfully.")

    def add_new_owner(self)->None:
        first_name=input("Enter owner's first name:")
        last_name=input("Enter owner's last name:")
        self.__manager.add_owner(first_name, last_name)
        print("Owner added successfully.")

