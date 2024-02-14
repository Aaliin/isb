import os
import logging
import json
from working_with_a_file import open_file, write_text, saving_values

logging.basicConfig(level=logging.INFO)

RUS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def encrypt(path: str, new_path: str, step: int) -> None:
    """Осуществляет шифрование текста; принимает путь к файлу с исходным 
    текстом, путь к новому файлу, в который пойдет запись, и шаг для сдвига"""
    try:
        data = open_file(path)
        cipher_str = ""
        for i in data:
            if i == " ":
                cipher_str += i
                continue
            place = RUS.find(i)
            new_place = (place + step) % len(RUS)
            cipher_str += RUS[new_place]
        write_text(new_path, cipher_str)
    except Exception as ex:
        logging.error(f"Data could not be encrypted : {ex.message}\n{ex.args}\n")


def cipher_key(path: str, step: int) -> None:
    """Осуществляет сохранение ключа от зашифрованного текста; принимает 
    путь к файлу, в который пойдет запись, и шаг для сдвига"""
    try:
        key = dict()
        for i in RUS:
            place = RUS.find(i)
            key[i] = RUS[(place + step) % len(RUS)]
        saving_values(key, path)
    except Exception as ex:
        logging.error(f"Data is not recognized : {ex.message}\n{ex.args}\n") 


if __name__ == "__main__":

    with open(os.path.join("lab_1", "main.json"), "r") as file:
        main = json.load(file)

    encrypt(
        os.path.join(main["directory"], main["folder_1"], main["initial_text"]),
        os.path.join(main["directory"], main["folder_1"],  main["my_encrypted"]),
        main["step"],
    )

    cipher_key(
        os.path.join(main["directory"], main["folder_1"], main["cipher_key"]),
        main["step"],
    )
