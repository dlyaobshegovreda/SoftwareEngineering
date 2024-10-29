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

    def display_info(self):
        return f"Название: {self._title}, Автор: {self._author}, Страницы: {self._pages}"

    def play(self):
        return "Чтение книги..."


class EBook(Book):
    def __init__(self, title, author, file_format):
        super().__init__(title, author)
        self.file_format = file_format

    def display_info(self):
        return super().display_info() + f", Формат: {self.file_format}"

    def play(self):
        return "Чтение электронной книги в формате " + self.file_format


class AudioBook(Book):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self.duration = duration

    def display_info(self):
        return super().display_info() + f", Длительность: {self.duration} минут"

    def play(self):
        return "Прослушивание аудиокниги..."


# Список книг разных типов
books = [
    Book("1984", "Джордж Оруэлл"),
    EBook("Война и мир", "Лев Толстой", "EPUB"),
    AudioBook("Мастера и Маргарита", "Михаил Булгаков", 500)
]

books[0].set_pages(328)

for book in books:
    print(book.display_info())
    print(book.play())