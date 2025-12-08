import csv
from colorama import Fore, Style


class CsvDataLoader:
    @staticmethod
    def load_rows(file_path):
        rows = []
        try:
            with open(file_path, "r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    rows.append(row)
        except FileNotFoundError:
            print(Fore.RED + "File not found: " + file_path + Style.RESET_ALL)
        except Exception as e:
            print(
                Fore.RED
                + "Error reading file "
                + file_path
                + ": "
                + str(e)
                + Style.RESET_ALL
            )
        return rows
