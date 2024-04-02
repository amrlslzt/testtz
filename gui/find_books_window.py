from PyQt5 import QtWidgets, QtCore
from gui import design


class FindBooksWidget(QtWidgets.QWidget, design.search_books_design.Ui_Form):

    def __init__(self, main_window):
        super().__init__()
        self.books = None

        self.main_window = main_window
        self.setupUi(self)

        self.books_model = QtCore.QStringListModel(self)
        self.listView.setModel(self.books_model)

        self.back_button.clicked.connect(self.back)
        self.listView.clicked.connect(self.book_choose)
        self.genre_search_button.clicked.connect(self.find_by_genre)
        self.keyword_search_button.clicked.connect(self.find_by_keyword)

    def update_books(self, books):
        self.books = books
        view_list = list()
        for book in self.books:
            view_list.append(f'{book.id} - {book.name}, {book.author}')
        self.books_model.setStringList(view_list)
        self.textBrowser.clear()

    def find_by_genre(self):
        genre = self.lineEdit.text()
        if not genre:
            return

        books = self.main_window.library.find_by_genre(genre)
        self.update_books(books)

    def find_by_keyword(self):
        keyword = self.lineEdit.text()
        if not keyword:
            return

        books = self.main_window.library.find_by_keyword(keyword)
        self.update_books(books)

    def book_choose(self, index):
        book = self.books[index.row()]
        self.textBrowser.setText(f'{book.name}, {book.author} - {book.genre.name}. {book.description}')

    def back(self):
        self.main_window.show()
        self.hide()
