import json
import logging 


logging.basicConfig(level=logging.INFO)


def open_file(path: str) -> str:
    """Осуществляет чтение из файла 

    path - путь к файлу, необходимый для открытия
    """
    try:
        with open(path, "r", encoding="utf-8") as file:   
            main = file.read()
        return main
    except Exception as ex:
        logging.error(f"Error opening the file: {ex.message}\n{ex.args}\n")

def open_file_bytes(path: str) -> str: 
    """Осуществляет чтение из файла в бинарном режиме

    path - путь к файлу, необходимый для открытия
    """
    try: 
        with open(path, "rb") as file:  
            main = file.read()
        return main
    except Exception as ex:
        logging.error(f"Error opening the file: {ex.message}\n{ex.args}\n")

def open_key_des(path: str) -> bytes:
    """Десериализация ключа симметричного алгоритма

    path - путь к файлу, необходимый для открытия
    """
    try:
        with open(path, "rb") as file:   
            main = file.read()
        return main
    except Exception as ex:
        logging.error(f"Error opening the file: {ex.message}\n{ex.args}\n") 

def write_text(path: str, data: str) -> None:
    """Осуществляет запись данных в файл 

    path - путь к файлу, в который пойдет запись
    data - данные для записи
    """
    try:
        with open(path, "w", encoding="utf-8") as file: 
            file.write(data)
    except Exception as ex:
        logging.error(f"Error writing the file: {ex.message}\n{ex.args}\n") 

def write_text_bytes(path: str, data: str) -> None: 
    """Осуществляет запись данных в файл в бинарном режиме

    path - путь к файлу, в который пойдет запись
    data - данные для записи
    """
    try:
        with open(path, "wb") as file: 
            file.write(data)
    except Exception as ex:
        logging.error(f"Error opening the file: {ex.message}\n{ex.args}\n")

def write_key_ser(path: str, key: bytes) -> None:
    """Сериализация ключа симмеричного алгоритма в файл

    path - путь к файлу, в который пойдет запись
    key - данные для записи
    """
    try:
        with open(path, "wb") as file: 
            file.write(key)
    except Exception as ex:
        logging.error(f"Error writing the file: {ex.message}\n{ex.args}\n") 

def read_json(path: str) -> dict:
    """Осуществляет чтение данных из json-файла
    
    path - путь к файлу, в который пойдет запись
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as ex:
        logging.error(f"Error reading the file: {ex.message}\n{ex.args}\n")   