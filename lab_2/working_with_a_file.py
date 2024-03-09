import json
import logging


logging.basicConfig(level=logging.INFO)


def write_text(path: str, data: str) -> None:
    """Осуществляет запись данных в файл принимает 
    путь к файлу и данные для записи
    """
    try:
        with open(path, "w", encoding="utf-8") as file: 
            file.write(data)
    except Exception as ex:
        logging.error(f"Error writing the file: {ex.message}\n{ex.args}\n")


def saving_values(dict: dict, path: str) -> None:
    """Осуществляет сохранение данных в json-файл
    принимает путь к файлу и данные для записи
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(json.dumps(dict, ensure_ascii=False, indent=4))
    except Exception as ex:
        logging.error(f"An error occurred while saving: {ex.message}\n{ex.args}\n")