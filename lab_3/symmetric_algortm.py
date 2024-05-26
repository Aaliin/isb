import base64
import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding 

from working_with_a_file import open_file, open_key_des, open_file_bytes, write_text, write_text_bytes


def symmetric_key(byte_count: int) -> bytes:
    """Генерация ключа симметричного алгоритма шифрования

    byte_count - количество байт 
    """
    return os.urandom(byte_count)

def symmetric_encryption(path_initial: str, path_public: str, path_save: str) -> bytes:
    """Осуществляет шифрование и паддинг текста симметричным алгоритмом

    path_initial - путь к шифруемому текстовому файлу
    path_public - путь к файлу с зашированным ключом симметричного алгоритма
    path_save - путь, по которому сохранить зашифрованный текстовый файл
    """ 
    padder = padding.ANSIX923(128).padder()
    initial_text = open_file(path_initial)
    public_key = open_key_des(path_public)
    text = bytes(initial_text, 'UTF-8')
    padded_text = padder.update(text) + padder.finalize() 
    iv = symmetric_key(8)
    cipher = Cipher(algorithms.CAST5(public_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    c_text = encryptor.update(padded_text) + encryptor.finalize()
    write_text_bytes(path_save, c_text)
    return base64.b64encode(iv + c_text)

def symmetric_decryption(path_initial: str, path_private: str, path_save: str) -> str:
    """Осуществляет дешифрование и депаддинг текста симметричным алгоритмом

    path_initial - путь к зашифрованному файлу
    path_private - путь к файлу с дешированным ключом симметричного алгоритма
    path_save - путь, по которому сохранить дешифрованный текстовый файл
    """ 
    encrypted_text = open_file_bytes(path_initial)
    private_key = open_key_des(path_private)
    iv, encrypted_text = encrypted_text[:8], encrypted_text[8:]
    cipher = Cipher(algorithms.CAST5(private_key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    dc_text = decryptor.update(encrypted_text) + decryptor.finalize()
    unpadder = padding.ANSIX923(128).unpadder()
    unpadded_dc_text = unpadder.update(dc_text) + unpadder.finalize()  
    decode_text = unpadded_dc_text.decode("UTF-8")
    write_text(path_save, decode_text) 
    return decode_text
