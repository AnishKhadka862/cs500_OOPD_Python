# Anish Khadka
# 164017
# Library Management Application Main Module
from presentation_layer.library_app import LibraryApp

def main() -> None:
    data_file = "data/catalog.csv"
    app = LibraryApp(data_file)
    app.show_program_title()
    app.process_command()

if __name__ == "__main__":
    main()