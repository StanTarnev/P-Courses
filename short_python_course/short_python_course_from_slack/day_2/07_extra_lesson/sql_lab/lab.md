# Python with SQL

Make a simple command line app that will help a library to manage its collection of books.

Your database should have a single table - books - and the table should contain the following columns:

- `id`
- `title`
- `author`
- `published_year`
- `is_loaned`

Provide the following functionality:

- List all books
- Search for a book by title
- Update `is_loaned` to be true or false.

**Hint:** Think about what data type each column will be. As SQLite doesn't have a `BOOLEAN` column type, the standard is to use the `INTEGER` data type and set it to be `1` or `0`.