from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import base64


def encrypt_chacha20(plaintext: str) -> dict:
    if plaintext is None:
        return None

    key = get_random_bytes(32)  # 256-bit key
    cipher = ChaCha20.new(key=key)

    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))

    return {
        "key": base64.b64encode(key).decode('utf-8'),
        "nonce": base64.b64encode(cipher.nonce).decode('utf-8'),
        "ciphertext": base64.b64encode(ciphertext).decode('utf-8')
    }


def decrypt_chacha20(encrypted: dict) -> str:
    if encrypted is None:
        return None

    key = base64.b64decode(encrypted["key"])
    nonce = base64.b64decode(encrypted["nonce"])
    ciphertext = base64.b64decode(encrypted["ciphertext"])

    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)

    return plaintext.decode('utf-8')

