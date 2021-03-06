from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
from config import KEY
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
import time, random
import jwt


def decrypt_password(secret_key):
    private_key = KEY['private']
    rsa_key = RSA.importKey(private_key)
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    password = cipher.decrypt(base64.b64decode(secret_key), '')
    return password


def encrypt_password(username, password):
    salt_length = len(password)
    pwd = username+password
    pwd_hash = generate_password_hash(pwd, salt_length=salt_length)
    return pwd_hash


def check_password(hashing, password):
    status = check_password_hash(hashing, password)
    return status


def generate_customer_id():
    customer_id = hashlib.md5(str(time.time())+str(random.random())).hexdigest()
    return customer_id


def generate_cookie(username, password, algorithm='HS256'):
    payload = {'username': username, 'password': password}
    token = jwt.encode(payload, 'secret', algorithm)
    return token[:256]
