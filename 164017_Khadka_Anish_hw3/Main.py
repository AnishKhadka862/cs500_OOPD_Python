# Samir Ghimire ID:164061
# Anish Khadka ID:164017
from Presentation_Layer.ConsoleUI import ConsoleUI
from Business_Layer.ListingManager import ListingManager

def main():
    manager = ListingManager()
    console = ConsoleUI(manager)
    console.run()

if __name__ == "__main__":
    main()