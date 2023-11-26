import base64

from Crypto.Cipher import AES
import binascii

from t_backend.settings import settings

cipher = AES.new(settings.AES_KEY, mode=AES.MODE_ECB)


def aes_encrypt(data: str) -> bytes:
    block_size = 64
    padding_length = block_size - (len(data) % block_size)
    data += chr(padding_length) * padding_length
    data = base64.b64encode(data.encode())
    return binascii.hexlify(cipher.encrypt(data))


def aes_decrypt(data: bytes) -> str:
    decrypted = cipher.decrypt(binascii.unhexlify(data))
    decrypted = base64.b64decode(decrypted)
    padding_length = decrypted[-1]
    decrypted = decrypted[:-padding_length]
    return decrypted.decode("utf-8")
