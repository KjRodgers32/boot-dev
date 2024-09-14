class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for ex_book in self.books:
            if ex_book.title == book.title and ex_book.author == book.author:
                self.books.remove(ex_book)
    
    def search_books(self, search_string):
        lowered_ss = search_string.lower()
        matching_books = []
        for book in self.books:
            if lowered_ss in book.title.lower() or lowered_ss in book.author.lower():
                matching_books.append(book)
        return matching_books