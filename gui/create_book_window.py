from PyQt5.QtCore import Qt, QStringListModel

from PyQt5 import QtWidgets
from gui import design


class CreateBookWidget(QtWidgets.QWidget, design.create_book_design.Ui_Form):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setupUi(self)
        self.back_button.clicked.connect(self.back)
        self.create_button.clicked.connect(self.create_book)

        self.completer = QtWidgets.QCompleter(None, self.genre_edit)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.genre_edit.setCompleter(self.completer)

        self.update_completer()

    def update_completer(self):
        genres = list(map(lambda genre: genre.name, self.main_window.library.get_genres()))

        self.completer.setModel(QStringListModel(genres, self.genre_edit))

    def create_book(self):
        name = self.name_edit.text()
        if not name:
            self.result_label.setText("Вы не указали название!")
            return

        author = self.author_edit.text()
        if not author:
            self.result_label.setText("Вы не указали автора!")
            return

        genre = self.genre_edit.text()
        if not genre:
            self.result_label.setText("Вы не указали жанр!")
            return

        description = self.description_edit.toPlainText()
        if not description:
            self.result_label.setText("Вы не указали описание!")
            return

        self.update_completer()
        self.main_window.library.create_book(author, name, genre, description)
        self.result_label.setText("Книга создана!")
        self.name_edit.clear()
        self.author_edit.clear()
        self.genre_edit.clear()
        self.description_edit.clear()

    def back(self):
        self.main_window.show()
        self.hide()
