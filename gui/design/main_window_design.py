# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(213, 239)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.create_book_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_book_button.setGeometry(QtCore.QRect(60, 80, 91, 23))
        self.create_book_button.setObjectName("create_book_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 211, 81))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.list_books_button = QtWidgets.QPushButton(self.centralwidget)
        self.list_books_button.setGeometry(QtCore.QRect(60, 110, 91, 23))
        self.list_books_button.setObjectName("list_books_button")
        self.find_books_button = QtWidgets.QPushButton(self.centralwidget)
        self.find_books_button.setGeometry(QtCore.QRect(60, 140, 91, 23))
        self.find_books_button.setObjectName("find_books_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Библиотечный менеджер"))
        self.create_book_button.setText(_translate("MainWindow", "Создать книгу"))
        self.label.setText(_translate("MainWindow", "Менеджер библиотечной\n"
"базы данных"))
        self.list_books_button.setText(_translate("MainWindow", "Список книг"))
        self.find_books_button.setText(_translate("MainWindow", "Поиск книг"))
