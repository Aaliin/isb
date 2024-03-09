import json
import logging
import math
import os


from working_with_a_file import write_text, saving_text

logging.basicConfig(level=logging.INFO)


def frequency_bitwise_test(data: str, path: str) -> None:
    sum_n = 0
    dict_value = {"0": -1, "1": 1}
    try:
        for i in data:
            sum_n += dict_value[i]
        sum_n = sum_n/math.sqrt(len(data))
        p_value = math.erfc(sum_n/math.sqrt(2))
        write_text(path, p_value)
    except Exception as ex:
        logging.error(f"Division by zero: {ex.message}\n{ex.args}\n") 


def same_consecutive_bits(data: str, path: str) -> None:
    sum_n = 0
    dict_value = {"0": -1, "1": 1}
    try:
        for i in data:
            sum_n += dict_value[i]
        sum_n = sum_n/len(data)
        comparison = abs(sum_n-0.5)
        module = 2/math.sqrt(len(data))
        if comparison >= module:
            return 0
        v_n = 0
        for i in len(data)-1:
            if data[i] != data[i+1]:
                v_n += 1
        p_value = math.erfc((abs(v_n-2*len(data)*sum_n*(1-sum_n))) /
                            (2*sum_n*(1-sum_n)*math.sqrt(2*len(data))))
        write_text(path, p_value)
    except Exception as ex:
        logging.error(f"Division by zero: {ex.message}\n{ex.args}\n") 


def longest_sequence_of_units(data: str, path: str) -> None:
    block_length = 8 
    count = len(data)/block_length
    try: 
        value = 0
        for i in range(0, len(data)-block_length, block_length):
            if data[i] == 1 and data[i+1] == 0:
                value += 1

        p_value = 
        write_text(path, p_value)
    except Exception as ex:
        logging.error(f"Division by zero: {ex.message}\n{ex.args}\n")


if __name__ == "__main__":
    with open(os.path.join("lab_2", "settings.json"), "r") as file:
        settings = json.load(file)
    frequency_bitwise_test(settings["c++"],
                        os.path.join(settings["directory"], settings["folder_1"], settings["c_sequence"]),)
    same_consecutive_bits(settings["c++"],
                        os.path.join(settings["directory"], settings["folder_2"], settings["c_sequence"]),)
    longest_sequence_of_units(settings["c++"],
                            os.path.join(settings["directory"], settings["folder_3"], settings["c_sequence"]),)


    frequency_bitwise_test(settings["java"],
                        os.path.join(settings["directory"], settings["folder_1"], settings["java_sequence"]),)
    same_consecutive_bits(settings["java"],
                        os.path.join(settings["directory"], settings["folder_2"], settings["java_sequence"]),)
    longest_sequence_of_units(settings["java"],
                            os.path.join(settings["directory"], settings["folder_3"], settings["java_sequence"]),)
