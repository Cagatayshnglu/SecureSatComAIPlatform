import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.backends import default_backend

KEY_SIZE = 32
HMAC_KEY_SIZE = 32

def generate_keys():
    return os.urandom(KEY_SIZE), os.urandom(HMAC_KEY_SIZE)

def encrypt_data(aes_key, hmac_key, plaintext):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    ciphertext = cipher.encryptor().update(plaintext) + cipher.encryptor().finalize()
    h = hmac.HMAC(hmac_key, hashes.SHA256(), backend=default_backend())
    h.update(iv + ciphertext)
    tag = h.finalize()
    return iv + ciphertext + tag

def decrypt_data(aes_key, hmac_key, data):
    iv = data[:16]
    tag = data[-32:]
    ciphertext = data[16:-32]
    h = hmac.HMAC(hmac_key, hashes.SHA256(), backend=default_backend())
    h.update(iv + ciphertext)
    h.verify(tag)
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    return cipher.decryptor().update(ciphertext) + cipher.decryptor().finalize()
