# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_books.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(673, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(270, 40, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.genre_search_button = QtWidgets.QPushButton(Form)
        self.genre_search_button.setGeometry(QtCore.QRect(270, 70, 121, 23))
        self.genre_search_button.setObjectName("genre_search_button")
        self.keyword_search_button = QtWidgets.QPushButton(Form)
        self.keyword_search_button.setGeometry(QtCore.QRect(270, 100, 121, 23))
        self.keyword_search_button.setObjectName("keyword_search_button")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(445, 0, 231, 301))
        self.textBrowser.setObjectName("textBrowser")
        self.back_button = QtWidgets.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(270, 270, 121, 23))
        self.back_button.setObjectName("back_button")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(0, 0, 256, 301))
        self.listView.setObjectName("listView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Поиск книг"))
        self.genre_search_button.setText(_translate("Form", "По жанру"))
        self.keyword_search_button.setText(_translate("Form", "По ключевому слову"))
        self.back_button.setText(_translate("Form", "Назад"))
