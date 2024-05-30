import hashlib
import logging
import os
import multiprocessing as mp
import time

from matplotlib import pyplot as plt

from working_with_a_file import read_json, saving_values


logging.basicConfig(level=logging.INFO)


def check_hash_card(hash: str, four_signs: str, bins: str, centre_number: int) -> str:
    """Осуществляет сравнение сгенерированного номера карты с заданным хэшем

    Args:
        hash(str) - хеш номера банковской карты
        four_signs(str) - последние 4 цифры карты
        bins(str) - бины карты
        centre_number(int) - середина номера карты

    Returns:
        str - текстовые данные
    """
    try:
        hex_dig = f"{bins}{centre_number:0>6}{four_signs:0>4}"
        hash_sha1 = hashlib.sha1(hex_dig.encode()).hexdigest()
        if hash == hash_sha1:
            return hex_dig
    except Exception as ex:
        logging.error(f"Error in check_hash_card {ex}\n")  

def selection_number(hash: str, four_signs: str, bins: list, save_path: str) -> None:
    """Осуществляет поиск данных банковской карты

    Args:
        hash(str) - хеш номера банковской карты
        four_signs(str) - последние 4 цифры карты
        bins(list) - бины карты
        save_path(str) - путь к файлу, в который пойдет запись

    Returns:
        None
    """
    try:
        cores = mp.cpu_count()
        with mp.Pool(processes=cores) as p:
            for bin in bins:
                check = [(hash, four_signs, bin, i) for i in range(0, 1000000)]
                for result in p.starmap(check_hash_card, check):
                    if result: 
                        print(f"Полученный номер: \n{result}")
                        saving_values(result, save_path)
                        return result
    except Exception as ex:
        logging.error(f"Error in selection_number {ex}\n")  

def algorithm_luna(card_number: str) -> bool:
    """Осуществляет проверку корректности номера карты при помощи алгоритма Луна

    Args:
        card_number(str) - номер банковской карты
    
    Returns:
        bool - метка о корректности
    """
    try:
        sum = 0
        reverse = card_number[::-1]
        for i in range(len(reverse)):
            sign = int(reverse[i])
            if i % 2 == 1:
                sign *= 2
                if sign > 9:
                    sign = (sign // 10) + (sign % 10)
                sum += sign
            else:
                sum += sign
        if(sum % 10 == 0):
            print(f"Номер является корректным")
        else: 
            print(f"Номер является некорректным")
        return sum % 10 == 0
    except Exception as ex:
        logging.error(f"Error in algorithm_luna {ex}\n") 

def finding_collision(hash: str, four_signs: str, bins: list) -> None:
    """Осуществляет замер времени для поиска коллизии хеша при различном числе процессов

    Args:
        hash(str) - хеш номера банковской карты
        four_signs(str) - последние 4 цифры карты
        bins(list) - бины карты

    Returns:
        None
    """
    try: 
        times = []
        for i in range(1, int(mp.cpu_count() * 1.5)):
            start = time.time()
            with mp.Pool(processes=i) as p:
                for bin in bins:
                    check = [(hash, four_signs, bin, i) for i in range(0, 1000000)]
                    for result in p.starmap(check_hash_card, check):
                        if result: 
                            times.append(time.time() - start)
                            break
        plt.figure(figsize=(20, 5))
        plt.plot(
            range(len(times)),
            times,
            color='navy', 
            linestyle = '--', 
            marker='*', 
            linewidth=1, 
            markersize=4
        )
        plt.bar(range(len(times)), times, color="blue")
        plt.title("Время для поиска коллизии хеша при различном числе процессов")
        plt.ylabel("Время поиска коллизий")
        plt.xlabel("Число процессов")
        plt.show()
    except Exception as ex:
        logging.error(f"Error in finding_collision {ex}\n")


if __name__ == "__main__": 
    try:
        settings = read_json(os.path.join("lab_4", "settings.json")) 
        result = selection_number(settings["hash"], settings["four_signs"], settings["bins"], settings["card_number"])
        algorithm_luna(result)
        finding_collision(settings["hash"], settings["four_signs"], settings["bins"])
    except Exception as ex:
        logging.error(f"Error in main: {ex}\n") 