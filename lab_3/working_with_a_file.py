import logging


logging.basicConfig(level=logging.INFO)


def open_file(path: str) -> bytes:
    """Осуществляет открытие файла 

path - путь к файлу, необходимый для открытия
"""
    try:
        with open(path, "rb", encoding="utf-8") as file:   
            main = file.read()
        return main
    except Exception as ex:
        logging.error(f"Error opening the file: {ex.message}\n{ex.args}\n")

def write_text(path: str, data: bytes) -> None:
    """Осуществляет запись данных в файл

path - путь к файлу, в который пойдет запись
data - данные для записи
"""
    try:
        with open(path, "wb", encoding="utf-8") as file: 
            file.write(data)
    except Exception as ex:
        logging.error(f"Error writing the file: {ex.message}\n{ex.args}\n")   