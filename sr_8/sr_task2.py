class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.pages = 0
        self.genre = genre

    def display_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Страницы: {self.pages}, Жанр: {self.genre}"

    def set_pages(self, pages):
        self.pages = pages

my_book = Book("1984", "Джордж Оруэлл", "Антиутопия")

my_book.set_pages(328)

print(my_book.display_info())