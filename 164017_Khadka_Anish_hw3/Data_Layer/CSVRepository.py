import csv

class CSVRepository:
    def __init__(self, filepath: str)->None:
        self.__filepath=filepath

    def read_all(self)->list:
        items=[]
        with open(self.__filepath, 'r') as file:
            reader=csv.reader(file)
            for row in reader:
                items.append(row)
        return items

    def write_all(self, items: list)->None:
        with open(self.__filepath, 'w', newline='') as file:
            writer=csv.writer(file)
            for item in items:
                writer.writerow(item)

    @property
    def filepath(self)->str:
        return self.__filepath