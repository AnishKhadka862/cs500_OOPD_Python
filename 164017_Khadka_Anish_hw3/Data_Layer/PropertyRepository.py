from Data_Layer.CSVRepository import CSVRepository

class PropertyRepository(CSVRepository):
    def __init__(self)->None:
        super().__init__("properties.csv")

    def load_properties(self)->list:
        raw_data=self.read_all()
        properties=[]
        for data in raw_data:
            if len(data)==7:
                properties.append(data)
            else:
                print(f"Warning: Skipping malformed property data: {data}")
        return properties

    def save_properties(self, properties: list)->None:
        raw_data=[]
        for property in properties:
            raw_data.append(property)
        self.write_all(raw_data)