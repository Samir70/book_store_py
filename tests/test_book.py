from lib.book import Book

"""
Book constructs with an id, title and author
"""
def test_artist_constructs():
    book = Book("1", "Test book", "Test author")
    assert book.id == 1
    assert book.title == "Test book"
    assert book.author == "Test author"

"""
We can format books to strings nicely
"""
def test_books_format_nicely():
    book = Book(1, "Test book", "Test author")
    assert str(book) == "1 - Test book - Test author"
    # Try commenting out the `__repr__` method in lib/book.py
    # And see what happens when you run this test again.

"""
We can compare two identical books
And have them be equal
"""
def test_books_are_equal():
    book1 = Book(1, "Test book", "Test author")
    book2 = Book(1, "Test book", "Test author")
    assert book1 == book2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
