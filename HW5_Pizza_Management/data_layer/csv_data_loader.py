import csv
from colorama import Fore, Style


class CsvDataLoader:
    @staticmethod
    def load_rows(file_path):
        """Reads data from a CSV file into a list of dictionaries."""
        rows = []
        try:
            with open(file_path, "r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    rows.append(row)
        except FileNotFoundError:
            print(Fore.RED + "Critical Error: Dataset file missing! Path: " + file_path + Style.RESET_ALL)
        except Exception as e:
            print(
                Fore.RED
                + "Data access failed for file "
                + file_path
                + ". System Error: "
                + str(e)
                + Style.RESET_ALL
            )
        return rows