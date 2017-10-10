from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
from config import KEY
from werkzeug.security import generate_password_hash, check_password_hash


def decrypt_password(secret_key):
    private_key = KEY['private_key']
    rsa_key = RSA.importKey(private_key)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    password = cipher.decrypt(base64.b64decode(secret_key), '')
    return password


def encrypt_password(username, password):
    salt_length = len(password)
    pwd = username+password
    pwd_hash = generate_password_hash(pwd, salt_length=salt_length)
    return pwd_hash


def check_password(hash, password):
    status = check_password_hash(hash, password)
    return status
