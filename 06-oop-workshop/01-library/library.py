class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        #
        # self.__available_books = [{book, status, reader}]
        # status = Available, Archived, Rented
        # if status is Rented: reader is not None
        #
        self.__available_books = []
        self.__archived_books = []
        self.__rented_books = {}  # { subscriber_id: [{return_date, book}] }
        self.__subscribers = []

    def add_book(self, book):
        self.__available_books.append(book)

    def remove_book(self, book_id):
        book_to_remove = self.__find_book(book_id)
        if book_to_remove is not None:
            self.__available_books.remove(book_to_remove)

    def store_book(self, book_id):
        book_to_archive = self.__find_book(book_id)
        if book_to_archive is not None:
            self.__archived_books.append(book_to_archive)
            self.remove_book(book_to_archive)

    def __find_book(self, book_id):
        for book in self.__available_books:
            if book.id == book_id:
                return book

        return None

    def rent_book(self, book_id, reader_id, return_date):
        available_book = self.__find_book(book_id)
        if available_book is not None:
            if not self.__is_reader_subscribed(reader_id):
                return "You are not a subscriber"

            self.__rent_book_by_subscriber(available_book, reader_id, return_date)
            return

        if self.__is_book_archived(book_id):
            self.__unarchive_book(book_id)
            return "The book is archived, please come back later"

        return "The book doesn't exist"

    def __is_book_archived(self, book_id):
        archived_book = self.__find_archived_book(book_id)
        return archived_book is not None

    def __unarchive_book(self, book_id):
        archived_book = self.__find_archived_book(book_id)
        if archived_book is None:
            return
        self.__archived_books.remove(archived_book)
        self.__available_books.append(archived_book)

    def __find_archived_book(self, book_id):
        for book in self.__archived_books:
            if book.id == book_id:
                return book
        return None

    def __rent_book_by_subscriber(self, book, reader_id, return_date):
        rented_book = {
            "return_date": return_date,
            "book": book
        }
        if self.__rented_books[reader_id]:
            self.__rented_books[reader_id].append(rented_book)
        else:
            self.__rented_books[reader_id] = [rented_book]

        self.remove_book(book.id)

    def __is_reader_subscribed(self, reader_id):
        subscriber = self.__find_subscriber(reader_id)
        return subscriber is not None

    def __find_subscriber(self, reader_id):
        for subscriber in self.__subscribers:
            if subscriber.id == reader_id:
                return subscriber

        return None

    def subscribe(self, reader):
        pass

    def unsubscribe(self, reader_id):
        pass
