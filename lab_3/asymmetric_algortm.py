from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

from key_deserialization import private_key_des, public_key_des
from working_with_a_file import open_key_des, write_key_ser, write_text


def asymmetric_key() -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
    """Генерация пары ключей для асимметричного алгоритма шифрования"""
    keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key = keys
    public_key = keys.public_key()
    return public_key, private_key

def asymmetric_encryption(public: str, path_initial_key: str, path_encryption: str) -> None:
    """Осуществляет шифрование и паддинг текста асимметричным алгоритмом

    public - путь к файлу с public ключом
    path_initial_key - путь к файлу с исходным симметричным ключом
    path_encryption - путь к файлу для сохранения зашифрованного симметричного ключа 
    """
    text = open_key_des(path_initial_key)
    public_key = public_key_des(public)
    encripted_text = public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(
        algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    write_text(path_encryption, encripted_text)


def asymmetric_decryption(private: str, path_encryption: str, path_decryption: str) -> bytes:
    """Осуществляет дешифрование и депаддинг текста асимметричным алгоритмом

    private - путь к файлу с private ключом
    path_encryption - путь к файлу с сохраненным зашифрованным симметричным ключом
    path_decryption - путь к файлу с дешифрованным симметричным ключом
    """
    text = open_key_des(path_encryption)
    private_key = private_key_des(private)
    decripted_text = private_key.decrypt(text, padding.OAEP(mgf=padding.MGF1(
        algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    write_key_ser(path_decryption, decripted_text)
    return decripted_text
