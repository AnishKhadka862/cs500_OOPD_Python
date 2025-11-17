import csv
from business_layer.book import Book
from business_layer.movie import Movie
from business_layer.periodical import Periodical
from business_layer.article import Article
from business_layer.enums import CoverType, FormatType, PeriodicalType


class CatalogRepository:
    def __init__(self, filename: str) -> None:
        self.__filename = filename
    # Get the filename of the repository
    def get_filename(self) -> str:
        return self.__filename
    
    # Save items to the repository
    def save_items(self, items: list) -> None:
        if items is None:
            return

        with open(self.__filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

            for item in items:
                if isinstance(item, Book):
                    writer.writerow([
                        "BOOK",
                        item.get_catalog_num(),
                        item.get_title(),
                        item.get_published_date(),
                        item.get_cover_type().value,
                        item.get_subject(),
                        item.get_author()
                    ])
                    continue

                if isinstance(item, Movie):
                    writer.writerow([
                        "MOVIE",
                        item.get_catalog_num(),
                        item.get_title(),
                        item.get_published_date(),
                        item.get_subject(),
                        item.get_format_type().value,
                        item.get_director(),
                        item.get_actors(),
                        item.get_year(),
                        item.get_length()
                    ])
                    continue

                if isinstance(item, Periodical):
                    writer.writerow([
                        "PERIODICAL",
                        item.get_catalog_num(),
                        item.get_title(),
                        item.get_published_date(),
                        item.get_periodical_type().value
                    ])
                    for a in item.get_articles():
                        writer.writerow([
                            "ARTICLE",
                            a.get_title(),
                            a.get_author(),
                            a.get_issue_date(),
                            a.get_periodical_title()
                        ])
                    continue

    def get_items(self):
        items = []
        periodical_map = {}

        with open(self.__filename, mode="r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if not row:
                    continue

                type_value = row[0].strip().upper()

                if type_value == "BOOK" and len(row) >= 7:
                    try:
                        num = int(row[1])
                    except:
                        continue
                    title = row[2].strip().strip('"')
                    date = row[3].strip().strip('"')
                    cover = row[4].strip().strip('"')
                    subject = row[5].strip().strip('"')
                    author = row[6].strip().strip('"')
                    try:
                        cover_enum = CoverType(cover)
                    except:
                        cover_enum = CoverType.HARDCOVER
                    items.append(Book(num, title, date, cover_enum, subject, author))

                elif type_value == "MOVIE" and len(row) >= 10:
                    try:
                        num = int(row[1])
                        year = int(row[8])
                        length = int(row[9])
                    except:
                        continue
                    title = row[2].strip().strip('"')
                    date = row[3].strip().strip('"')
                    subject = row[4].strip().strip('"')
                    fmt = row[5].strip().strip('"')
                    director = row[6].strip().strip('"')
                    actors = row[7].strip().strip('"')
                    try:
                        fmt_enum = FormatType(fmt)
                    except:
                        fmt_enum = FormatType.DVD
                    items.append(Movie(num, title, date, subject, fmt_enum, director, actors, year, length))

                elif type_value == "PERIODICAL" and len(row) >= 5:
                    try:
                        num = int(row[1])
                    except:
                        continue
                    title = row[2].strip().strip('"')
                    date = row[3].strip().strip('"')
                    ptype = row[4].strip().strip('"')
                    try:
                        p_enum = PeriodicalType(ptype)
                    except:
                        p_enum = PeriodicalType.JOURNAL
                    periodical = Periodical(num, title, date, p_enum)
                    items.append(periodical)
                    periodical_map[title] = periodical

                elif type_value == "ARTICLE" and len(row) >= 5:
                    article_title = row[1].strip().strip('"')
                    author = row[2].strip().strip('"')
                    issue_date = row[3].strip().strip('"')
                    parent_title = row[4].strip().strip('"')

                    article = Article(article_title, author, issue_date, parent_title)

                    if parent_title in periodical_map:
                        periodical_map[parent_title].add_article(article)
                    else:
                        container = Periodical(-1, parent_title, issue_date, PeriodicalType.JOURNAL)
                        container.add_article(article)
                        items.append(container)
                        periodical_map[parent_title] = container

        return items
