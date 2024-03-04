import json
import logging
import os

from working_with_a_file import open_file, write_text, saving_values


logging.basicConfig(level=logging.INFO)

RUS = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def cipher_key(path: str, key_my: str) -> dict:
    """Осуществляет сохранение ключа от зашифрованного текста;
    принимает путь к файлу, в который пойдет запись и слово, 
    которое используется в качестве ключа
    """
    try:
        key = dict()
        for i in range(len(key_my)):
            place = RUS.find(key_my[i])
            key[i] = place
        saving_values(key, path)
    except Exception as ex:
        logging.error(f"Data is not recognized: {ex.message}\n{ex.args}\n")
    return key


def encrypt(path: str, new_path: str, key_my: dict) -> None:
    """Осуществляет шифрование текста; принимает путь к файлу с 
    исходным текстом, путь к новому файлу, в который пойдет запись
    и директорию, содержащую сдвиги, в соответвии с выбранным словом
    """
    try:
        data = open_file(path)
        cipher_str = ""
        for i in range(len(data)):
            if data[i] == " ":
                cipher_str += " "
            else:
                place = (RUS.find(data[i]) + key_my[i % len(key_my)]) % len(RUS) 
                cipher_str += RUS[place]
        write_text(new_path, cipher_str)
    except Exception as ex:
        logging.error(f"Data could not be encrypted: {ex.message}\n{ex.args}\n")


def decoded(path: str, new_path: str, key_my: dict) -> None:
    """Осуществляет дешифрование текста; принимает путь к файлу с 
    зашифрованным текстом, путь к новому файлу, в который пойдет запись
    и директорию, содержащую сдвиги, в соответвии с выбранным словом
    """
    try:
        data = open_file(path)
        cipher_str = ""
        for i in range(len(data)):
            if data[i] == " ":
                cipher_str += " "
            else:
                place = (RUS.find(data[i]) - key_my[i % len(key_my)] + len(RUS)) % len(RUS) 
                cipher_str += RUS[place]
        write_text(new_path, cipher_str)
    except Exception as ex:
        logging.error(f"Data could not be encrypted: {ex.message}\n{ex.args}\n")


if __name__ == "__main__":
    with open(os.path.join("lab_1", "settings.json"), "r", encoding="utf-8") as file:
        settings = json.load(file)
    cipher_key = cipher_key(
        os.path.join(settings["directory"], settings["folder_1"], settings["cipher_key"]),
        settings["key"],
    )
    encrypt(
        os.path.join(settings["directory"], settings["folder_1"], settings["initial_text"]),
        os.path.join(settings["directory"], settings["folder_1"], settings["my_encrypted"]),
        cipher_key
    )
    decoded(
        os.path.join(settings["directory"], settings["folder_1"], settings["my_encrypted"]),
        os.path.join(settings["directory"], settings["folder_1"], settings["decrypted"]),
        cipher_key
    )
