# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_book.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(439, 239)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 50, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 47, 13))
        self.label_3.setObjectName("label_3")
        self.create_button = QtWidgets.QPushButton(Form)
        self.create_button.setGeometry(QtCore.QRect(180, 160, 91, 21))
        self.create_button.setObjectName("create_button")
        self.name_edit = QtWidgets.QLineEdit(Form)
        self.name_edit.setGeometry(QtCore.QRect(90, 50, 113, 20))
        self.name_edit.setObjectName("name_edit")
        self.author_edit = QtWidgets.QLineEdit(Form)
        self.author_edit.setGeometry(QtCore.QRect(90, 90, 113, 20))
        self.author_edit.setObjectName("author_edit")
        self.genre_edit = QtWidgets.QLineEdit(Form)
        self.genre_edit.setGeometry(QtCore.QRect(90, 130, 113, 20))
        self.genre_edit.setObjectName("genre_edit")
        self.back_button = QtWidgets.QPushButton(Form)
        self.back_button.setGeometry(QtCore.QRect(180, 190, 91, 23))
        self.back_button.setObjectName("back_button")
        self.description_edit = QtWidgets.QTextEdit(Form)
        self.description_edit.setGeometry(QtCore.QRect(240, 50, 171, 101))
        self.description_edit.setObjectName("description_edit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(300, 30, 51, 16))
        self.label_4.setObjectName("label_4")
        self.result_label = QtWidgets.QLabel(Form)
        self.result_label.setGeometry(QtCore.QRect(36, 2, 361, 31))
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setObjectName("result_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Создание книги"))
        self.label.setText(_translate("Form", "Название книги"))
        self.label_2.setText(_translate("Form", "Автор"))
        self.label_3.setText(_translate("Form", "Жанр"))
        self.create_button.setText(_translate("Form", "Создать книгу"))
        self.back_button.setText(_translate("Form", "Назад"))
        self.label_4.setText(_translate("Form", "Описание"))
        self.result_label.setText(_translate("Form", "Создание книги."))
