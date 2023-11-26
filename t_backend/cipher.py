import base64

from Crypto.Cipher import AES
import binascii

from t_backend.settings import settings

cipher = AES.new(settings.AES_KEY, mode=AES.MODE_ECB)


def aes_encrypt(data: str) -> bytes:
    data = data.encode("utf-8")
    block_size = 16
    padding_length = block_size - (len(data) % block_size)
    data += bytes([padding_length]) * padding_length
    encrypted_data = cipher.encrypt(data)
    return binascii.hexlify(encrypted_data)


def aes_decrypt(data: bytes) -> str:
    decrypted_data = cipher.decrypt(binascii.unhexlify(data))
    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]
    return decrypted_data.decode("utf-8", errors="ignore")
