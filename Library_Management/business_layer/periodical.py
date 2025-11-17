from __future__ import annotations
from .catalog import Catalog
from .enums import PeriodicalType
from .article import Article

class Periodical(Catalog):
    def __init__(self, catalog_num: int, title: str, published_date: str, periodical_type: PeriodicalType) -> None:
        super().__init__(catalog_num, title, published_date)
        self.__periodical_type = periodical_type
        self.__articles = []

    def add_article(self, article: 'Article') -> None:
        if article is None:
            return
        self.__articles.append(article)

    def get_periodical_type(self) -> PeriodicalType:
        return self.__periodical_type

    def get_articles(self) -> list['Article']:
        return list(self.__articles)

    def __str__(self) -> str:
        base = super().__str__()
        parts = []
        parts.append("PERIODICAL: ")
        parts.append(base)
        parts.append(" [")
        parts.append(self.__periodical_type.value)
        parts.append("]")
        if self.__articles:
            parts.append("\n  ARTICLES:")
            for article in self.__articles:
                parts.append(f"\n    - {str(article)}")
        return "".join(parts)