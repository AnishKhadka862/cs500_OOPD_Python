from .catalog import Catalog
from .book import Book
from .movie import Movie
from .periodical import Periodical
from .article import Article

class Library:
    def __init__(self, library_name: str) -> None:
        self.__library_name = library_name
        self.__items = []

    def get_library_name(self) -> str:
        return self.__library_name

    def get_items(self) -> list:
        return list(self.__items)

    def add_item(self, item: Catalog) -> None:
        if item is None:
            return
        self.__items.append(item)

    def remove_item(self, catalog_num: int) -> None:
        new_list = []
        for item in self.__items:
            if item.get_catalog_num() == catalog_num:
                continue
            new_list.append(item)
        self.__items = new_list

    def search_by_title(self, title: str) -> list:
        results = []
        if title is None:
            return results
        for item in self.__items:
            item_title = item.get_title()
            if item_title == title:
                results.append(item)
        return results

    def search_by_catalog_num(self, catalog_num: int):
        if catalog_num is None:
            return None
        for item in self.__items:
            if item.get_catalog_num() == catalog_num:
                return item
        return None

    def search_by_subject(self, subject: str) -> list:
        results = []
        if subject is None:
            return results
        for item in self.__items:
            # check attribute existence explicitly
            try:
                subject_value = item.get_subject()
            except Exception:
                subject_value = None
            if subject_value == subject:
                results.append(item)
        return results

    def search_by_article_title(self, title: str) -> list:
        results = []
        if title is None:
            return results
        for item in self.__items:
            if isinstance(item, Periodical):
                articles = item.get_articles()
                for article in articles:
                    if article.get_title() == title:
                        results.append(article)
        return results

    def get_books_by_cover_type(self, cover_type_str: str) -> list:
        results = []
        if cover_type_str is None:
            return results
        for item in self.__items:
            if isinstance(item, Book):
                ct = item.get_cover_type()
                if ct is not None and ct.value == cover_type_str:
                    results.append(item)
        return results

    def get_movies_by_movie_format(self, format_type_str: str) -> list:
        results = []
        if format_type_str is None:
            return results
        for item in self.__items:
            if isinstance(item, Movie):
                ft = item.get_format_type()
                if ft is not None and ft.value == format_type_str:
                    results.append(item)
        return results