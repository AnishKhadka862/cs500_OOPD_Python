from .catalog import Catalog
class Article:
    def __init__(self, title: str, author: str, issue_date: str, periodical_title: str) -> None:
        self.__title = title
        self.__author = author
        self.__issue_date = issue_date
        self.__periodical_title = periodical_title

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def get_issue_date(self) -> str:
        return self.__issue_date

    def get_periodical_title(self) -> str:
        return self.__periodical_title

    def __str__(self) -> str:
        parts = []
        parts.append("ARTICLE: ")
        parts.append(self.__title)
        parts.append(" (")
        parts.append(self.__periodical_title)
        parts.append(")")
        return "".join(parts)