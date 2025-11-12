from Business_Layer.Owner import Owner
from Business_Layer.Property import Property
from Business_Layer.Buyer import Buyer
from Business_Layer.Address import Address
from Data_Layer.OwnerRepository import OwnerRepository
from Data_Layer.PropertyRepository import PropertyRepository
from Data_Layer.BuyerRepository import BuyerRepository

class ListingManager:
    def __init__(self)->None:
        self.__owner_repo=OwnerRepository()
        self.__property_repo=PropertyRepository()
        self.__buyer_repo=BuyerRepository()
        self.__owners: dict={}
        self.__properties: dict={}
        self.__buyers: dict={}

    def load_data(self)->None:
        raw_owners=self.__owner_repo.load_owners()
        for data in raw_owners:
            if len(data)==2:
                first_name=data[0]
                last_name=data[1]
                key=f"{first_name} {last_name}"
                owner=Owner(first_name,last_name)
                self.__owners[key]=owner
            else:
                print(f"Warning: Skipping malformed owner data: {data}")

        raw_properties=self.__property_repo.load_properties()
        for data in raw_properties:
            if len(data)==7:
                id_str=data[0]
                title=data[1]
                address_str=data[2]
                addr_parts=address_str.split(",")
                if len(addr_parts)==4:
                    street,city,state,zipcode=addr_parts
                else:
                    print(f"Warning: Malformed address for property {id_str}: {address_str}. Using defaults.")
                    street,city,state,zipcode="Unknown","Unknown","Unknown","00000"
                address=Address(street,city,state,zipcode)
                price=float(data[3])
                sqft=int(data[4])
                bedrooms=int(data[5])
                owner_name=data[6]
                property=Property(id_str,title,address,price,sqft,bedrooms,owner_name)
                self.__properties[id_str]=property
                if owner_name in self.__owners:
                    self.__owners[owner_name].add_property(property)

        raw_buyers=self.__buyer_repo.load_buyers()
        for data in raw_buyers:
            if len(data)==3: # Name,Phone,Email
                name=data[0]
                phone=data[1]
                email=data[2]
                address=Address("Unknown","Unknown","Unknown","00000") # Default address
                buyer=Buyer(name,phone,email,address)
                self.__buyers[name]=buyer
            else:
                print(f"Warning: Skipping malformed buyer data: {data}")

    def save_data(self)->None:
        owners_list=[]
        for owner in self.__owners.values():
            owners_list.append([owner.first_name,owner.last_name])
        self.__owner_repo.save_owners(owners_list)

        properties_list=[]
        for property in self.__properties.values():
            addr_str=f"{property.address.street},{property.address.city},{property.address.state},{property.address.zipcode}"
            properties_list.append([property.id,property.title,addr_str,property.price,property.sqft,property.bedrooms,property.owner_name])
        self.__property_repo.save_properties(properties_list)

        buyers_list=[]
        for buyer in self.__buyers.values():
            buyers_list.append([buyer.name,buyer.phone,buyer.email])
        self.__buyer_repo.save_buyers(buyers_list)

    def add_property(self,property: Property)->None:
        self.__properties[property.id]=property
        if property.owner_name:
            if property.owner_name in self.__owners:
                self.__owners[property.owner_name].add_property(property)

    def update_property(self,property_id: str,new_data: dict)->None:
        if property_id in self.__properties:
            property=self.__properties[property_id]
            if 'title' in new_data:
                property._Property__title=new_data['title']
            if 'address' in new_data:
                property._Property__address=new_data['address']
            if 'price' in new_data:
                property._Property__price=new_data['price']
            if 'sqft' in new_data:
                property._Property__sqft=new_data['sqft']
            if 'bedrooms' in new_data:
                property._Property__bedrooms=new_data['bedrooms']
            if 'owner_name' in new_data:
                old_owner_name=property.owner_name
                new_owner_name=new_data['owner_name']
                property.owner_name=new_owner_name
                if old_owner_name and old_owner_name in self.__owners:
                    self.__owners[old_owner_name].remove_property(property)
                if new_owner_name and new_owner_name in self.__owners:
                    self.__owners[new_owner_name].add_property(property)
    def delete_property(self,property_id: str)->None:
        if property_id in self.__properties:
            property_to_delete=self.__properties[property_id]
            owner_name=property_to_delete.owner_name
            del self.__properties[property_id]

            if owner_name and owner_name in self.__owners:
                self.__owners[owner_name].remove_property(property_to_delete)

    def search_property_by_owner(self,owner_name: str)->list:
        found_properties=[]
        for property in self.__properties.values():
            if property.owner_name==owner_name:
                found_properties.append(property)
        return found_properties

    def get_owner_list(self)->list:
        return list(self.__owners.values())

    def get_buyer_info(self,buyer_name: str)->Buyer:
        if buyer_name in self.__buyers:
            return self.__buyers[buyer_name]
        return None

    def get_interested_buyers_for_property(self,property_id: str)->list:
        if property_id in self.__properties:
            return self.__properties[property_id].interested_buyers
        return []

    def add_owner(self,first_name: str,last_name: str)->None:
        owner_name=f"{first_name} {last_name}"
        if owner_name not in self.__owners:
            owner=Owner(first_name,last_name)
            self.__owners[owner_name]=owner
        else:
            print(f"Owner {owner_name} already exists.")

    def display_all_properties(self)->None:
        for property in self.__properties.values():
            property.display()

    def display_all_owners(self)->None:
        for owner in self.__owners.values():
            owner.display()

    def display_all_buyers(self)->None:
        for buyer in self.__buyers.values():
            buyer.display()