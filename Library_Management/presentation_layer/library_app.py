from business_layer.library import Library
from data_layer.catalog_repo import CatalogRepository

class LibraryApp:
    # Initialize the Library Application
    def __init__(self, data_filename: str) -> None:
        self.__repo = CatalogRepository(data_filename)
        self.__library = Library("My Library")

        # Load existing items from the repository
        loaded_items = self.__repo.get_items()
        for it in loaded_items:
            self.__library.add_item(it)

    def show_program_title(self) -> None:
        print("==== Library Catalog System ====")

    def show_menu(self) -> None:
        print("")
        print("1. List all items")
        print("2. Search by title")
        print("3. Search by catalog number")
        print("4. Search by subject")
        print("5. Search article by title")
        print("6. Save and Exit")
        print("")
    # List all items in the library
    def list_all_items(self) -> None:
        items = self.__library.get_items()
        if items is None:
            print("No items available.")
            return
        for item in items:
            print(item)
    # Handle searching items by title
    def handle_search_by_title(self) -> None:
        title = input("Enter full title to search: ").strip()
        results = self.__library.search_by_title(title)
        if len(results) == 0:
            print("No results found.")
        else:
            for r in results:
                print(r)
    # Handle searching items by catalog number
    def handle_search_by_catalog_num(self) -> None:
        num_str = input("Enter catalog number: ").strip()
        try:
            num = int(num_str)
        except Exception:
            print("Invalid number.")
            return
        item = self.__library.search_by_catalog_num(num)
        if item is None:
            print("Not found.")
        else:
            print(item)
    # Handle searching items by subject
    def handle_search_by_subject(self) -> None:
        subject = input("Enter subject: ").strip()
        results = self.__library.search_by_subject(subject)
        if len(results) == 0:
            print("No results found.")
        else:
            for r in results:
                print(r)
    # Handle searching articles by title
    def handle_search_article_by_title(self) -> None:
        title = input("Enter article title: ").strip()
        results = self.__library.search_by_article_title(title)
        if len(results) == 0:
            print("No articles found.")
        else:
            for a in results:
                print(a)
                
    def process_command(self) -> None:
        while True:
            self.show_menu()
            choice = input("Enter choice number: ").strip()
            if choice == "1":
                self.list_all_items()
                continue
            if choice == "2":
                self.handle_search_by_title()
                continue
            if choice == "3":
                self.handle_search_by_catalog_num()
                continue
            if choice == "4":
                self.handle_search_by_subject()
                continue
            if choice == "5":
                self.handle_search_article_by_title()
                continue
            if choice == "6":
                # save and exit
                all_items = self.__library.get_items()
                self.__repo.save_items(all_items)
                print("Data saved. Exiting.")
                break

            print("Unknown choice. Try again.")