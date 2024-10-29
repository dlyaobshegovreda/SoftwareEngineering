class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._pages = 0

    def set_pages(self, pages):
        if pages >= 0:
            self._pages = pages
        else:
            print("Количество страниц не может быть отрицательным.")

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_pages(self):
        return self._pages

    def display_info(self):
        return f"Название: {self._title}, Автор: {self._author}, Страницы: {self._pages}"

my_book = Book("1984", "Джордж Оруэлл")
my_book.set_pages(328)

print(my_book.display_info())
print(f"Автор: {my_book.get_author()}")
print(f"Название: {my_book.get_title()}")
print(f"Количество страниц: {my_book.get_pages()}")