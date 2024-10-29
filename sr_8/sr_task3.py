class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.pages = 0

    def set_pages(self, pages):
        self.pages = pages

    def display_info(self):
        return f"Название: {self.title}, Автор: {self.author}, Страницы: {self.pages}"

class EBook(Book):
    def __init__(self, title, author, file_format):
        super().__init__(title, author)
        self.file_format = file_format

    def display_info(self):
        return super().display_info() + f", Формат: {self.file_format}"

my_book = Book("1984", "Джордж Оруэлл")
my_book.set_pages(328)

my_ebook = EBook("1984", "Джордж Оруэлл", "PDF")
my_ebook.set_pages(328)

print(my_book.display_info())
print(my_ebook.display_info())