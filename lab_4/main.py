import argparse
import logging
import os
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
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
        self.setGeometry(800, 200, 400, 200)
        self.setWindowTitle("lab_4-var3 Поиск колизии хеш-функции")
        self.setStyleSheet("background-color: #2cf3e2")

        main_widget = QWidget()
        box_layout = QVBoxLayout()
        layout = QGridLayout()

        settings = read_json(os.path.join("lab_4", "settings.json")) 
        self.bins = settings["bins"]
        self.hash = settings["hash"]
        self.four_signs = settings["four_signs"] 
        self.card_number = ""

        self.label_hash = QLabel(f"Hash: {self.hash}")
        self.label_four_signs = QLabel(f"Four signs: {self.four_signs}")
        self.label_bins = QLabel(f"Bins: {str(self.bins).strip('[]')}")

        self.number_search = self.add_button("Подобрать номер карты по ее хешу")
        self.luna_algorithm = self.add_button("Проверить корректность при помощи алгоритма Луна")
        self.graph_collision = self.add_button("Замерить время для поиска коллизии хеша")
        self.exit = self.add_button("Выйти из программы") 

        box_layout.addWidget(self.label_hash)
        box_layout.addWidget(self.label_bins)
        box_layout.addWidget(self.label_four_signs) 
        box_layout.addWidget(self.number_search)
        box_layout.addWidget(self.luna_algorithm)
        box_layout.addWidget(self.graph_collision)
        box_layout.addWidget(self.exit)
        box_layout.addStretch()   
        layout.addLayout(box_layout, 0, 0)

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
            path = QFileDialog.getSaveFileName(
                self,
                "Введите название файла, в который сохранить номер карты:",
                "lab_4//",
                "JSON File(*.json)",
            )[0]
            if (path == ""):
                QMessageBox.information(None, "Ошибка ввода данных", "Не указаны все необходимые данные карты")
            else:
                result = selection_number(self.hash, self.four_signs, [int(item) for item in self.bins], path)
                self.card_number = result
                if result:
                    QMessageBox.information(None, "Результат нажатия", "Номер карты найден")
                else:
                    QMessageBox.information(None, "Результат нажатия", "Номер карты не найден")
        except Exception as ex:
            logging.error(f"Error in hash_number: {ex}\n") 

    def check_correctness(self) -> None:
        """Вызывает функцию для проверки корректности при помощи алгоритма Луна"""
        try:
            if self.card_number == "":
                QMessageBox.information(None, "Номер карты не найден", "Не подобран номер карты")
            else:
                result = algorithm_luna(self.card_number)
                if result:
                    QMessageBox.information(None, "Результат нажатия", "Номер является корректным")
                else:
                    QMessageBox.information(None, "Результат нажатия", "Номер является некорректным")
        except Exception as ex:
            logging.error(f"Error in check_correctness: {ex}\n") 

    def plotting(self) -> None:
        """Вызывает функцию для построения графика времени поиска коллизии хеша от числа процессов"""  
        try:
            if self.card_number == "":
                QMessageBox.information(None, "Номер карты не найден", "Не подобран номер карты")
            else:
                finding_collision(self.hash, self.four_signs, [int(item) for item in self.bins])
                QMessageBox.information(None, "Результат нажатия", "График успешно построен")
        except Exception as ex:
            logging.error(f"Error in plotting: {ex}\n") 


if __name__ == "__main__": 
    try:
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec())
    except Exception as ex:
        logging.error(f"Error in main: {ex}\n") 