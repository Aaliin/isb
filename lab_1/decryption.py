import os
import logging
import json
from working_with_a_file import open_file, write_text, saving_values


logging.basicConfig(level=logging.INFO)


def text_analysis(path: str, new_path: str) -> None:
    """Осуществляет анализ зашифрованного текста; принимает путь к файлу 
    с исходным текстом, путь к новому файлу, в который пойдет запись"""
    text = open_file(path)
    dict_my = dict() 
    for i in text:
        dict_my[i] = text.count(i) / len(text)
    sort = dict(sorted(dict_my.items(), key=lambda x: x[1], reverse=True))
    saving_values(sort, new_path)  


if __name__ == "__main__":
    with open(os.path.join("lab_1", "main.json"), "r") as file:
        main = json.load(file)
    text_analysis(
        os.path.join(main["directory"], main["folder_2"], main["code_text"]),
        os.path.join(main["directory"], main["folder_2"], main["text_analysis"]),
    ) 