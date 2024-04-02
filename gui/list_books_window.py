from PyQt5 import QtWidgets, QtGui, QtCore
from gui import design


class ListBooksWidget(QtWidgets.QWidget, design.list_books_design.Ui_Form):

    def __init__(self, main_window):
        super().__init__()
        self.books = None # кешируем отображённые книги

        self.main_window = main_window
        self.setupUi(self)

        self.books_model = QtCore.QStringListModel(self)
        self.listView.setModel(self.books_model)

        self.listView.clicked.connect(self.book_choose)
        self.delete_book_button.clicked.connect(self.delete_book)
        self.back_button.clicked.connect(self.back)

    def update_books(self):
        self.books = list(self.main_window.library.get_books())
        view_list = list()
        for book in self.books:
            view_list.append(f'{book.id} - {book.name}, {book.author}')
        self.books_model.setStringList(view_list)
        self.textBrowser.clear()

    def show(self) -> None:
        super().show()
        self.update_books()

    def book_choose(self, index):
        book = self.books[index.row()]
        self.textBrowser.setText(f'{book.name}, {book.author} - {book.genre.name}. {book.description}')

    def delete_book(self):
        chosen_index = self.listView.selectedIndexes()
        if not chosen_index:
            return
        chosen_index = chosen_index[0] # всегда может быть выбран лишь один элемент
        book = self.books[chosen_index.row()]
        self.main_window.library.remove_book(book.id)
        self.update_books()

    def back(self):
        self.main_window.show()
        self.hide()
