import json
import logging
import os

from working_with_a_file import open_file, write_text, saving_values


logging.basicConfig(level=logging.INFO)


def text_analysis(path: str, new_path: str) -> None:
    """Осуществляет анализ зашифрованного текста; принимает путь к файлу 
    с исходным текстом, путь к новому файлу, в который пойдет запись
    """
    text = open_file(path)
    dict_my = dict()
    for i in text:
        dict_my[i] = text.count(i) / len(text)
    sort = dict(sorted(dict_my.items(), key=lambda x: x[1], reverse=True))
    saving_values(sort, new_path)


def decoded(old_str: str, new_str: str, text: str, path: str, dict: dict) -> str:
    """Осуществляет замену символов в тексте; принимает исходный символ, символ на 
    который заменяем, зашифрованный текст, путь к файлу, в который пойдет запись 
    """
    text = text.replace(old_str, new_str)
    dict[old_str] = new_str
    saving_values(dict, path)
    return text


def decryption(path: str, new_path: str, keys: str) -> None:
    """Осуществляет расшифровку исходного текста; принимает путь к файлу с исходным 
    текстом, путь к новому файлу, в который пойдет запись, ключ шифрования
    """
    try:
        text = open_file(path)
        with open(keys, "r", encoding="utf-8") as file:
            dict = json.load(file)
        for key, value in dict.items():
            text = text.replace(key, value)
        write_text(new_path, text)
    except Exception as ex:
        logging.error(f"The directory could not be opened: {ex.message}\n{ex.args}\n")


if __name__ == "__main__":
    with open(os.path.join("lab_1", "setting.json"), "r") as file:
        settings = json.load(file)
    text_analysis(
        os.path.join(settings["directory"], settings["folder_2"], settings["code_text"]),
        os.path.join(settings["directory"], settings["folder_2"], settings["text_analysis"]),
    )
    decryption(
        os.path.join(settings["directory"], settings["folder_2"], settings["code_text"]),
        os.path.join(settings["directory"], settings["folder_2"], settings["decrypted"]),
        os.path.join(settings["directory"], settings["folder_2"], settings["cipher_key"]),
    )
