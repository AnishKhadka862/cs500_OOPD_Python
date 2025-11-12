from Data_Layer.CSVRepository import CSVRepository

class OwnerRepository(CSVRepository):
    def __init__(self)->None:
        super().__init__("owners.csv")

    def load_owners(self)->list:
        raw_data=self.read_all()
        owners=[]
        for data in raw_data:
            if len(data)==2:
                first_name=data[0]
                last_name=data[1]
                owners.append([first_name, last_name])
        return owners

    def save_owners(self, owners: list)->None:
        raw_data=[]
        for owner in owners:
            raw_data.append(owner)
        self.write_all(raw_data)