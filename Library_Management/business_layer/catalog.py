class Catalog:
    def __init__(self, catalog_num: int, title: str, published_date: str) -> None:
        self.__catalog_num = catalog_num
        self.__title = title
        self.__published_date = published_date

    def get_catalog_num(self) -> int:
        return self.__catalog_num

    def get_title(self) -> str:
        return self.__title

    def get_published_date(self) -> str:
        return self.__published_date

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if not isinstance(other, Catalog):
            return False
        if self.__catalog_num == other.get_catalog_num():
            return True
        return False

    def __str__(self) -> str:
        parts = []
        parts.append(str(self.__catalog_num))
        parts.append(" - ")
        parts.append(self.__title)
        parts.append(" (")
        parts.append(self.__published_date)
        parts.append(")")
        return "".join(parts)