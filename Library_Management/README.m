# Library Catalog Management System

This project implements a **Library Catalog Management System** in Python that allows managing **books, movies, periodicals, and articles**. The system stores the catalog in a CSV file and supports reading from and writing to the file. It is designed using an **object-oriented approach**.

## Features

The system can:

- Read the catalog from a CSV file
- Display books, movies, periodicals, and articles
- Add new items (books, movies, periodicals, articles)
- Save the catalog back to the CSV file

### Books
- Store catalog number, title, published date, cover type, subject, and author.

### Movies
- Store catalog number, title, published date, subject, format type, director, actors, year, and length.

### Periodicals
- Store catalog number, title, published date, and type (Journal or Magazine). Can contain multiple articles.

### Articles
- Store title, author, issue date, and parent periodical title.

### Additional Features
- Read and save catalog data in CSV format.
- Proper handling of missing or inconsistent data.
