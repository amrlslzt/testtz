import asyncio
import sys

from PyQt5 import QtWidgets

import gui.main_window
from library import Library


async def main():
    lib = Library()

    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = gui.main_window.LibraryApp(lib)  # Создаём объект класса LibraryApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    asyncio.run(main())
