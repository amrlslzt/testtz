import sqlite3


# Класс, представляющий SQLite датабазу программы.
class SQLiteDatabase:

    # Параметры:
    # name - название базы данных.
    def __init__(self, name: str = "database"):
        self.name = name
        # подключаемся...
        self.connection = sqlite3.connect(f"db/{name}.db", check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        # заполняем бд
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS genres (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
                        )''')
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY,
                        author TEXT NOT NULL,
                        name TEXT NOT NULL,
                        genre INTEGER NOT NULL,
                        description TEXT NOT NULL,
                        FOREIGN KEY (name) REFERENCES genres (id)
                        )''')
        self.connection.commit()

    # Возвразает все книги, сохранённые в базу данных.
    def get_books(self):
        with self.connection:
            return self.cursor.execute('SELECT * FROM books').fetchall()

    def get_book(self, book_id):
        with self.connection:
            return self.cursor.execute('SELECT * FROM books WHERE id = ?', book_id)

    # Сохраняет книгу с данными параметрами.
    # Возвращает айди, присвоенный этой книге.
    def save_book(self, author: str, name: str, genre: int, description: str) -> int:
        with self.connection:
            self.cursor.execute("INSERT INTO books (author, name, genre, description) VALUES (?, ?, ?, ?)",
                                (author, name, genre, description))
            return self.cursor.lastrowid

    # Удаляет книгу из базы данных.
    # id - Айди книги для удаления.
    def delete_book(self, id: int):
        with self.connection:
            self.cursor.execute("DELETE FROM books WHERE id = ?", (id,))

    # Возвращает список жанров.
    def get_genres(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM genres").fetchall()

    # Сохраняет жанр с данным названием в базу данных.
    # Возвращает айди, присвоенный этому жанру.
    def save_genre(self, name: str) -> int:
        with self.connection:
            self.cursor.execute("INSERT INTO genres (name) VALUES (?)", (name,))
            return self.cursor.lastrowid
