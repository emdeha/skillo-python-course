# Book
#   - add
#   - remove
#   - store
#   - rent
#
# Reader
#   - add
#   - remove
import datetime

from library import Library
from book import Book
from reader import Reader


library = Library(
    name="St. St. Cyril and Methodius",
    address="Vasil Levski Blvd, 1504 Sofia"
)

book = Book(
    id_=1,
    name="War and Peace"
)

reader = Reader(
    id_=1,
    name="Tsvetan Tsvetanov"
)

amount = 3
return_date = datetime.datetime(2024, 3, 8)

library.add_book(book)
library.remove_book(book.id)
# What does it mean to store a book? Will it affect renting? Will it affect removing?
library.store_book(book.id)

# A reader can rent a book if they're subscribed to the library
library.rent_book(book.id, reader.id, return_date)

library.subscribe(reader)
library.unsubscribe(reader.id)
