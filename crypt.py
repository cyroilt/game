from cryptography.fernet import Fernet
class crypto():
    def gen_nkey():
        return Fernet.generate_key()
    def encrypt(data,key):
        return Fernet(key).encrypt(data.encode())
    def decrypt(data,key):
        print(type(key))
        return Fernet(key).decrypt(data).decode()

