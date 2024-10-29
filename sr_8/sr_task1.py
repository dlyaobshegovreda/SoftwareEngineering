class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Название: {self.title}, Автор: {self.author}"

my_book = Book("1984", "Джордж Оруэлл")

print(my_book.display_info())