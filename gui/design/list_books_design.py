# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_books.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(669, 301)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(410, 0, 256, 301))
        self.textBrowser.setObjectName("textBrowser")
        self.back_button = QtWidgets.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(280, 260, 111, 23))
        self.back_button.setObjectName("back_button")
        self.delete_book_button = QtWidgets.QPushButton(Form)
        self.delete_book_button.setGeometry(QtCore.QRect(280, 130, 111, 23))
        self.delete_book_button.setObjectName("delete_book_button")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(0, 0, 256, 301))
        self.listView.setObjectName("listView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Список книг"))
        self.back_button.setText(_translate("Form", "Назад"))
        self.delete_book_button.setText(_translate("Form", "Удалить книгу"))
