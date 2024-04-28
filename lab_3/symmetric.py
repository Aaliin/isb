import os 

def symmetric_key(byte_count: int) -> bytes:
    """Генерация ключа симметричного алгоритма шифрования

    byte_count - количество байт 
    """
    return os.urandom(byte_count)

