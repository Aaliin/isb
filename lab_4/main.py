import argparse
import logging
import os
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout, 
    QWidget,
    QFileDialog)

from working_with_a_file import read_json
from visualization import algorithm_luna, selection_number, finding_collision


logging.basicConfig(level=logging.INFO)


class Window(QMainWindow):
    def __init__(self) -> None:
        """Создание главного окна"""
        super().__init__()
        self.setGeometry(500, 200, 700, 400)
        self.setWindowTitle("lab_4-var3 Поиск колизии хеш-функции")
        self.setStyleSheet("background-color: #2cf3e2")

        main_widget = QWidget()
        box_layout = QVBoxLayout()
        layout = QGridLayout()

        settings = read_json(os.path.join("lab_4", "settings.json")) 
        self.bins = settings["bins"]
        self.hash = settings["hash"]
        self.four_signs = settings["four_signs"]

        self.number_search = self.add_button("Подобрать номер карты по ее хешу")
        self.luna_algorithm = self.add_button("Проверить корректность при помощи алгоритма Луна")
        self.graph_collision = self.add_button("Замерить время для поиска коллизии хеша")
        self.exit = self.add_button("Выйти из программы")       

        box_layout.addWidget(self.bins)
        box_layout.addWidget(self.hash)
        box_layout.addWidget(self.four_signs)
        box_layout.addWidget(self.number_search)
        box_layout.addWidget(self.luna_algorithm)
        box_layout.addWidget(self.graph_collision)
        box_layout.addWidget(self.exit)
        box_layout.addStretch()   
        layout.addLayout(box_layout, 0, 0)
        layout.addWidget(self.image_label, 0, 1) 

        self.number_search.clicked.connect(self.hash_number)
        self.luna_algorithm.clicked.connect(self.check_correctness)
        self.graph_collision.clicked.connect(self.plotting) 
        self.exit.clicked.connect(self.close)

        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        self.show()

    def add_button(self, name: str) -> QPushButton:
        """Осуществляет добавление кнопки

        Args:
            name(str) - название поля кнопки

        Returns:
            QPushButton - необходимая кнопка
        """
        button = QPushButton(name, self)
        button.resize(button.sizeHint())
        button.setStyleSheet("background-color: #ee5300")
        return button

    def hash_number(self) -> None:
        """Вызывает функцию для подбора номера карты по ее хешу"""
        try:
            folder = QFileDialog.getSaveFileName(
                self,
                "Введите название папки для создания csv-файла:",
            )[0]
            if folder == "":
                QMessageBox.information(
                    None, "Ошибка работы программы!", "Не правильно выбрана папка")
                return
            a = make_list(self.dataset_path, self.classes)
            write_in_file(a, folder)
            QMessageBox.information(
                None, "Результат нажатия кнопки", "Действия успешно выполнены!")
        except Exception as ex:
            logging.error(f"Error in hash_number: {ex}\n") 

    def check_correctness(self) -> None:
        """Вызывает функцию для проверки корректности при помощи алгоритма Луна"""
        try:
            path_base = QFileDialog.getOpenFileName(
                self, "Выберите файл для итерации:")[0]
            path_new = QFileDialog.getSaveFileName(
                self, "Выберите файл куда итерируем:")[0]
            if path_new == "" or path_base == "":
                return
            self.choice_iterator = ChoiceIterator(os.path.relpath(path_base.rpartition('.')[0]),
                                                os.path.relpath(path_new), self.classes[0], self.classes[1])
        except Exception as ex:
            logging.error(f"Error in check_correctness: {ex}\n") 

    def plotting(self) -> None:
        """Вызывает функцию для построения графика времени поиска коллизии хеша от числа процессов"""
        try:
            folder = QFileDialog.getSaveFileName(
                self,
                "Введите название папки для создания csv-файла:",
            )[0]
            if folder == "":
                QMessageBox.information(
                    None, "Ошибка работы программы!", "Не правильно выбрана папка")
                return
            write_in_new(self.dataset_path, self.classes, folder, number)
            QMessageBox.information(
                None, "Результат нажатия кнопки", "Действия успешно выполнены!")
        except Exception as ex:
            logging.error(f"Error in plotting: {ex}\n") 


if __name__ == "__main__": 
    try:
        parser = argparse.ArgumentParser(description="Запуск режимов работы с хешем")
        parser.add_argument("-j", "--json_file", type= str,
                        default=os.path.join("lab_4", "settings.json"),
                        help= "Путь к файлу json")
        args = parser.parse_args()
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec_())
    except Exception as ex:
        logging.error(f"Error in main: {ex}\n") 