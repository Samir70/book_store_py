# book_store Model and Repository Classes Design Recipe

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE students RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO students (name, cohort_name) VALUES ('David', 'April 2022');
INSERT INTO students (name, cohort_name) VALUES ('Anna', 'May 2022');
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book.py)
class Book:


# Repository class
# (in lib/book_repository.py)
class BookRepository:

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python

class Book

  #  should have instance variables id (integer), title (string), author_name (string)

```

<!-- Expectations -->

```python
# 1 can be initialised
book = Book("1", "title", "me")
assert book.id ==  1
assert book.title ==  "title"
assert book.author_name ==  "me"

# 2 can be printed out in a nice way
book = Book("1", "How To Fly", "A Sparrow")
assert str(book) == "1 - How To Fly - A Sparrow"

# 3 can be compared
book1 = Book("1", "How To Fly", "A Sparrow")
book2 = Book("1", "How To Fly", "A Sparrow")
assert book1 == book2
```


## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python

class BookRepository

  # Selecting all records
  # No arguments
  def all
    # Executes the SQL query:
    # SELECT * FROM books;

    # Returns an array of Book objects.
  end

  

  # Add more methods below for each operation you'd like to implement.

  # def create(book)
  # end

  # def update(book)
  # end

  # def delete(book)
  # end
end
```

## 6. Write Test Examples

Write python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as RSpec tests.

```python
# EXAMPLES

# 1 Gets the right data
repo = BookRepository(db_connection)
books = repo.all

books.length # =>  2

books[0].id # =>  1
books[0].title # =>  'Nineteen Eighty-Four'
books[0].author_name # =>  'George Orwell'

books[1].id # =>  2
books[1].title # =>  'Mrs Dalloway'
books[1].author_name # => 'Virginia Woolf'

# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._