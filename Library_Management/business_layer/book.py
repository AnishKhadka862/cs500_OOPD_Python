from .catalog import Catalog
from .enums import CoverType

class Book(Catalog):
    def __init__(
        self,
        catalog_num: int,
        title: str,
        published_date: str,
        cover_type: CoverType,
        subject: str,
        author: str
    ) -> None:
        super().__init__(catalog_num, title, published_date)
        self.__cover_type = cover_type
        self.__subject = subject
        self.__author = author

    def get_cover_type(self) -> CoverType:
        return self.__cover_type

    def get_subject(self) -> str:
        return self.__subject

    def get_author(self) -> str:
        return self.__author

    def __str__(self) -> str:
        base = super().__str__()
        parts = []
        parts.append("BOOK: ")
        parts.append(base)
        parts.append(" [")
        parts.append(self.__cover_type.value)
        parts.append("] ")
        parts.append(self.__subject)
        parts.append(" by ")
        parts.append(self.__author)
        return "".join(parts)