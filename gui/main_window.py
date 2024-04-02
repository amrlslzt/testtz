from PyQt5 import QtWidgets
from gui.create_book_window import CreateBookWidget
from gui.list_books_window import ListBooksWidget
from gui.find_books_window import FindBooksWidget
from gui import design


class LibraryApp(QtWidgets.QMainWindow, design.main_window_design.Ui_MainWindow):

    def __init__(self, library):
        super().__init__()
        self.library = library

        self.create_book_widget = CreateBookWidget(self)
        self.list_books_widget = ListBooksWidget(self)
        self.find_books_widget = FindBooksWidget(self)

        self.setupUi(self)

        self.create_book_button.clicked.connect(self.create_book)
        self.list_books_button.clicked.connect(self.list_books)
        self.find_books_button.clicked.connect(self.find_books)

    def create_book(self):
        self.create_book_widget.show()
        self.hide()

    def list_books(self):
        self.list_books_widget.show()
        self.hide()

    def find_books(self):
        self.find_books_widget.show()
        self.hide()
