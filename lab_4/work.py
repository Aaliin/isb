import hashlib
import logging
import multiprocessing as mp
import time

from matplotlib import pyplot as plt

from working_with_a_file import read_json, saving_values


logging.basicConfig(level=logging.INFO)


def check_hash_card(hash: str, four_signs: str, bins: list, centre_number: int) -> str:
    """Осуществляет сравнение сгенерированного номера карты с заданным хэшем

    Args:
        hash(str) - хеш номера банковской карты
        four_signs(str) - последние 4 цифры карты
        bins(list) - бин карты
        centre_number(int) - середина номера карты

    Returns:
        str - текстовые данные
    """
    try:
        for bin in bins:
            hex_dig = f"{bin}{centre_number:0>6}{four_signs:0>4}"
            hash_sha1 = hashlib.sha1(hex_dig.encode()).hexdigest()
            if hash == hash_sha1:
                print(f"Полученный хеш: \n{hex_dig}")
                return hex_dig
    except Exception as ex:
        logging.error(f"Error in check_hash_card {ex}\n")  

def selection_number(hash: str, four_signs: str, bins: list, save_path: str) -> None:
    """Осуществляет поиск данных банковской карты

    Args:
        hash(str) - хеш номера банковской карты
        four_signs(str) - последние 4 цифры карты
        bins(list) - бин карты
        save_path(str) - путь к файлу, в который пойдет запись

    Returns:
        None
    """
    try:
        cores = mp.cpu_count()
        check = [(hash, four_signs, bins, i) for i in list(range(0, 1000000))]
        with mp.Pool(processes=cores) as p:
            for result in p.starmap(check_hash_card, check):
                if result:
                    saving_values(result, save_path)
                    print(f"Найденный хеш: \n{result}")
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
            print(f"Номер является не корректным")
        return sum % 10 == 0
    except Exception as ex:
        logging.error(f"Error in algorithm_luna {ex}\n")  