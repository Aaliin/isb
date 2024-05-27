import json
import logging 


logging.basicConfig(level=logging.INFO)


def read_json(path: str) -> dict:
    """Осуществляет чтение данных из json-файла

    Args:
        path(str) - путь к файлу, необходимый для открытия

    Returns:
        dict - данные json-файла в виде словаря
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as ex:
        logging.error(f"Error reading the file: {ex.message}\n{ex.args}\n") 
        
def saving_values(dict: dict, path: str) -> None:
    """Осуществляет сохранение данных в json-файл

    Args:
        dict(dict) - данные для записи
        path(str) - путь к файлу, в который пойдет запись

    Returns:
        None
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(json.dumps(dict, ensure_ascii=False, indent=4))
    except Exception as ex:
        logging.error(f"An error occurred while saving: {ex.message}\n{ex.args}\n")  