from Data_Layer.CSVRepository import CSVRepository

class BuyerRepository(CSVRepository):
    def __init__(self)->None:
        super().__init__("buyers.csv")

    def load_buyers(self)->list:
        raw_data=self.read_all()
        buyers=[]
        for data in raw_data:
            if len(data)==3:
                name=data[0]
                phone=data[1]
                email=data[2]
                buyers.append([name, phone, email])
        return buyers

    def save_buyers(self, buyers: list)->None:
        raw_data=[]
        for buyer in buyers:
            raw_data.append(buyer)
        self.write_all(raw_data)