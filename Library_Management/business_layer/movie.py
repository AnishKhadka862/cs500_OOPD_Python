from .catalog import Catalog
from .enums import FormatType

class Movie(Catalog):
    def __init__(
        self,
        catalog_num: int,
        title: str,
        published_date: str,
        subject: str,
        format_type: FormatType,
        director: str,
        actors: str,
        year: int,
        length: int
    ) -> None:
        super().__init__(catalog_num, title, published_date)
        self.__subject = subject
        self.__format_type = format_type
        self.__director = director
        self.__actors = actors
        self.__year = year
        self.__length = length

    def get_subject(self) -> str:
        return self.__subject

    def get_format_type(self) -> FormatType:
        return self.__format_type

    def get_director(self) -> str:
        return self.__director

    def get_actors(self) -> str:
        return self.__actors

    def get_year(self) -> int:
        return self.__year

    def get_length(self) -> int:
        return self.__length

    def __str__(self) -> str:
        base = super().__str__()
        parts = []
        parts.append("MOVIE: ")
        parts.append(base)
        parts.append(" [")
        parts.append(self.__format_type.value)
        parts.append("] ")
        parts.append(self.__subject)
        return "".join(parts)