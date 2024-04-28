import argparse
import json
import os


from symmetric import symmetric_key
from working_with_a_file import read_json


def main():
    settings = read_json("settings.json") 
    parser = argparse.ArgumentParser( description="Запуск режимов генерации ключей, шифрования и дешифрования")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', action='store_true', help='Запускает режим генерации ключей')
    group.add_argument('-enc', '--encryption', action='store_true', help='Запускает режим шифрования')
    group.add_argument('-dec', '--decryption', action='store_true', help='Запускает режим дешифрования') 
    parser.add_argument('-text', '--initial_text', type=str,
                        default=os.path.join("lab_3", settings["initial_text"]),
                        help='Путь к исходному тексту (lab_3/text/initial_text.txt)')
    parser.add_argument('-public', '--public_key', type=str,
                        default=os.path.join("lab_3", settings["asymmetric_public"]),
                        help='Путь к публичному ключу (lab_3/key/asymmetric/public.pem)')
    parser.add_argument('-private', '--private_key', type=str,
                        default=os.path.join("lab_3", settings["asymmetric_private"]),
                        help='Путь к закрытому ключу (lab_3/key/asymmetric/private.pem)') 
    parser.add_argument('-enctext', '--encrypted_text_file', type=str,
                        default=os.path.join("lab_3", settings["symmetric_encrypted_key"]),
                        help='Путь к зашифрованному файлу (lab_3/key/symmetric/encrypted_key.txt)')
    parser.add_argument('-dectext', '--decrypted_text_file', type=str,
                        default=os.path.join("lab_3", settings["symmetric_decrypted_key"]),
                        help='Путь к расшифрованному файлу (lab_3/key/symmetric/decrypted_key.txt)') 

    if args.generation: 

    elif args.encryption: 

    elif args.decryption: 


if __name__ == "__main__":
    main()
