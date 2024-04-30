import logging

from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


logging.basicConfig(level=logging.INFO)


def public_key_ser(public_pem: str, public_key: rsa.RSAPublicKey)-> None:
    """Осуществляет сериализацию открытого ключа в файл

    public_pem - путь к файлу, в который пойдет запись 
    public_key - открытый rsa ключ
    """ 
    try:
        with open(public_pem, 'wb') as public_out:
            public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo))
    except Exception as ex:
        logging.error(f"Error writing the file: {ex.message}\n{ex.args}\n")  
            
def private_key_ser(private_pem: str, private_key: rsa.RSAPrivateKey)->None:
    """Осуществляет сериализацию закрытого ключа в файл

    public_pem - путь к файлу, в который пойдет запись 
    private_key - закрытый rsa ключ
    """ 
    try:
        with open(private_pem, 'wb') as private_out:
            private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()))
    except Exception as ex:
        logging.error(f"Error writing the file: {ex.message}\n{ex.args}\n")  

def public_key_des(public_pem: str)-> rsa.RSAPublicKey:
    """Осуществляет десериализацию открытого ключа в файл

    public_pem - путь к файлу, в который пойдет запись  
    """ 
    try:
        with open(public_pem, 'rb') as pem_in:
            public_bytes = pem_in.read()
        return load_pem_public_key(public_bytes)
    except Exception as ex:
        logging.error(f"Error writing the file: {ex.message}\n{ex.args}\n") 
            
def private_key_des(private_pem: str)->rsa.RSAPrivateKey:
    """Осуществляет десериализацию закрытого ключа в файл

    public_pem - путь к файлу, в который пойдет запись  
    """ 
    try:
        with open(private_pem, 'rb') as pem_in:
            private_bytes = pem_in.read()
        return load_pem_private_key(private_bytes,password=None,)
    except Exception as ex:
        logging.error(f"Error writing the file: {ex.message}\n{ex.args}\n")