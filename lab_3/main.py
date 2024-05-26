import argparse
import os

from enum import Enum

from asymmetric_algortm import asymmetric_key, asymmetric_encryption, asymmetric_decryption
from key_serialization import private_key_ser, public_key_ser
from symmetric_algortm import symmetric_key, symmetric_encryption, symmetric_decryption
from working_with_a_file import write_key_ser, read_json


class Choice(Enum):
    GENERATE_SYMMETRIC_KEY = 0
    GENERATE_ASYMMETRIC_KEYS = 1
    ENCRYPT_SYMMETRIC_KEY = 2
    ENCRYPT_TEXT = 3
    DECRYPT_SYMMETRIC_KEY = 4
    DECRYPT_TEXT = 5


def main():
    settings = read_json(os.path.join("lab_3", "settings.json")) 
    parser = argparse.ArgumentParser(description="Запуск режимов генерации ключей, шифрования и дешифрования")
    parser.add_argument("-c", "--choice", type=int,
                        help="Выбор режима работы: "
                            "0 - генерация симметричного ключа"
                            "1 - генерация ассимметричных ключей"
                            "2 - шифрование симметричного ключа"
                            "3 - шифрование текста"
                            "4 - дешифрование симметричного ключа"
                            "5 - дешифрование текста") 
    args = parser.parse_args()  

    match (args.choice):
        case Choice.GENERATE_SYMMETRIC_KEY.value: 
            write_key_ser(settings["symmetric_key"], symmetric_key(16))

        case Choice.GENERATE_ASYMMETRIC_KEYS.value:
            public_key, private_key = asymmetric_key()
            public_key_ser(settings["asymmetric_public"], public_key)
            private_key_ser(settings["asymmetric_private"], private_key)

        case Choice.ENCRYPT_SYMMETRIC_KEY.value:
            asymmetric_encryption(
                settings["symmetric_key"], settings["asymmetric_public"], settings["symmetric_encrypted_key"])

        case Choice.ENCRYPT_TEXT.value:
            encrypted_text = symmetric_encryption(
                settings["initial_text"], settings["symmetric_key"], settings["encrypted_text"])
            print(f"Зашифрованный текст: \n{encrypted_text}")

        case Choice.DECRYPT_SYMMETRIC_KEY.value:
            asymmetric_decryption(settings["symmetric_encrypted_key"],
                                settings["asymmetric_private"], settings["symmetric_decrypted_key"])

        case Choice.DECRYPT_TEXT.value:
            decrypted_text = symmetric_decryption(
                settings["encrypted_text"], settings["symmetric_key"], settings["decrypted_text"])
            print(f"Дешифрованный текст: \n{decrypted_text}")

        case _:
            print("Неправильный вид работы с данными")

if __name__ == "__main__":
    main()
