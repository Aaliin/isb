import logging

from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import rsa 


logging.basicConfig(level=logging.INFO) 


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
