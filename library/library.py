from db import database


class Genre:

    def __init__(self, genre_id: int, name: str):
        self.id = genre_id
        self.name = name


class Book:

    def __init__(self, id: int, author: str, name: str, genre: Genre, description: str):
        self.id = id
        self.author = author
        self.name = name
        self.genre = genre
        self.description = description

    # проверяет вхождение строки в основные поля книги
    def __contains__(self, item: str):
        item = item.lower()
        return item in self.author.lower() or item in self.name.lower() or item in self.description.lower()


class Library:

    def __init__(self, name: str = "library"):
        self.name = name
        # создаём книжную полку - словарь в котором ключ - айди книги, значения - сама книга
        self.bookshelf = dict()
        # создаём словарь с жанрами по названию
        self.genres_by_name = dict()
        # создаём второй словарь в котором будем записывать жанр по айди
        self.genres_by_id = dict()
        self.db = database.SQLiteDatabase(name)
        self.load_data()

    def load_data(self):
        # загружаем информацию о жанрах
        for genre_data in self.db.get_genres():
            genre = Genre(genre_data['id'], genre_data['name'])
            self.genres_by_name[genre.name] = genre
            self.genres_by_id[genre.id] = genre
        # загружаем информацию о книгах
        for book_data in self.db.get_books():
            self.bookshelf[book_data['id']] = Book(book_data['id'], book_data['author'],
                                                   book_data['name'], self.genres_by_id[book_data['genre']],
                                                   book_data['description'])

    def create_book(self, author: str, name: str, genre_name: str, description: str):
        # проверяем использовался ли жанр до этого, если нет записываем его в бд
        if genre_name not in self.genres_by_name:
            # при сохранении жанра бд присваивает ему айди и возвращает его
            # используем это айди для записи жанра в словарь
            genre_id = self.db.save_genre(genre_name)
            genre = Genre(genre_id, genre_name)
            self.genres_by_id[genre_id] = genre
            self.genres_by_name[genre_name] = genre
        # записываем информацию о книге в бд, база данных присваивает ей айди
        genre = self.genres_by_name[genre_name]
        book_id = self.db.save_book(author, name, genre.id, description)
        book = Book(book_id, author, name, genre, description)
        self.bookshelf[book_id] = book
        return book

    def remove_book(self, book_id: int):
        if book_id not in self.bookshelf:
            raise ValueError(f"Unknown book id: {book_id}")
        del self.bookshelf[book_id]
        self.db.delete_book(book_id)

    def get_book(self, book_id: int):
        if book_id not in self.bookshelf:
            return None
        return self.bookshelf[book_id]

    def get_books(self):
        return self.bookshelf.values()

    def get_genres(self):
        return self.genres_by_name.values()

    def find_by_keyword(self, word: str):
        books = []
        for book in self.get_books():
            if word in book:
                books.append(book)
        return books

    def find_by_genre(self, genre_name: str):
        if genre_name not in self.genres_by_name:
            return []
        genre_id = self.genres_by_name[genre_name].id
        books = []
        # сравниваем данный жанр с жанром каждой книги, записываем результат в список
        for book in self.get_books():
            if book.genre.id == genre_id:
                books.append(book)
        return books
