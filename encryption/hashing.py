import hashlib
import base64

def hash_value(plaintext: str) -> str:
    if plaintext is None:
        return None

    sha256_hash = hashlib.sha256(plaintext.encode('utf-8')).digest()
    return base64.b64encode(sha256_hash).decode('utf-8')


def verify_hash(plaintext: str, stored_hash: str) -> bool:
    if plaintext is None or stored_hash is None:
        return False

    computed_hash = hash_value(plaintext)
    return computed_hash == stored_hash