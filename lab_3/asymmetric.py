from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa 


def asymmetric_key() -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
    """Генерация пары ключей для асимметричного алгоритма шифрования"""
    keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key = keys
    public_key = keys.public_key()
    return public_key, private_key 
