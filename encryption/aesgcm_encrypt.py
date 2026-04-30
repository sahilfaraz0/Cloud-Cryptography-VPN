from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
def encrypt_aes_gcm(plaintext: str) -> dict:
    if plaintext is None:
        return None

    key = get_random_bytes(32)  # AES-256
    cipher = AES.new(key, AES.MODE_GCM)

    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode('utf-8'))

    return {
        "key": base64.b64encode(key).decode('utf-8'),
        "nonce": base64.b64encode(cipher.nonce).decode('utf-8'),
        "tag": base64.b64encode(tag).decode('utf-8'),
        "ciphertext": base64.b64encode(ciphertext).decode('utf-8')
    }


def decrypt_aes_gcm(encrypted: dict) -> str:
    if encrypted is None:
        return None

    key = base64.b64decode(encrypted["key"])
    nonce = base64.b64decode(encrypted["nonce"])
    tag = base64.b64decode(encrypted["tag"])
    ciphertext = base64.b64decode(encrypted["ciphertext"])

    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    return plaintext.decode('utf-8')